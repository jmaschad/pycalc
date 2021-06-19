class CheckObjectsDefined:
  """
  Check if the set of read objects is a subset of the defined objects.

  Use case:
  Predicate for function swap. Called with the outer 
  and inner node of the swap.

  Example:
  Check whether a filter can be swapped with a join.
  - True if all filter objects are define by the first input of the join.
  - __call__ receives the filter node as first argument and the join as second.
  - get_defs returns the definitions of the join's first argument.
  - get_reads returns the reads of the filter's second argument.
  """

  def __init__(self, defs, reads):
    """
      defs: a callable that is called with a list of nodes 
                and that returns a list of group indices.
                The 'defs' of all returned groups define the set of
                defined objects.
      
      reads: a callable that is called with a list of nodes 
                and that returns a list of group indices.
                The 'reads' of all returned groups define the set of
                defined objects.
    """
    self._defs = defs
    self._reads = reads

  def __call__(self, nodes, memo):
    def_groups = self._defs(*nodes)
    read_groups = self._reads(*nodes)
    defs = set()
    for group_idx in def_groups:
      defs |= memo.get_group(group_idx).attrs['defs']
    for group_idx in read_groups:
      reads = memo.get_group(group_idx).attrs['reads']
      if not reads.issubset(defs):
        return False
    return True
