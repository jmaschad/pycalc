import logging
import pyproc

logger = logging.getLogger(__name__)

class PyProcValue:

  def __init__(self, expr, local_scope, driver, is_table=False, real_size=None):
    self.expr = expr
    self.local_scope = local_scope
    self.driver = driver
    self.frame = None
    self.is_table = is_table
    self.real_size = real_size

  def to_pandas(self):
    if self.frame is None:
      logger.debug("Will evaluate expression: %s", self.expr)
      self.frame = eval(self.expr, globals(), self.local_scope)
    return self.frame