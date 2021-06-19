import logging

from pycalc.scheduler.rewrites.rewrite import Rewrite
from pycalc.scheduler.memo import Node

logger = logging.getLogger(__name__)

class SwapFuncs(Rewrite):
  """
  Swap the order of a binary function composition.

  if not predicate or predicate(f(g(a, b), c)):
    f(g(a, b), c) => g(f(a, c), b)

  Note: additional arguments are copied unchanged
  """

  def __init__(self, outer_func, inner_func, predicate = None):
    super().__init__()
    self._outer_func = outer_func
    self._inner_func = inner_func
    self._predicate = predicate

  def _rewrites(self, group_idx, memo):
    for outer_node in memo.get_group(group_idx):
      self._outer_node = outer_node
      if outer_node.func == self._outer_func:
        for new_inner in self._rewrites_inner(outer_node.args[0], memo):
          logger.debug("swap %s with %s: ")
          yield Node(
            self._inner_node.func,
            self._make_args(new_inner, self._inner_node.args[1:]),
            self._inner_node.attrs
          )
  
  def _rewrites_inner(self, group_idx, memo):
    for inner_node in memo.get_group(group_idx):
      self._inner_node = inner_node
      if (
        inner_node.func == self._inner_func and 
          (
            not self._predicate or
            self._predicate([self._outer_node, self._inner_node], memo)
          )
      ):
        yield memo.append(Node(
          self._outer_node.func, 
          self._make_args(inner_node.args[0], self._outer_node.args[1:]), 
          self._outer_node.attrs
        ))
