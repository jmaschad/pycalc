import logging

from pycalc import dc
from pycalc.scheduler.memo import Node
from pycalc.scheduler.rewrites.rewrite import Rewrite

logger = logging.getLogger(__name__)

class PullUpUnion(Rewrite):

  def __init__(self):
    super().__init__()
    self._gen_agg = set()

  simple_outer = { dc.SELECT, dc.FILTER } | dc.SQL_JOIN_OPS
  outer = simple_outer | { dc.GROUP_BY, }
  allowed_aggs = { "key", "count", "sum", "min", "max", } 

  def clear(self):
    super().clear()
    self._gen_agg.clear()

  def _rewrites(self, group_idx, memo):
    for outer_node in memo.get_group(group_idx):
      # never rewrite self generated aggregations
      if outer_node.func in self.outer and not outer_node in self._gen_agg:
        for union_node in memo.get_group(outer_node.args[0]):
          if self._first_visit(outer_node, union_node):
            if union_node.func == dc.UNION_ALL:
              new_lhs = memo.append(Node(
                outer_node.func,
                (union_node.args[:1] + outer_node.args[1:]),
                outer_node.attrs
              ))
              new_rhs = memo.append(Node(
                outer_node.func,
                (union_node.args[1:] + outer_node.args[1:]),
                outer_node.attrs
              ))
              new_union = Node(
                union_node.func,
                (new_lhs, new_rhs) + union_node.args[2:],
                union_node.attrs
              )
              if outer_node.func in self.simple_outer:
                yield new_union
              elif outer_node.func == dc.GROUP_BY:
                if all([agg in self.allowed_aggs for agg in outer_node.attrs["aggs"]]):
                  paths = [[label] for label in outer_node.attrs["labels"]]
                  if "definition" in outer_node.attrs:
                    paths = [[outer_node.attrs["definition"], path[0]] for path in paths]
                  exprs = tuple(memo.append(Node(dc.READ_CTX, (), attrs={"path": path})) for path in paths)
                  new_agg = Node(
                    dc.GROUP_BY,
                    (memo.append(new_union), ) + exprs,
                    attrs=outer_node.attrs
                  )
                  self._gen_agg.add(new_agg)
                  yield new_agg
