from pycalc.matcher import PrefixMatcher
from pycalc.scheduler.no_plan_error import NoPlanError

class Driver:
  def __init__(self, prefix):
    self._prefix = prefix
    self._matcher = PrefixMatcher(prefix)

  @property
  def prefix(self):
    return self._prefix

  def get_call_cost(self, node, arg_costs):
    raise NotImplementedError

  def get_import_cost(self, source_driver, source_binding):
    raise NotImplementedError
  
  def evaluate(self, node, args):
    raise NotImplementedError

  def import_(self, source_driver, definition, value):
    raise NotImplementedError

  def _match_prefix(self, node):
    return self._matcher.match(node)

  def __hash__(self):
    return hash(self._prefix)

  def __eq__(self, that):
    return (
      isinstance(that, Driver) and 
      self._prefix == that._prefix
    )

  def __str__(self):
    return type(self).__name__ + '@' + self._prefix

  def __repr__(self):
    return self.__str__()
