import logging
from os import linesep
from time import time

from pycalc import dc
from pycalc.cost import Cost
from pycalc.scheduler.memo import Memo, Node
from pycalc.scheduler.no_plan_error import NoPlanError
from pycalc.scheduler.rewrites.permutate_args import PermutateArgs
from pycalc.scheduler.rewrites.swap_funcs import SwapFuncs

logger = logging.getLogger("scheduler")

class ReoptException(Exception):
  pass

class Scheduler:
  def __init__(self, rewrites=[], drivers=[]):
    self.rewrites = rewrites
    self.drivers = drivers
    self.memo = None

  def add_rewrite(self, rewrite):
    self.rewrites.append(rewrite)

  def add_driver(self, driver):
    self.drivers.append(driver)

  def schedule(self, memo, dry_run=False):
    if not self.drivers: 
      raise RuntimeError('No driver')

    if self.memo:
      raise RuntimeError('Parallel schedule')

    self.memo = memo
    for rewrite in self.rewrites:
      rewrite.clear()
    
    logger.info("Begin optimization")
    start = time()
    self._optimize()
    self._set_read_paths(set(), self.memo.root_idx)
    logger.info("Optimization ended after %.3f seconds", time() - start)
    
    res = None
    if not dry_run:
      res = self._evaluate()

    self.memo = None
    return res
  
  def _split_paths(self, paths, lhs_defs, rhs_defs):
    lhs_paths = set()
    rhs_paths = set()
    for path in paths:
      if path[0] in lhs_defs:
        lhs_paths.add(path)
      elif path[0] in rhs_defs:
        rhs_paths.add(path)
      else:
        raise RuntimeError
    return lhs_paths, rhs_paths

  def _set_read_paths(self, read_paths, group_idx):
    for node in self.memo.get_group(group_idx):
      node.attrs["read_paths"] = read_paths
      # Functions that set definitions
      if node.func in [dc.SELECT, dc.GROUP_BY]:
        expr_paths = set()
        for arg in node.args[1:]:
          expr_paths |= self.memo.get_group_attr(arg, "paths", set())
        self._set_read_paths(expr_paths, node.args[0])

      # Functions that do not set definitions
      elif node.func in [dc.ORDER_BY, dc.LIMIT, dc.OFFSET]:
        self._set_read_paths(read_paths, node.args[0])
      
      elif node.func == dc.UNION_ALL:
        for arg in node.args:
          self._set_read_paths(read_paths, arg)

      elif node.func == dc.FILTER:
        expr_paths = self.memo.get_group_attr(node.args[1], "paths", set())
        self._set_read_paths(read_paths | expr_paths, node.args[0])

      elif node.func == dc.CROSS_JOIN:
        lhs_defs = self.memo.get_group_attr(node.args[0], "defs", set())
        rhs_defs = self.memo.get_group_attr(node.args[1], "defs", set())
        lhs_paths, rhs_paths = self._split_paths(read_paths, lhs_defs, rhs_defs)
        self._set_read_paths(lhs_paths, node.args[0])
        self._set_read_paths(rhs_paths, node.args[1])

      elif node.func in [dc.INNER_JOIN, dc.LEFT_JOIN, dc.RIGHT_JOIN, dc.FULL_JOIN]:
        lhs_defs = self.memo.get_group_attr(node.args[0], "defs", set())
        rhs_defs = self.memo.get_group_attr(node.args[1], "defs", set())
        lhs_paths, rhs_paths = self._split_paths(read_paths, lhs_defs, rhs_defs)
        lhs_pred_paths = self.memo.get_group_attr(node.args[2], "paths", set())
        rhs_pred_paths = self.memo.get_group_attr(node.args[3], "paths", set())
        self._set_read_paths(lhs_paths | lhs_pred_paths, node.args[0])
        self._set_read_paths(rhs_paths | rhs_pred_paths, node.args[1])

  def _evaluate(self):
    min_driver = self.memo.root.get_min_binding().driver
    try:
      return self._evaluate_group(min_driver, self.memo.root_idx)
    except ReoptException:
      pass
    
    return self._reoptimize()

  def _reoptimize(self):
    logger.info("Begin re-optimization")
    start = time()
    for group in self.memo.groups.values():
      group.bindings.clear()
    self._optimize()
    self._set_read_paths(set(), self.memo.root_idx)
    logger.info("Re-optimization ended after %.3f seconds", time() - start)
    return self._evaluate()

  def _set_intermediate(self, group, driver, cost, value):
    size = cost.size
    if hasattr(value, "real_size") and value.real_size is not None:
      size = value.real_size
    group.set_intermediate(value, driver, Cost(size, 1))

  def _evaluate_group(self, driver, group_idx):
    group = self.memo.get_group(group_idx)
    binding = group.get_binding(driver)
    
    res = None

    # This group has been evaluated before, use the previous result
    if binding.node.func == dc.INTERMEDIATE:
      res = binding.node.attrs['value']
    else:
      eval_driver = binding.source_driver if binding.source_driver else binding.driver

      # evaluate the arguments
      cost_order = sorted(enumerate(binding.node.args), key=lambda idx_arg: self.memo.get_cost(idx_arg[1], eval_driver).total)
      args = [None] * len(binding.node.args)
      for idx, arg in cost_order:
        args[idx] = self._evaluate_group(eval_driver, arg)
      
      # evaluate the node
      res, reopt = eval_driver.evaluate(binding.node, args)
      if reopt:
        self._set_intermediate(group, eval_driver, binding.cost, res)
        logger.debug("%s has triggered re-optimization after %s call.", type(eval_driver).__name__, binding.node.func)
        raise ReoptException
      
    # Import if necessary
    reopt = False
    if binding.source_driver:
      defs = list(group.attrs.get("defs", set()))
      if len(defs) > 1:
        raise RuntimeError
      res, reopt = binding.driver.import_(
        binding.source_driver, 
        res, 
        defs[0] if defs else None,
        binding.node.attrs["read_paths"]
      )
    
    if binding.node.func != dc.INTERMEDIATE:
      self._set_intermediate(group, binding.driver, binding.cost, res)
    
    if reopt:
      logger.debug("%s has triggered re-optimization after import from %s", type(binding.driver).__name__, type(eval_driver).__name__)
      raise ReoptException

    return res
  
  def _optimize(self):
    start = time()
    # Fully expand the memo using logical rewrites
    while self._expand_group(self.memo.root_idx):
      continue
    expanded = time()
    logger.debug("Logical expansion ended after %.3f seconds", expanded - start)

    # Bind the nodes of the memo
    did_bind = self._bind_group(self.memo.root_idx)
    bound = time()

    logger.debug("Binding ended after %.3f seconds", bound - expanded)
    self._log_plan()

    return did_bind

  def _expand_group(self, group_idx):
    """
    Recursively applies rewrites to all nodes of a group
    """

    group = self.memo.get_group(group_idx)
    did_expand = False

    # Apply all rewrites to this group.
    for rewrite in self.rewrites:
      rewrite_did_expand = rewrite(group_idx, self.memo)
      did_expand |= rewrite_did_expand
      
    # Recursively expand the arguments of this group
    for arg_idx in group.get_all_args():
      did_expand |= self._expand_group(arg_idx)

    return did_expand

  def _bind_group(self, group_idx):
    """
    Recursively bind all nodes of a group
    """

    group = self.memo.get_group(group_idx)
    
    # This group has already been bound!
    if group.bindings:
      return False
    
    # Recursively bind the arguments of this group
    for arg_idx in group.get_all_args():
      self._bind_group(arg_idx)

    # The costs of all arguments are determined. Now bind the group itself
    did_bind = False
    for node in group:
      did_bind |= self._bind_node(node, group)

    return did_bind

  def _bind_node(self, node, group):
    """
    Determine execution and import cost of "node" for each driver
    """

    did_bind = False
    # For each driver, find the cheapest call
    if node.func == dc.INTERMEDIATE:
      did_bind = group.bind_call(node, node.attrs["cost"], node.attrs["driver"])
    else:
      for call_driver in self.drivers:
        if self._bind_call(node, group, call_driver):  # "driver" is now bound to "node"
          did_bind = True
    
    # Values with multiple definitions (un-mapped joins) can not be imported
    if not did_bind or len(group.attrs.get("defs", set())) > 1:
      return False

    # For each cheapest call check all imports
    for source_driver in self.drivers:
      if not group.has_binding(source_driver):
        continue

      for import_driver in self.drivers:
        if import_driver is source_driver:
          continue
        
        self._bind_import(group, source_driver, import_driver)
  
    return True

  def _bind_call(self, node, group, driver):
    """
    Determine the execution cost of 'node for a given "driver"
    """

    arg_costs = []
    for arg_idx in node.args:
      arg_cost = self.memo.get_cost(arg_idx, driver)
      if arg_cost is None: # we only accept calls if all arguments have cost for this driver
        return False
      arg_costs.append(arg_cost)
    
    new_cost = driver.get_call_cost(node, arg_costs)
    return group.bind_call(node, new_cost, driver)
    
  def _bind_import(self, group, source_driver, target_driver):
    """
    Determine the cost of transfering "node" from "source_driver" to "target_driver"
    """

    source_binding = group.get_binding(source_driver)
    new_cost = target_driver.get_import_cost(source_driver, source_binding)
    return group.bind_import(new_cost, source_driver, target_driver)

  def _log_plan(self):
    try:
      min_driver = self.memo.root.get_min_binding().driver
      lines = self.memo.plan_to_string(min_driver).splitlines()
      for line in lines:
        logger.debug(line)
      pass
    except RuntimeError:
      lines = self.memo.bindings_to_string().splitlines()
      for line in lines:
        logger.debug(line)
      raise
  