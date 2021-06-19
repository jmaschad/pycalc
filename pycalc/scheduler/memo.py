import logging
from pycalc import dc
from pycalc.cost import Cost
from pycalc.scheduler.no_plan_error import NoPlanError

logger = logging.getLogger("memo")

class Memo:
  def __init__(self):
    self._idx_map = {}
    self.groups = {}
    self.root_idx = None

  @property
  def root(self):
    return self.get_group(self.root_idx)

  def append(self, node):
    if not isinstance(node, Node):
      raise RuntimeError
    if node in self._idx_map:
      return self._idx_map[node]
    else:
      group_idx = len(self.groups)
      logger.debug("Append node to new group %d", group_idx)
      group = Group(node, self)
      self.groups[group_idx] = group
      self._idx_map[node] = group_idx
      return group_idx

  def insert(self, group_idx, node):
    if not isinstance(node, Node):
      raise RuntimeError
    if node not in self._idx_map:
      logger.debug("Insert node into group %d", group_idx)
      self._idx_map[node] = group_idx
      self.groups[group_idx].append(node)
      return True
    else:
      return False

  def get_group(self, group_idx):
    if isinstance(group_idx, int):
      return self.groups[group_idx]
    elif isinstance(group_idx, Node):
      return self.groups[self._idx_map[group_idx]]
    else:
      raise RuntimeError

  def covers(self, defs_idx, reads_idx):
    defs = self.get_group_attr(defs_idx, 'defs', set())
    reads = self.get_group_attr(reads_idx, 'reads', set())
    return reads.issubset(defs)

  def get_group_attr(self, group_idx, attr, default=None):
    return self.get_group(group_idx).attrs.get(attr, default)

  def set_group_attr(self, group_idx, attr, value):
    self.get_group(group_idx).attrs[attr] = value
  
  def get_binding(self, group_idx, driver):
    return self.get_group(group_idx).get_binding(driver)
  
  def get_cost(self, group_idx, driver):
    return self.get_group(group_idx).get_cost(driver)
  
  def bindings_to_string(self):
    strs = ['Root group: ' + str(self.root_idx)]
    visited = set()
    strs += self._group_bindings_to_string(self.root_idx, visited)
    return '\n'.join(strs)

  def _group_bindings_to_string(self, group_idx, visited):
    if group_idx in visited:
      return []

    visited.add(group_idx)
    group = self.get_group(group_idx)
    strs = [str(group_idx) + ": " + group.bindings_to_string()]
    
    for arg_idx in group.get_all_args():
      strs += self._group_bindings_to_string(arg_idx, visited)
    
    return strs

  def plan_to_string(self, driver):
    return self._plan_to_string(self.root_idx, driver)

  def _plan_to_string(self, group_idx, driver, indent=2):
      prefix = ' ' * indent

      def prefix_lines(lines, prefix):
          prefixed = []
          for idx, line in enumerate(lines):
              if idx == 0:
                  prefixed.append("' " + prefix + '> ' + line)
              else:
                  prefixed.append("' " + prefix + '  ' + line)
          return prefixed

      binding = self.get_binding(group_idx, driver)
      head = str(binding)
      if binding.source_driver:
        driver = binding.source_driver
      
      node = binding.node
      head += '('
      if not node.args:
          return head + ')'
      else:
          lines = [head]
          for arg_idx in node.args:
              arg_lines = self._plan_to_string(arg_idx, driver).splitlines()
              lines += prefix_lines(arg_lines, prefix)
          lines.append(')')
          return '\n'.join(lines)

  def to_string(self, show_attrs=False):
    lines = ['\n', 'Root Idx: ' + str(self.root_idx)]
    for group_idx, group in self.groups.items():
      lines.append(str(group_idx) + ': ' + group.to_string(show_attrs=show_attrs))
    return '\n'.join(lines)

  def __str__(self):
    return self.to_string()

class Binding:
  def __init__(self, node, cost, driver, source_driver):
    self.node = node
    self.cost = cost
    self.driver = driver
    self.source_driver = source_driver
  
  def to_string(self, show_args=False):
    rep = self.node.to_string(show_attrs=False) if show_args else self.node.func
    rep += '@'
    if self.source_driver:
      rep += self.source_driver.prefix + '~>' + self.driver.prefix
    else:
      rep += self.driver.prefix
    rep += ';cost={}'.format(self.cost)
    return rep

  def __str__(self):
    return self.to_string()

