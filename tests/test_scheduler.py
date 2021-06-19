import unittest

from pycalc import Cost, DefaultCostModel, Driver, Scheduler, dc
from pycalc.scheduler.rewrites.default_rewrites import default_rewrites

IMPORT = "IMPORT"

class Trace:
  def __init__(self, traces, skip_unknown=False):
    self._traces = traces
    
    self._whitelist = set()
    if skip_unknown:
      for trace in traces.values():
        for func in trace:
          self._whitelist.add(func)
  
  def check(self, driver, func):
    if self._whitelist and func not in self._whitelist:
      return

    prefix = driver.prefix

    if not prefix in self._traces:
      raise TraceError("Unknown driver: " + prefix)

    trace = self._traces[prefix]

    if not trace:
      raise TraceError(f"Unexpected call: {str(func)}@{prefix}. Expected end of trace")

    if func != trace[0]:
      raise TraceError(f"Unexpected call: {str(func)}@{prefix}. Expected {str(trace[0])}")

    del trace[0]

class TraceError(Exception):
  pass

class SqlTestDriver(Driver):
  def __init__(self, prefix, trace, *source_drivers):
    super().__init__(prefix)
    self._cost_model = DefaultCostModel()
    self._source_drivers = list(source_drivers)
    self._trace = trace

  def evaluate(self, node, args):
    self._trace.check(self, node.func)
    return self, False

  def import_(self, source_driver, definition, value):
    self._trace.check(self, IMPORT)
    return self, False

  def get_import_cost(self, source_driver, source_binding):
    if source_driver in self._source_drivers and source_binding.node.func in dc.SQL_OPS:
      return self._cost_model.get_import_cost(source_binding.cost)
    else:
      return None

  def get_call_cost(self, node, arg_costs):
    if node.func == dc.SCAN and not self._match_prefix(node):
      return None
    else:
      return self._cost_model.get_call_cost(node, arg_costs)
      
class TestScheduler(unittest.TestCase):
  def test_scan(self):
    memo = dc.scan("db", "nation", as_="n").to_memo()
    
    trace = Trace({"db": [dc.SCAN]})
    driver = SqlTestDriver("db", trace)
    scheduler = Scheduler(drivers=[driver])
    
    try:
      scheduler.schedule(memo)
    except TraceError as er:
      self.fail(er)
    
  def test_filter(self):
    memo = dc.scan("db", "customer", as_="c").filter(
      dc.and_(
        dc.ctx("c", "balance") >= dc.float(0.0),
        dc.ctx("c", "balance") <= dc.float(1000.0)
      )
    ).to_memo()

    trace = Trace({"db": [dc.SCAN, dc.FILTER]}, skip_unknown=True)
    driver = SqlTestDriver("db", trace)
    scheduler = Scheduler(drivers=[driver])
    
    try:
      scheduler.schedule(memo)
    except TraceError as er:
      self.fail(er)
    
  def test_multi_driver(self):
    memo = dc.scan("db1", "customer", as_="c").inner_join(
      dc.scan("db2", "order", as_="o"),
      dc.ctx("c", "id"),
      dc.ctx("o", "cust_id")
    ).filter(
        dc.ctx("c", "balance") <= dc.float(1000.0)
    ).to_memo()
    
    trace = Trace({
      "db1": [dc.SCAN],
      "db2": [IMPORT, dc.SCAN, dc.INNER_JOIN, dc.FILTER]
    }, skip_unknown=True)

    driver1 = SqlTestDriver("db1", trace)
    driver2 = SqlTestDriver("db2", trace, driver1)
    scheduler = Scheduler(drivers=[driver1, driver2])

    try:
      scheduler.schedule(memo)
    except TraceError as er:
      self.fail(er)
    
  def test_multi_driver_opt_1(self):
    memo = dc.scan("db1", "customer", as_="c").inner_join(
      dc.scan("db2", "order", as_="o"),
      dc.ctx("c", "id"),
      dc.ctx("o", "cust_id")
    ).filter(
        dc.ctx("c", "balance") <= dc.float(1000.0)
    ).to_memo()

    trace = Trace({
      "db1": [dc.SCAN, dc.FILTER],
      "db2": [IMPORT, dc.SCAN, dc.INNER_JOIN]
    }, skip_unknown=True)

    driver1 = SqlTestDriver("db1", trace)
    driver2 = SqlTestDriver("db2", trace, driver1)
    scheduler = Scheduler(
      drivers=[driver1, driver2],
      rewrites=default_rewrites()
    )

    try:
      scheduler.schedule(memo)
    except TraceError as er:
      self.fail(er)
  
  def test_multi_driver_opt_2(self):
    memo = dc.scan("db1", "facts", as_="f").cross_join(
      dc.scan("db2", "orders", as_="o")
    ).cross_join(
      dc.scan("db3", "date", as_="d")
    ).filter(
      dc.and_(
        dc.ctx("f", "order_id") == dc.ctx("o", "id"),
        dc.ctx("o", "gross") > dc.float(10000.0),
        dc.ctx("o", "tax") < dc.float(8.0),
        dc.ctx("o", "discount") < dc.float(2.0),
        dc.ctx("f", "date_id") == dc.ctx("d", "id"),
        dc.ctx("d", "year") == dc.int(2020),
        dc.ctx("d", "month") == dc.int(1),
      )
    ).to_memo()

    trace = Trace({
      "db1": [dc.SCAN, IMPORT, dc.INNER_JOIN, IMPORT, dc.INNER_JOIN],
      "db2": [dc.SCAN, dc.FILTER],
      "db3": [dc.SCAN, dc.FILTER]
    }, skip_unknown=True)

    driver2 = SqlTestDriver("db2", trace)
    driver3 = SqlTestDriver("db3", trace)
    driver1 = SqlTestDriver("db1", trace, driver2, driver3)
    
    scheduler = Scheduler(
      drivers=[driver1, driver2, driver3],
      rewrites=default_rewrites()
    )

    try:
      scheduler.schedule(memo)
    except TraceError as er:
      self.fail(er)
