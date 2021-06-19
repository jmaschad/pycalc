from pymongo import MongoClient
from pycalc import dc, Cost, DefaultCostModel, Driver
from mongo_driver.mongo_value import MongoValue, MongoPipeline

class MongoDriver(Driver):
  mongo_ops = set([
      dc.SCAN,
      dc.SELECT,
      dc.FILTER,
      dc.LIMIT,
      dc.OFFSET,
    ]) | dc.BASIC_EXPR

  def __init__(self, prefix, dbname, mongo_params={}):
    super().__init__(prefix)
    self._connection = MongoClient(**mongo_params)
    self.database = self._connection[dbname]
    self._cost_model = DefaultCostModel()

  def get_call_cost(self, node, arg_costs):
    if node.func == dc.SCAN and not self._match_prefix(node):
      return None
    elif node.func not in self.mongo_ops:
      return None
    else:
      return self._cost_model.get_call_cost(node, arg_costs)

  def get_import_cost(self, source_driver, source_binding):
    return None

  def evaluate(self, node, args):
    expr = None

    # clauses
    if node.func == dc.SCAN:
      col_path = node.attrs["path"][1:]
      if len(col_path) != 1:
        raise ValueError
      expr = MongoPipeline(col_path[0])
            
    elif node.func == dc.SELECT:
      query = args[0].expr
      projection = {}
      for label, arg in zip(node.attrs["labels"], args[1:]):
        projection[label] = arg.expr
      query.add_stage({ "$project": projection })
      expr = query

    elif node.func == dc.FILTER:
      query = args[0].expr
      query.add_stage({ "$match": { "$expr": args[1].expr }})
      expr = query

    elif node.func == dc.LIMIT:
      query = args[0].expr
      query.add_stage({ "$limit": node.attrs["limit"]})
      expr = query

    elif node.func == dc.OFFSET:
      query = args[0].expr
      query.add_stage({ "$skip": node.attrs["offset"]})
      expr = query

    # literals

    elif node.func in [
        dc.INT,
        dc.FLOAT,
        dc.STRING
    ]:
      expr = { "$literal": node.attrs["value"] }

    # context expressions

    elif node.func == dc.READ_CTX:
      expr = "$" + ".".join(node.attrs["path"][1:])

    # bool expressions

    elif node.func == dc.NOT:
      expr = { "$not": args[0].expr }

    elif node.func == dc.AND:
      expr = { "$and": [ arg.expr for arg in args] }

    elif node.func == dc.OR:
      expr = { "$or": [ arg.expr for arg in args] }

    elif node.func == dc.EQ:
      expr = { "$eq": [ arg.expr for arg in args] }

    elif node.func == dc.GT:
      expr = { "$gt": [ arg.expr for arg in args] }

    elif node.func == dc.GE:
      expr = { "$gte": [ arg.expr for arg in args] }

    elif node.func == dc.LT:
      expr = { "$lt": [ arg.expr for arg in args] }

    elif node.func == dc.LE:
      expr = { "$lte": [ arg.expr for arg in args] }

    # num expressions

    elif node.func == dc.ADD:
      expr = { "$add": [arg.expr for arg in args] }

    elif node.func == dc.SUB:
      expr = { "$subtract": [arg.expr for arg in args] }

    elif node.func == dc.MULT:
      expr = { "$multiply": [arg.expr for arg in args] }

    elif node.func == dc.DIV:
      expr = { "$divide": [arg.expr for arg in args] }

    elif node.func == dc.MOD:
      expr = { "$mod": [arg.expr for arg in args] }

    else:
      raise RuntimeError("unknown node: " + repr(node))

    return MongoValue(expr, self), False

  def import_(self, source_driver, value, alias, paths):
    raise NotImplementedError

  def __str__(self):
    return f"Mongo@{self.prefix}"
  
  def __repr__(self):
    return self.__str__()
