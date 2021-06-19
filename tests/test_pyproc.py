import unittest

from pycalc import dc, Scheduler
from pyproc_driver import PyProcDriver

class TestPyProc(unittest.TestCase):

  def test_expression(self):
    memo = (
      (dc.ctx("o", "a1") * dc.int(5)) == dc.int(42)
    ).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(PyProcDriver("pp"))
    
    res = scheduler.schedule(memo)
    self.assertEqual(res.expr, '''((pyproc.read_ctx(ctx, ('o', 'a1')) * 5) == 42)''')
  
  def test_scan_file(self):
    memo = dc.scan("pp", "file://items.parquet", as_="n").select({
        "name": dc.ctx("n", "line_nr")
    }).to_memo()

    scheduler = Scheduler()
    scheduler.add_driver(PyProcDriver("pp", base_dir="data"))
    res = scheduler.schedule(memo)
    self.assertIsNotNone(res.to_pandas())
