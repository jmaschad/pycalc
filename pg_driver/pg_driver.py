import importlib
import logging
from time import time, time_ns

import psycopg2 as pg
from psycopg2.extras import execute_values

from pg_driver.pg_value import PgValue
from pypika import Field, Order, Query, Table
from pypika import functions as fn
from pypika.enums import JoinType
from pycalc import Cost, DefaultCostModel, Driver, dc

logger = logging.getLogger(__name__)

class PgDriver(Driver):
  _pg_ops = dc.SQL_OPS | dc.BASIC_EXPR

  _join_type = {
    dc.INNER_JOIN: JoinType.inner,
    dc.LEFT_JOIN: JoinType.left_outer,
    dc.RIGHT_JOIN: JoinType.right_outer,
    dc.FULL_JOIN: JoinType.full_outer
  }

  def __init__(self, prefix, **pg_params):
    super().__init__(prefix)
    self._cost_model = DefaultCostModel()
    self.connection = pg.connect(**pg_params) if pg_params else None

  def get_call_cost(self, node, arg_costs):
    if node.func == dc.SCAN and not self._match_prefix(node):
      return None
    elif node.func not in self._pg_ops:
      return None
    else:
      return self._cost_model.get_call_cost(node, arg_costs)

  def get_import_cost(self, source_driver, source_binding):
    if (
      isinstance(source_driver, importlib.import_module('pyproc_driver').PyProcDriver) and 
      source_binding.node.func == dc.INTERMEDIATE and
      source_binding.node.attrs["value"].is_table
    ):
      cost = self._cost_model.get_import_cost(source_binding.cost)
      logger.debug("Created import estimate %s for binding %d", cost, id(source_binding))
      return cost
    else:
      return None

  def evaluate(self, node, args):
    expr = None

    # clauses

    if node.func == dc.SCAN:
      table_path = node.attrs['path'][1:]
      if len(table_path) != 1:
        raise ValueError
      expr = Table(table_path[0])

    elif node.func == dc.SELECT:
      table = self.to_query(args[0].expr)
      exprs = [arg.expr for arg in args[1:]]
      expr = table.select(*[
        field.as_(label) for (field, label) in zip(exprs, node.attrs['labels'])
      ])

    elif node.func == dc.FILTER:
      table = self.to_query(args[0].expr)
      predicate = args[1].expr
      expr = table.where(predicate)

    elif node.func == dc.CROSS_JOIN:
      lhs = self.to_query(args[0].expr)
      rhs = args[1].expr
      if isinstance(rhs, Table):
        expr = lhs.from_(rhs)
      else:
        expr = lhs.cross_join(rhs).cross()

    elif node.func in [
      dc.INNER_JOIN,
      dc.LEFT_JOIN,
      dc.RIGHT_JOIN,
      dc.FULL_JOIN
    ]:
      lhs = self.to_query(args[0].expr)
      rhs = args[1].expr
      lhs_key = args[2].expr
      rhs_key = args[3].expr
      join_type = self._join_type[node.func]
      predicate = lhs_key == rhs_key
      join = lhs.join(rhs, how=join_type).on(predicate)
      expr = join

    elif node.func == dc.UNION_ALL:
      first = self.to_query(args[0].expr)
      second = self.to_query(args[0].expr)
      expr = first.union_all(second)

    elif node.func == dc.GROUP_BY:
      table = self.to_query(args[0].expr)
      labels = node.attrs["labels"]
      aggs = node.attrs["aggs"]
      expressions = [arg.expr for arg in args[1:]]
      keys = []

      for idx, agg in enumerate(aggs):
        if agg == 'key':
          keys.append(idx + 1)
        elif agg == 'count':
          expressions[idx] = fn.Count(expressions[idx]).as_(labels[idx])
        elif agg == 'sum':
          expressions[idx] = fn.Sum(expressions[idx]).as_(labels[idx])
        elif agg == 'min':
          expressions[idx] = fn.Min(expressions[idx]).as_(labels[idx])
        elif agg == 'max':
          expressions[idx] = fn.Max(expressions[idx]).as_(labels[idx])
      
      expr = table.groupby(*keys).select(*expressions)

    elif node.func == dc.LIMIT:
      table = self.to_query(args[0].expr)
      expr = table.limit(node.attrs['limit'])

    elif node.func == dc.OFFSET:
      table = self.to_query(args[0].expr)
      expr = table.offset(node.attrs['offset'])

    elif node.func == dc.ORDER_BY:
      table = self.to_query(args[0].expr)
      for expr in node.args[1:]:
        order = Order.asc if expr.attrs.get('order', 'asc') == 'asc' else Order.desc
        table = table.orderby(expr, order=order)
      expr = table

    # literals

    elif node.func in [
      dc.INT,
      dc.FLOAT,
      dc.STRING
    ]:
      expr = node.attrs['value']

    # context expressions

    elif node.func == dc.READ_CTX:
      path = node.attrs['path']
      if len(path) != 2:
        raise RuntimeError
      expr = Field(path[1], table=Table(path[0]))

    # bool expressions

    elif node.func == dc.NOT:
      expr = args[0].expr.negate()

    elif node.func == dc.AND:
      expr = args[0].expr & args[1].expr

    elif node.func == dc.OR:
      expr = args[0].expr | args[1].expr

    elif node.func == dc.EQ:
      expr = args[0].expr == args[1].expr

    elif node.func == dc.GT:
      expr = args[0].expr > args[1].expr

    elif node.func == dc.GE:
      expr = args[0].expr >= args[1].expr

    elif node.func == dc.LT:
      expr = args[0].expr < args[1].expr

    elif node.func == dc.LE:
      expr = args[0].expr <= args[1].expr

    # num expressions

    elif node.func == dc.ADD:
      expr = args[0].expr + args[1].expr

    elif node.func == dc.SUB:
      expr = args[0].expr - args[1].expr

    elif node.func == dc.MULT:
      expr = args[0].expr * args[1].expr

    elif node.func == dc.DIV:
      expr = args[0].expr / args[1].expr

    elif node.func == dc.MOD:
      expr = args[0].expr % args[1].expr

    # date expressions

    elif node.func == dc.GET_YEAR:
      expr = fn.Extract('YEAR', args[0].expr)

    elif node.func == dc.GET_MONTH:
      expr = fn.Extract('YEAR', args[0].expr)

    elif node.func == dc.GET_DAY:
      expr = fn.Extract('YEAR', args[0].expr)

    else:
      raise RuntimeError('unknown node: ' + repr(node))
    
    if "definition" in node.attrs:
      expr = expr.as_(node.attrs["definition"])

    return PgValue(expr, self), False

  def _to_sql_type(self, dtype):
    if dtype == int:
      return "integer"
    elif dtype == float:
      return "double precision"
    elif dtype == object:
      return "text"
    else:
      raise ValueError

  def import_(self, source_driver, value, alias, paths):
    frame = value.to_pandas()[[tuple(path) for path in paths]]
    frame_size = int(frame.memory_usage().sum() / 2**10)
    cols = list(zip(*frame.columns.to_list()))[-1]

    typed_cols = []
    for name, tpe in zip(cols, frame.dtypes.to_list()):
      typed_cols.append(name + " " + self._to_sql_type(tpe))
    
    name = "import" + str(time_ns())
    create_query = "CREATE TEMP TABLE " + name + " (" + ", ".join(typed_cols) + ");"
    insert_query = "INSERT INTO " + name + " (" + ", ".join(cols) + ") values %s"

    tuples = list(frame.itertuples(index=False))

    start = time()
    with self.connection.cursor() as cur:
      cur.execute(create_query)
      execute_values(cur, insert_query, tuples)
      self.connection.commit()
    
    logger.info("Import %d KB from %s in %.3f seconds", frame_size, source_driver.prefix, time() - start)

    return PgValue(Table(name).as_(alias), self), False
  
  def to_query(self, table):
    return Query.from_(table, auto_star=True) if isinstance(table, Table) else table

  def __str__(self):
    return f'PostgreSQL@{self.prefix}'
      
  def __repr__(self):
    return self.__str__()
