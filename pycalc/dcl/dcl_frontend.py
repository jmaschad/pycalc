import logging
from time import time

from antlr4 import *

from pycalc import Scheduler, dc
from pycalc.dc.dsl import DCBuilder
from pycalc.dcl.generated.DCLLexer import DCLLexer
from pycalc.dcl.generated.DCLListener import DCLListener
from pycalc.dcl.generated.DCLParser import DCLParser
from pycalc.scheduler.memo import Memo

logger = logging.getLogger("dcl_frontend")

SELECT_CLAUSE = "SELECT_CLAUSE"
MATCH_CLAUSE = "MATCH_CLAUSE"
FROM_TABLE_CLAUSE = "FROM_TABLE_CLAUSE"
FROM_MATCH_CLAUSE = "FROM_MATCH_CLAUSE"
WHERE_CLAUSE = "WHERE_CLAUSE"
GROUPBY_CLAUSE = "GROUPBY_CLAUSE"
ORDERBY_CLAUSE = "ORDERBY_CLAUSE"
LIMIT_CLAUSE = "LIMIT_CLAUSE"

class Query:
  pass

class BaseQuery(Query):
  def __init__(self):
    self.current_clause = None
    self.is_group_by = False
    self.is_graph_match = True
    self.tables = []
    self.predicate = None
    self.result_columns = {}
    self.order_columns = []
    self.limit = None
    self.offset = None

  def to_memo(self):
    builder = self.to_builder()
    builder.fix_definitions()
    memo = Memo()
    memo.root_idx = builder.append_to_memo(memo)
    return memo

  def to_builder(self):
    table = self.tables[0]
    for other in self.tables[1:]:
      table = table.cross_join(other)
    
    if self.predicate:
      table = table.filter(self.predicate)
    
    if self.is_group_by:
      result_columns = {}

      # We implicitly add key columns to the result. 
      # We remove them here if they are duplicated by explicitly defined user columns
      known_paths = set()
      for name, col in self.result_columns.items():
        if isinstance(col, DCBuilder):
          if col._func != dc.READ_CTX:
            raise ValueError

          path = tuple(col._attrs["path"])
          if name.startswith("__group_key") and path in known_paths:
            continue
          known_paths.add(path)

          result_columns[name] = dc.key(col)
        else:
          result_columns[name] = col
      
      table = table.group_by(result_columns)
    elif self.result_columns:
      table = table.select(self.result_columns)

    if self.order_columns:
      table = table.order_by(*self.order_columns)

    if self.limit:
      table = table.limit(self.limit)

    if self.offset:
      table = table.offset(self.offset)

    return table

class CompoundQuery(Query):
  def __init__(self, lhs, rhs, op):
    self.lhs = lhs
    self.rhs = rhs
    self.op = op

  def to_memo(self, memo):
    memo = Memo()
    builder = self.to_builder()
    builder.fix_definitions()
    memo.root_idx = builder.append_to_memo(memo)
    return memo

  def to_builder(self):
    if self.op == "union_all":
      return self.lhs.to_builder().union_all(self.rhs.to_builder())
    else:
      raise RuntimeError

