import math
from pycalc import dc, Cost

class DefaultCostModel:
  
  def __init__(self, perf_factor=1.0, import_factor=1000.0):
    self.perf_factor = perf_factor
    self.import_factor = import_factor

  def get_import_cost(self, value_cost):
    return Cost(
      size=value_cost.size,
      total=value_cost.total + value_cost.size * self.import_factor
    )

  def get_call_cost(self, node, args):
    if node.func == dc.SCAN:
      in_cost = 0
      size = 100
      compute = 1

    elif node.func == dc.MATCH:
      in_cost = 0
      size = 100
      compute = 1

    elif node.func == dc.FILTER:
      in_cost = args[0].total
      size = args[0].size * 0.5
      compute = args[1].total

    elif node.func == dc.SELECT:
      in_cost = args[0].total
      size = args[0].size
      compute = args[1].total

    elif node.func == dc.CROSS_JOIN:
      in_cost = args[0].total + args[1].total
      size = args[0].size * args[1].size
      compute = 1

    elif node.func in dc.SQL_JOIN_OPS:
      in_cost = args[0].total + args[1].total
      size = args[0].size * args[1].size * 0.5
      compute = args[2].total

    elif node.func == dc.UNION_ALL:
      in_cost = args[0].total + args[1].total
      size = args[0].size + args[1].size
      compute = 1

    elif node.func == dc.GROUP_BY:
      in_cost = args[0].total
      size = args[0].size * 0.3
      compute = args[1].total

    elif node.func == dc.ORDER_BY:
      in_cost = args[0].total
      size = args[0].size
      compute = args[0].total * math.log(args[0].total)

    elif node.func == dc.LIMIT:
      in_cost = args[0].total
      size = node.attrs['limit']
      compute = 1

    elif node.func == dc.OFFSET:
      in_cost = args[0].total
      size = args[0].size
      compute = 1

    elif node.func == dc.GRAPH_NODE:
      in_cost = 0
      size = 1
      compute = 1
      
    elif node.func == dc.GRAPH_RELATION:
      in_cost = args[0].total + args[1].total
      size = 1
      compute = 1

    elif node.func in dc.BASIC_EXPR:
      in_cost = sum([arg.total for arg in args])
      size = 1
      compute = 1
    
    else:
        return None
    
    return Cost(
      size=size,
      total=in_cost + size * compute * self.perf_factor
    )
