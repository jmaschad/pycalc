from pycalc import dc
from pycalc.scheduler.memo import Node
from pycalc.scheduler.rewrites.push_down_filter import PushDownFilter
from pycalc.scheduler.rewrites.pull_up_union import PullUpUnion
from pycalc.scheduler.rewrites.permutate_args import PermutateArgs
from pycalc.scheduler.rewrites.swap_funcs import SwapFuncs
from pycalc.scheduler.rewrites.check_objects_defined import CheckObjectsDefined


def default_rewrites():
  joins = [
    dc.CROSS_JOIN,
    dc.INNER_JOIN,
    dc.LEFT_JOIN,
    dc.RIGHT_JOIN,
    dc.FULL_JOIN,
  ]
  
  predicated_joins = [
    dc.INNER_JOIN,
    dc.LEFT_JOIN,
    dc.RIGHT_JOIN,
    dc.FULL_JOIN,
  ]

  rewrites = [
    PushDownFilter(),
    PullUpUnion(),
    PermutateArgs(dc.UNION_ALL, [1, 0]),
    PermutateArgs(dc.CROSS_JOIN, [1, 0]),
  ]

  filter_pred = CheckObjectsDefined(
      defs=lambda *nodes: [nodes[1].args[0]],
      reads=lambda *nodes: [nodes[0].args[1]]
    )
  for join in joins:
    rewrites.append(SwapFuncs(dc.CROSS_JOIN, join))
    rewrites.append(SwapFuncs(dc.FILTER, join, filter_pred))

  join_pred = CheckObjectsDefined(
      defs=lambda *nodes: [nodes[0].args[1], nodes[1].args[0]],
      reads=lambda *nodes: [nodes[0].args[2]]
    )
  for outer_join in predicated_joins:
    rewrites.append(PermutateArgs(outer_join, [1, 0, 3, 2]))
    for inner_join in predicated_joins:
      rewrites.append(SwapFuncs(outer_join, inner_join, join_pred))
  
  return rewrites
