import logging

class Rewrite:
  def __init__(self):
    self._logger = logging.getLogger(type(self).__name__)
    self._visited_set = set()

  def clear(self):
    self._visited_set.clear()

  def _first_visit(self, *nodes):
    if nodes in self._visited_set:
      return False
    else:
      self._visited_set.add(nodes)
      return True

  def __eq__(self, value):
    return self is value

  def __hash__(self):
    return id(self)

  def _make_args(self, *elems):
    args = []
    for elem in elems:
      try:
        args.extend(elem)
      except TypeError:
        args.append(elem)
    return tuple(args)

  def __call__(self, group_idx, memo):
    did_update = False
    for new_outer in self._rewrites(group_idx, memo):
      # allow rewrites to consume a node
      if new_outer is not None:
        if memo.insert(group_idx, new_outer):
          did_update = True
          self._logger.debug("Inserted new node %s into %d", new_outer, group_idx)


    return did_update

  def _rewrites(self, group_idx, memo):
    raise NotImplementedError
