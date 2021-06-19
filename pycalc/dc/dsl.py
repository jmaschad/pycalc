from functools import reduce

from pycalc import dc
from pycalc.scheduler.memo import Memo, Node


def scan(*path, as_=None):
  attrs = { "path": path }
  if as_:
    attrs["definition"] = as_
  
  return DCBuilder(dc.SCAN, **attrs)


def match(path, *patterns):
  return DCBuilder(dc.MATCH, *patterns, path=(path, ))


def ctx(*path):
  return DCBuilder(dc.READ_CTX, path=path)


def bool(value):
  return DCBuilder(dc.BOOL, value=value)


def int(value):
  return DCBuilder(dc.INT, value=value)


def float(value):
  return DCBuilder(dc.FLOAT, value=value)


def string(value):
  return DCBuilder(dc.STRING, value=value)


def not_(node_or_builder):
  return DCBuilder(dc.NOT, node_or_builder)


def and_(*nodes_or_builders):
  return reduce(lambda lhs, rhs: DCBuilder(dc.AND, lhs, rhs), nodes_or_builders)


def or_(*nodes_or_builders):
  return reduce(lambda lhs, rhs: DCBuilder(dc.OR, lhs, rhs), nodes_or_builders)


def nulls_first(builder):
  builder._attrs['nulls'] = 'first'
  return builder


def nulls_last(builder):
  builder._attrs['nulls'] = 'last'
  return builder

class Agg:
  def __init__(self, builder, func):
    self.builder = builder
    self.func = func