class Group:

  def _infer_defs(self, node, memo):
    defs = set()
    if "definition" in node.attrs:
      defs.add(node.attrs["definition"])
    else:
      for arg_idx in node.args:
        defs |= memo.get_group_attr(arg_idx, "defs", set())
    return defs

  def _infer_reads_and_paths(self, node, memo):
    reads = set()
    paths = set()
    if node.func == dc.READ_CTX:
      path = node.attrs["path"]
      reads.add(path[0])
      paths.add(tuple(path))
    elif node.func in dc.EXPRESSIONS:
      for arg_idx in node.args:
        reads |= memo.get_group_attr(arg_idx, "reads", set())
        paths |= memo.get_group_attr(arg_idx, "paths", set())
    return reads, paths

  def __init__(self, node, memo):
    self._nodes = [node]
    self._bindings = {}
    self._attrs = {}

    defs = self._infer_defs(node, memo)
    if defs:
      self._attrs["defs"] = defs

    reads, paths = self._infer_reads_and_paths(node, memo)
    if reads:
      self._attrs["reads"] = reads
    if paths:
      self._attrs["paths"] = paths

  @property
  def nodes(self):
    return self._nodes

  @property
  def attrs(self):
    return self._attrs

  @property
  def bindings(self):
    return self._bindings

  def get_node(self, node_idx):
    return self._nodes[node_idx]

  def get_all_args(self):
    arg_groups = set()
    for node in self:
      arg_groups |= set(node.args)
    return arg_groups

  def get_min_binding(self):
    if not self.bindings:
      raise RuntimeError('No binding')
    
    min_binding = sorted(
      self.bindings.values(), 
      key=lambda binding: binding.cost.total
    )[0]
    return min_binding

  def set_intermediate(self, value, driver, cost):
    new_node = Node(dc.INTERMEDIATE, (), attrs={ "value": value, "driver": driver, "cost": cost })
    self._nodes.append(new_node)

  def append(self, node):
    self._is_initial = False
    self._nodes.append(node)

  def _bind(self, node, new_cost, driver, source_driver):
    if new_cost is None:
      return False

    old_cost = self.get_cost(driver)
    if old_cost is None or new_cost.total < old_cost.total :
      self._is_initial = False
      self._bindings[driver] = Binding(node, new_cost, driver, source_driver)
      return True
    else:
      return False

  def bind_call(self, node, cost, driver):
    return self._bind(node, cost, driver, None)
    
  def bind_import(self, target_import_cost, source_driver, target_driver):
    source_binding = self.get_binding(source_driver)
    node = source_binding.node
    return self._bind(node, target_import_cost, target_driver, source_driver)

  def get_cost(self, driver):
    binding = self.get_binding(driver)
    if binding is None:
      return None
    else:
      return binding.cost
    
  def has_binding(self, driver):
    return driver in self._bindings

  def get_binding(self, driver):
    return self._bindings.get(driver)

  def bindings_to_string(self):
    if not self.bindings:
      return self.to_string() + ' - Unbound Group'
    strs = [binding.to_string(show_args=True) for binding in self.bindings.values()]
    return '[' + ', '.join(strs) + ']'

  def to_string(self, show_attrs=False):
    rep = ', '.join([str(node) for node in self.nodes])
    if show_attrs and self._attrs:
      rep += ' -GRP ATTS-> ' + str(self._attrs)
    return rep

  def __iter__(self):
    return iter(self.nodes)

  def __len__(self):
    return len(self.nodes)
  
  def __str__(self):
    return self.to_string(show_attrs=True)

class Node:
  def __init__(self, func, args, attrs={}):
    if not isinstance(args, tuple):
      raise TypeError

    self._func = func
    self._args = args
    self._attrs = attrs
    self._rewrites = set()
  
  @property
  def func(self):
    return self._func
  
  @property
  def args(self):
    return self._args
  
  @property
  def attrs(self):
    return self._attrs

  def to_string(self, show_attrs=True):
    repr = self._func
    if show_attrs and self.attrs:
      repr += str(self.attrs)
    repr += str(self._args)

    return repr

  def __str__(self):
    return self.to_string()

  def __repr__(self):
    return self.__str__()

  def __hash__(self):
    if self.attrs:
      return hash((self._func, id(self.attrs), self._args))
    else:
      return hash((self._func, self._args))
  
  def __eq__(self, that):
    if self.attrs:
      return (self.func == that.func and
              self.attrs is that.attrs and
              self.args == that.args)
    else:
      return self.func == that.func and self.args == that.args
