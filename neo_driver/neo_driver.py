from neo4j import GraphDatabase
from neo_driver.neo_value import NeoValue
from pycalc import dc, Driver, DefaultCostModel

class NodePattern:
  def __init__(self, binding, label):
    self.binding = binding
    self.label = label

  def bindings(self):
    bindings = []
    if self.binding:
      bindings.append(self.binding)
    return bindings

  def to_cypher(self):
    cypher = "("
    if self.binding:
      cypher += self.binding
    if self.label:
      cypher += ":" + self.label
    cypher += ")"
    return cypher

class RelPattern:
  def __init__(self, lhs, rhs, binding, types):
    self.lhs = lhs
    self.rhs = rhs
    self.binding = binding
    self.types = types

  def bindings(self):
    bindings = self.lhs.bindings() + self.rhs.bindings()
    if self.binding:
      bindings.append(self.binding)
    return bindings

  def to_cypher(self):
    pattern = [self.lhs.to_cypher(), "-["]
    if self.binding:
        pattern.append(self.binding)
    if self.types:
        pattern.append(":")
        for i, tpe in enumerate(self.types):
          if i != 0:
              pattern.append("|")
          pattern.append(tpe)
    pattern.append("]->")
    pattern.append(self.rhs.to_cypher())
    return ''.join(pattern)

class NeoQuery:
  def __init__(self):
    self.patterns = []
    self.predicate = None
    self.expr = None

  def to_cypher(self):
    if not self.patterns:
      raise RuntimeError

    bindings = []
    for pattern in self.patterns:
      bindings += pattern.bindings()

    if not (self.expr or bindings):
      raise RuntimeError

    query = ["MATCH ", ", ".join([pattern.to_cypher() for pattern in self.patterns])]
    if self.predicate:
      query.append(" WHERE ")
      query.append(self.predicate)

    query.append(" RETURN ")
    if (self.expr):
      query.append(self.expr)
    else:
      query.append(", ".join(bindings))
    
    return ''.join(query)


class NeoDriver(Driver):
  neo_ops = set([
    dc.MATCH,
    dc.FILTER,
    dc.SELECT,
    dc.GROUP_BY,
    dc.GRAPH_NODE,
    dc.GRAPH_RELATION,
  ]) | dc.BASIC_EXPR

  def __init__(self, prefix, neo_uri=None, **neo_params):
    super().__init__(prefix)
    self.connection = GraphDatabase.driver(neo_uri, **neo_params) if neo_uri else None
    self._cost_model = DefaultCostModel()

  def get_call_cost(self, node, arg_costs):
    if node.func == dc.MATCH and not self._match_prefix(node):
      return None
    elif node.func not in self.neo_ops:
      return None
    else:
      return self._cost_model.get_call_cost(node, arg_costs)

  def get_import_cost(self, source_driver, source_binding):
    return None

  def evaluate(self, node, args):
    expr = None

    # clauses

    if node.func == dc.MATCH:
      expr = NeoQuery()
      expr.patterns = [arg.expr for arg in args]

    elif node.func == dc.FILTER:
      expr = args[0].expr
      expr.predicate = args[1].expr

    elif node.func == dc.SELECT:
      expr = args[0].expr
      fields = [arg.expr + " AS " + label for (arg, label) in zip(args[1:], node.attrs["labels"])]
      expr.expr = ", ".join(fields)

    elif node.func == dc.GROUP_BY:
      expr = args[0].expr
      aggs = node.attrs["aggs"]
      exprs = [arg.expr for arg in args[1:]]
      labels = node.attrs["labels"]
      fields = [
        f"{ex} AS {label}" if agg == "key" else f"{agg}({ex}) AS {label}" 
        for agg, ex, label in zip(aggs, exprs, labels)
      ]
      expr.expr = ", ".join(fields)

    # node expression

    elif node.func == dc.GRAPH_NODE:
      binding = node.attrs["alias"] if "alias" in node.attrs else None
      label = node.attrs["label"] if "label" in node.attrs else None
      expr = NodePattern(binding, label)

    elif node.func == dc.GRAPH_RELATION:
      binding = node.attrs["alias"] if "alias" in node.attrs else None
      types = node.attrs["types"] if "types" in node.attrs else None
      expr = RelPattern(args[0].expr, args[1].expr, binding, types)

    # literals

    elif node.func in [
        dc.INT,
        dc.FLOAT
    ]:
        expr = str(node.attrs["value"])

    elif node.func == dc.STRING:
        expr = "\"" + node.attrs["value"] + "\""

    # context expressions

    elif node.func == dc.READ_CTX:
        expr = ".".join(node.attrs["path"])

    # bool expressions

    elif node.func == dc.NOT:
      expr = "NOT " + args[0].expr

    elif node.func == dc.AND:
        expr = args[0].expr + " AND " + args[1].expr

    elif node.func == dc.OR:
        expr = args[0].expr + " OR " + args[1].expr

    elif node.func == dc.EQ:
        expr = args[0].expr + " = " + args[1].expr

    elif node.func == dc.GT:
        expr = args[0].expr + " > " + args[1].expr

    elif node.func == dc.GE:
        expr = args[0].expr + " >= " + args[1].expr

    elif node.func == dc.LT:
        expr = args[0].expr + " < " + args[1].expr

    elif node.func == dc.LE:
        expr = args[0].expr + " <= " + args[1].expr

    # num expressions

    elif node.func == dc.ADD:
        expr = args[0].expr + " + " + args[1].expr

    elif node.func == dc.SUB:
        expr = args[0].expr + " - " + args[1].expr

    elif node.func == dc.MULT:
        expr = args[0].expr + " * " + args[1].expr

    elif node.func == dc.DIV:
        expr = args[0].expr + " / " + args[1].expr

    elif node.func == dc.MOD:
        expr = args[0].expr + " % " + args[1].expr
        
    else:
        raise RuntimeError("unknown: " + repr(node))

    return NeoValue(expr, self), False

  def import_(self, source_driver, value, alias, paths):
    raise NotImplementedError

  def __str__(self):
      return f"Neo4j@{self.prefix}"

  def __repr__(self):
      return self.__str__()