class DCLBaseListener(DCLListener):
  def __init__(self):
    self.stack = []
    self.clause_stack = []
    self.binding_stack = []

  @property
  def clause(self):
    if self.clause_stack:
      return self.clause_stack[-1]
    else:
      return None

  def push(self, builder):
    self.stack.append(builder)

  def pop(self):
    return self.stack.pop()

  def top(self):
    return self.stack[-1]

  def enterWithQuery(self, ctx):
    self.binding_stack.append({})

  def exitWithQuery(self, ctx):
    self.binding_stack.pop()

  def exitCommonTableExpressionRule(self, ctx):
    query = self.pop()
    scope = self.binding_stack[-1]
    scope[ctx.alias.text] = query.to_builder()

  def getBinding(self, alias):
    for scope in reversed(self.binding_stack):
      if alias in scope:
        return scope[alias]
    return None

  def enterSelectClauseRule(self, ctx):
    self.clause_stack.append(SELECT_CLAUSE)

  def exitSelectClauseRule(self, ctx):
    self.clause_stack.pop()

  def enterFromTableRule(self, ctx):
    self.clause_stack.append(FROM_TABLE_CLAUSE)

  def exitFromTableRule(self, ctx):
    self.clause_stack.pop()

  def enterFromMatchRule(self, ctx):
    self.clause_stack.append(FROM_MATCH_CLAUSE)

  def exitFromMatchRule(self, ctx):
    self.clause_stack.pop()

  def enterWhereClauseRule(self, ctx):
    self.clause_stack.append(WHERE_CLAUSE)

  def exitWhereClauseRule(self, ctx):
    self.clause_stack.pop()

  def enterGroupByClauseRule(self, ctx):
    self.clause_stack.append(GROUPBY_CLAUSE)

  def exitGroupByClauseRule(self, ctx):
    self.clause_stack.pop()

  def enterOrderByClauseRule(self, ctx):
    self.clause_stack.append(ORDERBY_CLAUSE)

  def exitOrderByClauseRule(self, ctx):
    self.clause_stack.pop()

  def enterLimitClauseRule(self, ctx):
    self.clause_stack.append(LIMIT_CLAUSE)

  def exitLimitClauseRule(self, ctx):
    self.clause_stack.pop()