class DCBuilder:

  def __init__(self, func, *args, **attrs):
    self._func = func
    self._args = args
    self._attrs = attrs

  # Front-ends may set definitions too high in the builder tree.
  # For example, DCL infers definitions from aliases which might
  # be set on ORDER BY, LIMIT, or UNION nodes instead of the 
  # corresponding SELECT, GROUPBY etc. This method moves definitions
  # down the tree.
  def fix_definitions(self, definition=None):
    def set_definition():
      if (
        definition and 
        "definition" in self._attrs and
        definition != self._attrs["definition"]
      ):
        raise RuntimeError("Can not redefine definition")
      elif definition:
        self._attrs["definition"] = definition
    
    def get_definition():
      self_def = None
      if "definition" in self._attrs:
        self_def = self._attrs["definition"]
        del self._attrs["definition"]
      
      if definition and self_def and definition != self_def:
        raise RuntimeError("Can not fix multiple definitions")

      if self_def:
        return self_def
      else:
        return definition
      
    if self._func in [dc.SCAN, dc.MATCH]:
      set_definition()
    
    elif self._func in [dc.SELECT, dc.GROUP_BY]:
      set_definition()
      self._args[0].fix_definitions()
    
    elif self._func in dc.SQL_JOIN_OPS:
      set_definition()
      self._args[0].fix_definitions()
      self._args[1].fix_definitions()

    elif self._func in dc.UNION_ALL:
      d = get_definition()
      self._args[0].fix_definitions(d)
      self._args[1].fix_definitions(d)

    elif self._func in [dc.FILTER, dc.LIMIT, dc.OFFSET, dc.ORDER_BY]:
      self._args[0].fix_definitions(get_definition())

    else:
      raise ValueError("Unknown func")

  def to_memo(self):
    memo = Memo()
    memo.root_idx = self.append_to_memo(memo)
    return memo

  def append_to_memo(self, memo):
    arg_ids = tuple(arg.append_to_memo(memo) for arg in self._args)
    return memo.append(Node(self._func, arg_ids, self._attrs))

  # BOOL

  def and_(self, value):
    return DCBuilder(dc.AND, self, value)

  def or_(self, value):
    return DCBuilder(dc.OR, self, value)

  def __eq__(self, value):
    return DCBuilder(dc.EQ, self, value)

  def __ne__(self, value):
    return DCBuilder(dc.NE, self, value)

  def __gt__(self, value):
    return DCBuilder(dc.GT, self, value)

  def __ge__(self, value):
    return DCBuilder(dc.GE, self, value)

  def __lt__(self, value):
    return DCBuilder(dc.LT, self, value)

  def __le__(self, value):
    return DCBuilder(dc.LE, self, value)

  # NUMERIC

  def __neg__(self):
    return DCBuilder(dc.NEG, self)

  def __add__(self, value):
    return DCBuilder(dc.ADD, self, value)

  def __sub__(self, value):
    return DCBuilder(dc.SUB, self, value)

  def __mul__(self, value):
    return DCBuilder(dc.MULT, self, value)

  def __truediv__(self, value):
    return DCBuilder(dc.DIV, self, value)

  def __mod__(self, value):
    return DCBuilder(dc.MOD, self, value)

  # DATE

  def year(self):
    return DCBuilder(dc.GET_YEAR, self)

  def month(self):
    return DCBuilder(dc.GET_MONTH, self)

  def day(self):
    return DCBuilder(dc.GET_DAY, self)
    

  # TRANSFORMATION

  def to_bool(self):
    return DCBuilder(dc.TO_BOOL, self)

  def to_int(self):
    return DCBuilder(dc.TO_INT, self)

  def to_double(self):
    return DCBuilder(dc.TO_DOUBLE, self)

  # DATA OPS
  def select(self, columns, as_=None):
    labels = []
    expressions = []
    for label, expression in columns.items():
      labels.append(label)
      expressions.append(expression)

    attrs = { "labels": labels }
    if as_:
      attrs["definition"] = as_

    return DCBuilder(dc.SELECT, self, *expressions, **attrs)

  def group_by(self, groups, as_=None):
    labels = []
    aggs = []
    expressions = []
    for label, group in groups.items():
      if not isinstance(group, Agg):
        raise ValueError
      labels.append(label)
      aggs.append(group.func)
      if (group.builder):
        expressions.append(group.builder)

    attrs = { "labels": labels, "aggs": aggs }
    if as_:
      attrs["definition"] = as_

    return DCBuilder(dc.GROUP_BY, self, *expressions, **attrs)

  def filter(self, expr):
    return DCBuilder(dc.FILTER, self, expr)

  def cross_join(self, that):
    return DCBuilder(dc.CROSS_JOIN, self, that)

  def inner_join(self, that, self_key, that_key):
    return DCBuilder(dc.INNER_JOIN, self, that, self_key, that_key)

  def left_join(self, that, self_key, that_key):
    return DCBuilder(dc.LEFT_JOIN, self, that, self_key, that_key)

  def right_join(self, that, self_key, that_key):
    return DCBuilder(dc.RIGHT_JOIN, self, that, self_key, that_key)

  def full_join(self, that, self_key, that_key):
    return DCBuilder(dc.FULL_JOIN, self, that, self_key, that_key)

  def union_all(self, that):
    return DCBuilder(dc.UNION_ALL, self, that)

  def limit(self, limit):
    return DCBuilder(dc.LIMIT, self, limit=limit)

  def offset(self, offset):
    return DCBuilder(dc.OFFSET, self, offset=offset)

  def order_by(self, *cols):
    return DCBuilder(dc.ORDER_BY, self, order=cols)


def node(alias=None, label=None):
  return NodeBuilder(alias, label)

class NodeBuilder:
  def __init__(self, alias, label):
    self._alias = alias
    self._label = label

  def rel(self, *types, alias=None):
    return RelBuilder(self, types=types, alias=alias)

  def append_to_memo(self, memo):
    attrs = {}
    if self._label:
      attrs['label'] = self._label
    if self._alias:
      attrs['alias'] = self._alias
    return memo.append(Node(dc.GRAPH_NODE, (), attrs))

class RelBuilder:
  def __init__(self, node, types, alias):
    self._from = node
    self._types = types
    self._alias = alias
  
  def to(self, node):
    return Tripple(self._from, self, node)

class Tripple:
  def __init__(self, fromNode, rel, toNode):
    self._fromNode = fromNode
    self._rel = rel
    self._toNode = toNode
  
  def append_to_memo(self, memo):
    attrs = {}
    if self._rel._types:
      attrs['types'] = self._rel._types
    if self._rel._alias:
      attrs['alias'] = self._rel._alias
    
    return memo.append(Node(
      dc.GRAPH_RELATION, 
      (self._fromNode.append_to_memo(memo), self._toNode.append_to_memo(memo)),
      attrs,
    ))
