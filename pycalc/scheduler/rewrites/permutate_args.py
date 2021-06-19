from pycalc.scheduler.rewrites.rewrite import Rewrite
from pycalc.scheduler.memo import Node

class PermutateArgs(Rewrite):
  """
  Permutate the arguments of a function according to a permutation vector.

  f(a1, a2, a3), [3, 1, 2]=> f(a3, a1, a2)

  Note: additional arguments are copied unchanged
  """

  def __init__(self, func, permutation):
    super().__init__()
    self._func = func
    self._permutation = permutation
          
  def _rewrites(self, group_idx, memo):
    for node in memo.get_group(group_idx):
      if node.func == self._func:
        if len(node.args) != len(self._permutation):
          raise ValueError

        new_args = tuple(node.args[i] for i in self._permutation)
        yield Node(node.func, new_args, node.attrs)
