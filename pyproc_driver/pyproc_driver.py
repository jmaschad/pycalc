import importlib
import logging
from os import path
from time import time

import pandas as pd

import pyproc
from pycalc import DefaultCostModel, Driver, dc
from pyproc_driver.pyproc_value import PyProcValue

logger = logging.getLogger(__name__)

class PyProcDriver(Driver):
  pyproc_ops =  dc.SQL_OPS | dc.BASIC_EXPR

  def __init__(self, prefix, base_dir = None):
    super().__init__(prefix)
    self._base_dir = base_dir
    self._cost_model = DefaultCostModel(perf_factor=2)

  def get_call_cost(self, node, arg_costs):
    if node.func == dc.SCAN and not (self._base_dir and self._match_prefix(node)):
      return None
    elif node.func not in self.pyproc_ops:
      return None
    else:
      return self._cost_model.get_call_cost(node, arg_costs)

  def get_import_cost(self, source_driver, source_binding):
    if source_binding.node.func in dc.VALUE_OPS and any([
      isinstance(source_driver, importlib.import_module('mongo_driver').MongoDriver),
      isinstance(source_driver, importlib.import_module('neo_driver').NeoDriver),
      isinstance(source_driver, importlib.import_module('pg_driver').PgDriver),
    ]):
      return self._cost_model.get_import_cost(source_binding.cost)
    else:
      return None

  def evaluate(self, node, args):
    expr = None

    if node.func == dc.SCAN:
      file_path = node.attrs["path"][1]
      if not file_path.startswith("file://"):
        raise RuntimeError
      _, ext = path.splitext(file_path)
      if not ext in [".parquet"]:
        raise RuntimeError
      abs_file_path = repr(path.join(self._base_dir, file_path[7:]))
      columns = [path[-1] for path in node.attrs["read_paths"]]
      logger.debug("Schedule scan of %s with columns %s", abs_file_path, columns)
      expr = f'''pyproc.scan({abs_file_path}, {repr(columns)})'''

    elif node.func == dc.SELECT:
      exprs = ", ".join(['lambda ctx: ' + arg.expr for arg in args[1:]])
      labels = repr(node.attrs["labels"])
      expr = f'''pyproc.select({args[0].expr}, [{exprs}], labels={labels})'''

    elif node.func == dc.FILTER:
      expr = f'''pyproc.filter({args[0].expr}, lambda ctx: {args[1].expr})'''

    elif node.func == dc.CROSS_JOIN:
      expr = f'''pyproc.cross({args[0].expr}, {args[1].expr})'''

    elif node.func in [
      dc.INNER_JOIN,
      dc.LEFT_JOIN,
      dc.RIGHT_JOIN,
      dc.FULL_JOIN
    ]:
      how = node.func[:-5].lower()
      expr = f'''pyproc.join({args[0].expr}, {args[1].expr}, {repr(how)}, lambda ctx: {args[2].expr}, lambda ctx: {args[3].expr})'''

    elif node.func == dc.UNION_ALL:
      expr = f'''pyproc.union_all({args[0].expr}, {args[1].expr})'''

    elif node.func == dc.LIMIT:
      expr = f'''pyproc.limit({args[0].expr}, {node.attrs["limit"]})'''

    elif node.func == dc.OFFSET:
      expr = f'''pyproc.offset({args[0].expr}, {node.attrs["offset"]})'''

    elif node.func == dc.ORDER_BY:
      value = args[0].expr
      order = node.attrs["order"]
      cols, asc = zip(*order)
      expr = f'''pyproc.orderby({value}, {repr([col - 1 for col in cols])}, {repr(list(asc))})'''

    elif node.func == dc.GROUP_BY:
      # COPY PASTE from SELECT
      exprs = ", ".join(['lambda ctx: ' + arg.expr for arg in args[1:]])
      labels = node.attrs["labels"]
      projection = f'''pyproc.select({args[0].expr}, [{exprs}], labels={repr(labels)})'''
      
      keys = []
      aggs = {}
      for label, agg in zip(labels, node.attrs["aggs"]):
        if agg == "key":
          keys.append(label)
          aggs[label] = "first"
        else:
          aggs[label] = agg
      expr = f'''pyproc.groupby({projection}, {repr(keys)}, {repr(aggs)})'''

    # literals
    elif node.func in [
        dc.INT,
        dc.FLOAT,
        dc.STRING
    ]:
      expr = repr(node.attrs["value"])

    # context expressions

    elif node.func == dc.READ_CTX:
      expr = f'''pyproc.read_ctx(ctx, {repr(node.attrs["path"])})'''

    # type casts

    elif node.func == dc.TO_BOOL:
      expr = f'''bool({args[0].expr})'''

    elif node.func == dc.TO_INT:
      expr = f'''int({args[0].expr})'''

    elif node.func == dc.TO_DOUBLE:
      expr = f'''float({args[0].expr})'''

    # bool expressions

    elif node.func == dc.NOT:
      expr = self._nest("not", args[0].expr)

    elif node.func == dc.AND:
      expr = self._nest(args[0].expr, "and", args[1].expr)

    elif node.func == dc.OR:
      expr = self._nest(args[0].expr, "or", args[1].expr)

    elif node.func == dc.EQ:
      expr = self._nest(args[0].expr, '==', args[1].expr)

    elif node.func == dc.GT:
      expr = self._nest(args[0].expr, '>', args[1].expr)

    elif node.func == dc.GE:
      expr = self._nest(args[0].expr, '>=', args[1].expr)

    elif node.func == dc.LT:
      expr = self._nest(args[0].expr, '<', args[1].expr)

    elif node.func == dc.LE:
      expr = self._nest(args[0].expr, '<=', args[1].expr)

    # num expressions
    elif node.func == dc.ADD:
      expr = self._nest(args[0].expr, '+', args[1].expr)

    elif node.func == dc.SUB:
      expr = self._nest(args[0].expr, '-', args[1].expr)

    elif node.func == dc.MULT:
      expr = self._nest(args[0].expr, '*', args[1].expr)

    elif node.func == dc.DIV:
      expr = self._nest(args[0].expr, '/', args[1].expr)

    elif node.func == dc.MOD:
      expr = self._nest(args[0].expr, '%', args[1].expr)

    # date expressions
    elif node.func in dc.DATE_EXPR:
      expr = f'''pyproc.{node.func.lower()}({args[0].expr})'''

    else:
      raise RuntimeError('unknown node: ' + repr(node))
    
    if not isinstance(expr, str):
      raise RuntimeError

    local_scope = {}
    for arg in args:
      local_scope.update(arg.local_scope)
      
    if "definition" in node.attrs:
      alias = repr(node.attrs["definition"])
      expr = f'''pyproc.as_({expr}, {alias})'''

    return PyProcValue(expr, local_scope, self), False

  def is_table_type(self, frame):
    for idx, tpe in enumerate(frame.dtypes):
      if (
        tpe == object and 
        not pd.api.types.is_string_dtype(frame.iloc[:, idx])
      ):
        return False
    return True

  def import_(self, source_driver, value, alias, paths):
    ident = type(value).__name__ + str(id(value))
    start = time()
    frame = value.to_pandas()
    if alias:
      frame = pyproc.as_(frame, alias)

    frame_size = int(frame.memory_usage().sum() / 2**10)
    logger.info("Import %d KB from %s in %.3f seconds", frame_size, source_driver.prefix, time() - start)
    value = PyProcValue(ident, {ident: frame}, self, is_table=self.is_table_type(frame), real_size=frame_size / 2**10)
    return value, value.is_table

  def _nest(self, *elems):
    return '(' + ' '.join(elems) + ')'

  def __str__(self):
    return f'PyCalc@{self.prefix}'
      
  def __repr__(self):
    return self.__str__()