class DCLQueryListener(DCLBaseListener):

  def exitSqlQueryRule(self, ctx):
    if ctx.compoundOps:
      tables = []
      ops = []
      for _ in range(len(ctx.compoundOps)):
        tables.append(self.pop())
        ops.append(self.pop())
      root_table = self.pop()
      for op, table in zip(reversed(ops), reversed(tables)):
        root_table = CompoundQuery(root_table, table, op)
      self.push(root_table)

  def enterTableExpressionRule(self, ctx):
    self.push(BaseQuery())

  def exitWhereClauseRule(self, ctx):
    predicate = self.pop()
    query = self.top()
    query.predicate = predicate

  def exitUnionAll(self, ctx):
    self.push("union_all")

  def exitTableRule(self, ctx):
    alias = None
    if ctx.tableAliasRule():
      alias = self.pop()
    
    table = self.pop()
    if alias:
      table._attrs["definition"] = alias
    
    query = self.top()
    query.tables.append(table)
  
  def exitFromMatchRule(self, ctx):
    path = ctx.system.text
    patterns = []
    for _ in range(len(ctx.patterns)):
      patterns.append(self.pop())
    query = self.top()
    query.is_graph_match = True
    query.tables.append(dc.match(path, *reversed(patterns)))

  def exitExpressionResult(self, ctx):
    col_expr = self.pop()

    alias = None
    if ctx.columnAlias:
      alias = ctx.columnAlias.text
    elif isinstance(col_expr, DCBuilder) and col_expr._func == dc.READ_CTX:
      alias = col_expr._attrs["path"][-1]
    else:
      raise RuntimeError("Can not derive column name")

    query = self.top()
    query.result_columns[alias] = col_expr

  def exitGroupByClauseRule(self, ctx):
    keys = []
    for _ in range(len(ctx.groupBy)):
      keys.append(self.pop())
    query = self.top()
    query.is_group_by = True
    for i, key in enumerate(keys):
      query.result_columns["__group_key" + str(i)] = key

  def exitOrderByClauseRule(self, ctx):
    order_columns = []
    for _ in range(len(ctx.expr)):
      order_columns.append(self.pop())
    query = self.top()
    query.order_columns = order_columns

  def exitOrderingTermRule(self, ctx):
    self.push((int(ctx.column.text), not ctx.order or ctx.order == DCLParser.K_ASC))

  def exitLimitClauseRule(self, ctx):
    offset = None
    if ctx.offset:
      offset = int(ctx.offset.text)
    limit = int(ctx.limit.text)
    query = self.top()
    query.limit = limit
    query.offset = offset

  def exitPathExpression(self, ctx):
    segments = [seg.text for seg in ctx.segments]
    binding = self.getBinding(segments[0])
    if len(segments) == 1 and binding:
      self.push(binding)
    elif self.clause == FROM_TABLE_CLAUSE:
      segments = [seg.strip("'") for seg in segments]
      table = dc.scan(*segments)
      self.push(table)
    else:
      self.push(dc.ctx(*segments))

  def exitLowCompExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    if ctx.op.type in [DCLParser.EQ1, DCLParser.EQ2]:
      self.push(lhs == rhs)
    elif ctx.op.type in [DCLParser.NOT_EQ1, DCLParser.NOT_EQ2]:
      self.push(lhs != rhs)
    else:
      raise RuntimeError
  
  def exitHighCompExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    if ctx.op.type == DCLParser.LT:
      self.push(lhs < rhs)
    elif ctx.op.type == DCLParser.LT_EQ:
      self.push(lhs <= rhs)
    elif ctx.op.type == DCLParser.GT:
      self.push(lhs > rhs)
    elif ctx.op.type == DCLParser.GT_EQ:
      self.push(lhs >= rhs)
    else:
      raise RuntimeError

  def exitNotExpression(self, ctx):
    val = self.pop()
    self.push(dc.not_(val))

  def exitAndExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    self.push(dc.and_(lhs, rhs))

  def exitOrExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    self.push(dc.or_(lhs, rhs))

  def exitBetweenExpression(self, ctx):
    upper = self.pop()
    lower = self.pop()
    value = self.pop()
    self.push(dc.and_(
      value >= lower,
      value <= upper
    ))

  def exitHighMathExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    if ctx.op.type == DCLParser.STAR:
      self.push(lhs * rhs)
    elif ctx.op.type == DCLParser.DIV:
      self.push(lhs / rhs)
    elif ctx.op.type == DCLParser.MOD:
      self.push(lhs % rhs)
    else:
      raise RuntimeError

  def exitLowMathExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    if ctx.op.type == DCLParser.PLUS:
      self.push(lhs + rhs)
    elif ctx.op.type == DCLParser.MINUS:
      self.push(lhs - rhs)
    else:
      raise RuntimeError

  def exitApplyExpression(self, ctx):
    func = ctx.func.text.lower()
    args = []
    for i in range(len(ctx.args)):
      args.append(self.pop())
    if func == "count":
      if len(args) != 1:
        raise RuntimeError
      self.push(dc.count(args[0]))
    elif func == "sum":
      if len(args) != 1:
        raise RuntimeError
      self.push(dc.sum(args[0]))
    elif func == "min":
      if len(args) != 1:
        raise RuntimeError
      self.push(dc.min(args[0]))
    elif func == "max":
      if len(args) != 1:
        raise RuntimeError
      self.push(dc.max(args[0]))
    else:
      raise RuntimeError

  def exitIsExpression(self, ctx):
    lhs = self.pop()
    rhs = self.pop()
    if ctx.negate:
      self.push(lhs != rhs)
    else:
      self.push(lhs == rhs)

  def exitTableAliasRule(self, ctx):
    self.push(ctx.tableAlias.text)  

  def exitGraphPathRule(self, ctx):
    to_node = self.pop()
    rel = None
    if ctx.rel:
      rel = self.pop()
    from_node = self.pop()
    self.push(from_node.rel(rel).to(to_node))

  def exitGraphNodeRule(self, ctx):
    name = ctx.name.text
    label = ctx.label.text if ctx.label else None
    self.push(dc.node(name, label))

  def exitGraphRelationRule(self, ctx):
    self.push(ctx.relType.text)

  def enterNumericLiteral(self, ctx):
    raw = ctx.getText()
    if "." in raw:
      self.push(dc.float(float(raw)))
    else:
      self.push(dc.int(int(raw)))
  
  def enterStringLiteral(self, ctx):
    self.push(dc.string(ctx.getText().strip("'")))

def parse_dcl(query):
  start = time()
  input_stream = InputStream(query)
  lexer = DCLLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = DCLParser(stream)
  tree = parser.queryRule()
  walker = ParseTreeWalker()
  front_end = DCLQueryListener()
  walker.walk(front_end, tree)
  result = front_end.pop()
  if front_end.stack:
    raise RuntimeError
  memo = result.to_memo()
  logger.info("DCL translation completed %.3f seconds", time() - start)
  return memo
