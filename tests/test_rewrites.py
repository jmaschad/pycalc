import unittest

from pycalc import dc
from pycalc.scheduler.memo import Memo
from pycalc.scheduler.rewrites.check_objects_defined import CheckObjectsDefined
from pycalc.scheduler.rewrites.push_down_filter import (ExtractPredicates,
                                                         PushDownFilter)
from pycalc.scheduler.rewrites.permutate_args import PermutateArgs
from pycalc.scheduler.rewrites.swap_funcs import SwapFuncs
from pycalc.scheduler.rewrites.pull_up_union import PullUpUnion


class TestPermutateArgs(unittest.TestCase):
  def test_permutate_args(self):
    memo = dc.scan("nation", as_="n").inner_join(
              dc.scan("region", as_="r"),
              dc.ctx("n", "n_regionkey"),
              dc.ctx("r", "r_regionkey")
          ).to_memo()
    
    rewrite = PermutateArgs(dc.INNER_JOIN, [1, 0, 3, 2])
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    old = memo.root.get_node(0)
    new = memo.root.get_node(1)
    self.assertEqual(
      (old.args[0], old.args[1], old.args[2], old.args[3]),
      (new.args[1], new.args[0], new.args[3], new.args[2])
    )

class TestSwapFuncs(unittest.TestCase):
  def test_swap_cross_inner(self):
    memo = dc.scan("nation", as_="n").inner_join(
            dc.scan("region", as_="r"),
            dc.ctx("n", "n_regionkey"),
            dc.ctx("r", "r_regionkey")
        ).cross_join(dc.scan("customer", as_="c")).to_memo()
    
    rewrite = SwapFuncs(dc.CROSS_JOIN, dc.INNER_JOIN)
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    old_outer = memo.root.get_node(0)
    old_inner = memo.get_group(old_outer.args[0]).get_node(0)
    new_outer = memo.root.get_node(1)
    new_inner = memo.get_group(new_outer.args[0]).get_node(0)

    self.assertEqual(new_outer.func, dc.INNER_JOIN)   # func swap
    self.assertEqual(new_inner.func, dc.CROSS_JOIN)   # func swap
    self.assertEqual(new_outer.args[1], old_inner.args[1])  # inner lhs => outer lhs
    self.assertEqual(new_outer.args[2], old_inner.args[2])  # maintain join predicate
    self.assertEqual(new_outer.args[3], old_inner.args[3])  # maintain join predicate
    self.assertEqual(new_inner.args[0], old_inner.args[0])  # inner rhs => inner rhs
    self.assertEqual(new_inner.args[1], old_outer.args[1])  # outer rhs => inner rhs

  def test_swap_inner_inner(self):
    memo = dc.scan("nation", as_="n").inner_join(
            dc.scan("region", as_="r"),
            dc.ctx("n", "n_regionkey"),
            dc.ctx("r", "r_regionkey")
          ).inner_join(
            dc.scan("customer", as_="c"),
            dc.ctx("c", "c_nationkey"),
            dc.ctx("n", "n_nationkey")
          ).to_memo()
          
    pred = CheckObjectsDefined(
      defs=lambda *nodes: [nodes[0].args[1], nodes[1].args[0]],
      reads=lambda *nodes: [nodes[0].args[2]]
    )
    rewrite = SwapFuncs(dc.INNER_JOIN, dc.INNER_JOIN, pred)
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    old_outer = memo.root.get_node(0)
    old_inner = memo.get_group(old_outer.args[0]).get_node(0)
    new_outer = memo.root.get_node(1)
    new_inner = memo.get_group(new_outer.args[0]).get_node(0)

    self.assertEqual(new_outer.func, dc.INNER_JOIN)   # func swap
    self.assertEqual(new_inner.func, dc.INNER_JOIN)   # func swap
    self.assertEqual(new_outer.args[2], old_inner.args[2])  # maintain join predicate
    self.assertEqual(new_outer.args[3], old_inner.args[3])  # maintain join predicate
    self.assertEqual(new_inner.args[2], old_outer.args[2])  # maintain join predicate
    self.assertEqual(new_inner.args[3], old_outer.args[3])  # maintain join predicate
    self.assertEqual(new_outer.args[1], old_inner.args[1])  # inner lhs => outer lhs
    self.assertEqual(new_inner.args[0], old_inner.args[0])  # inner rhs => inner rhs
    self.assertEqual(new_inner.args[1], old_outer.args[1])  # outer rhs => inner rhs

  def test_swap_filter_inner(self):
    memo = dc.scan("customer", as_="c").inner_join(
            dc.scan("nation", as_="n"),
            dc.ctx("c", "c_nationkey"),
            dc.ctx("n", "n_nationkey")
          ).filter(
            dc.ctx("c", "c_balance") <= dc.float(1000.0)
          ).to_memo()
          
    pred = CheckObjectsDefined(
      defs=lambda *nodes: [nodes[1].args[0]],
      reads=lambda *nodes: [nodes[0].args[1]]
    )
    rewrite = SwapFuncs(dc.FILTER, dc.INNER_JOIN, pred)
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    old_outer = memo.root.get_node(0)
    old_inner = memo.get_group(old_outer.args[0]).get_node(0)
    new_outer = memo.root.get_node(1)
    new_inner = memo.get_group(new_outer.args[0]).get_node(0)

    self.assertEqual(new_outer.func, dc.INNER_JOIN)   # func swap
    self.assertEqual(new_outer.args[1], old_inner.args[1])  # inner lhs => outer lhs
    self.assertEqual(new_outer.args[2], old_inner.args[2])  # maintain join predicate
    self.assertEqual(new_outer.args[3], old_inner.args[3])  # maintain join predicate
    
    self.assertEqual(new_inner.func, dc.FILTER)       # func swap
    self.assertEqual(new_inner.args[0], old_inner.args[0])  # inner lhs => filter in
    self.assertEqual(new_inner.args[1], old_outer.args[1])  # maintain filter predicate

class TestExtractPredicates(unittest.TestCase):
  def test_extract_some(self):
    memo = dc.and_(
      dc.ctx("f", "order_id") == dc.ctx("o", "id"),
      dc.ctx("o", "gross") > dc.float(10000.0),
      dc.ctx("o", "tax") != dc.float(8.0),
      dc.ctx("o", "discount") < dc.float(2.0),
      dc.ctx("f", "date_id") == dc.ctx("d", "id"),
      dc.ctx("d", "year") == dc.int(2020),
      dc.ctx("d", "month") == dc.int(1),
    ).to_memo()

    rewrite = ExtractPredicates(lambda node, g, m: node.func == dc.EQ)
    results = list(rewrite(memo.root_idx, memo))
    self.assertEqual(len(results), 1)

    new_0_group, matches = results[0]
    new_0 = memo.get_group(new_0_group).get_node(0)
    self.assertEqual(len(matches), 4)
    self.assertEqual(new_0.func, dc.AND)
    
    new_0_1 = memo.get_group(new_0.args[1]).get_node(0)
    self.assertEqual(new_0_1.func, dc.LT)

    new_1 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_1.func, dc.AND)

    new_1_0 = memo.get_group(new_1.args[0]).get_node(0)
    self.assertEqual(new_1_0.func, dc.GT)

    new_1_1 = memo.get_group(new_1.args[1]).get_node(0)
    self.assertEqual(new_1_1.func, dc.NE)

  def test_extract_all(self):
    memo = dc.and_(
      dc.ctx("f", "order_id") == dc.ctx("o", "id"),
      dc.ctx("f", "date_id") == dc.ctx("d", "id"),
      dc.ctx("d", "year") == dc.int(2020),
      dc.ctx("d", "month") == dc.int(1),
    ).to_memo()

    rewrite = ExtractPredicates(lambda node, g, m: node.func == dc.EQ)
    results = list(rewrite(memo.root_idx, memo))
    self.assertEqual(len(results), 1)

    new_0_group, matches = results[0]
    self.assertIsNone(new_0_group)
    self.assertEqual(len(matches), 4)

  def test_extract_one_shot(self):
    memo = dc.and_(
      dc.ctx("f", "order_id") > dc.ctx("o", "id"),
      dc.ctx("o", "gross") >= dc.float(10000.0),
      dc.and_(
        dc.ctx("o", "tax") == dc.float(8.0),
        dc.ctx("o", "discount") == dc.int(2)
      ),
      dc.ctx("f", "date_id") <= dc.ctx("d", "id"),
      dc.ctx("d", "month") == dc.int(1),
    ).to_memo()

    rewrite = ExtractPredicates(
      lambda node, g, m: node.func == dc.EQ,
      one_shot=True
    )
    results = list(rewrite(memo.root_idx, memo))
    self.assertEqual(len(results), 1)

    _, matches = results[0]
    self.assertEqual(len(matches), 1)
    match_node = matches[0]
    self.assertEqual(match_node.func, dc.EQ)
    match_node_1 = memo.get_group(match_node.args[1]).get_node(0)
    self.assertEqual(match_node_1.func, dc.FLOAT)

class TestPushDownFilter(unittest.TestCase):
  
  def test_no_push_filter(self):
    memo = dc.scan("person", as_="p").filter(
      dc.and_(
        dc.ctx("p", "age") > dc.int(21),
        dc.ctx("p", "height") > dc.int(170)
      )
    ).inner_join(
      dc.scan("nation", as_="n").filter(
        dc.ctx("n", "population") > dc.int(40_000_000)
      ),
      dc.ctx("p", "nation"),
      dc.ctx("n", "id")
    ).filter(
      dc.ctx("p", "income") > dc.ctx("n", "mean_income")
    ).to_memo()

    rewrite = PushDownFilter()
    self.assertFalse(rewrite(memo.root_idx, memo))

  
  def test_push_filter_1(self):
    memo = dc.scan("customer", as_="c").cross_join(
            dc.scan("nation", as_="n"),
          ).filter(
            dc.ctx("c", "balance") <= dc.float(1000.0)
          ).to_memo()
    rewrite = PushDownFilter()
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.CROSS_JOIN)
    
    new_1 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_1.func, dc.FILTER)

  
  def test_push_filter_2(self):
    memo = dc.scan("nation", as_="n").cross_join(
            dc.scan("customer", as_="c"),
          ).filter(
            dc.ctx("c", "balance") <= dc.float(1000.0)
          ).to_memo()
    rewrite = PushDownFilter()
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.CROSS_JOIN)
    
    new_1 = memo.get_group(new_0.args[1]).get_node(0)
    self.assertEqual(new_1.func, dc.FILTER)
  
  def test_push_filter_3(self):
    memo = dc.scan("customer", as_="c").cross_join(
            dc.scan("nation", as_="n")
          ).filter(
            dc.ctx("n", "id") == dc.ctx("c", "nation")
          ).to_memo()
    rewrite = PushDownFilter()
    self.assertTrue(rewrite(memo.root_idx, memo))
    
    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.INNER_JOIN)
    
    new_0_0 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_0_0.func, dc.SCAN)
    self.assertEqual(new_0_0.attrs["path"], ("customer", ))
    
    new_0_1 = memo.get_group(new_0.args[1]).get_node(0)
    self.assertEqual(new_0_1.func, dc.SCAN)
    self.assertEqual(new_0_1.attrs["path"], ("nation", ))

    new_0_2 = memo.get_group(new_0.args[2]).get_node(0)
    self.assertEqual(new_0_2.func, dc.READ_CTX)
    self.assertEqual(new_0_2.attrs["path"], ("c", "nation"))

    new_0_3 = memo.get_group(new_0.args[3]).get_node(0)
    self.assertEqual(new_0_3.func, dc.READ_CTX)
    self.assertEqual(new_0_3.attrs["path"], ("n", "id"))

  def test_push_filter_4(self):
    memo = dc.scan("person", as_="p").cross_join(
            dc.scan("nation", as_="n"),
          ).filter(
            dc.and_(
              dc.ctx("p", "nation") == dc.ctx("n", "id"),
              dc.ctx("p", "income") > dc.float(2.0) * dc.ctx("n", "median_income"),
              dc.ctx("p", "height") < dc.ctx("n", "median_height"),
              dc.ctx("p", "age") > dc.int(21),
              dc.ctx("p", "sex") == dc.string("m"),
              dc.ctx("p", "postcode") == dc.int(12345),
              dc.ctx("n", "population") > dc.int(100000000),
            )
          ).to_memo()
    rewrite = PushDownFilter()
    self.assertTrue(rewrite(memo.root_idx, memo))

    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.FILTER)
    
    new_1 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_1.func, dc.INNER_JOIN)

    new_2_1 = memo.get_group(new_1.args[0]).get_node(0)
    self.assertEqual(new_2_1.func, dc.FILTER)

    new_2_2 = memo.get_group(new_1.args[1]).get_node(0)
    self.assertEqual(new_2_2.func, dc.FILTER)

    new_3 = memo.get_group(new_2_1.args[0]).get_node(0)
    self.assertEqual(new_3.func, dc.SCAN)

    new_4 = memo.get_group(new_2_2.args[0]).get_node(0)
    self.assertEqual(new_4.func, dc.SCAN)

class TestPullUpUnion(unittest.TestCase):

  def test_pull_accross_select(self):
    memo = dc.scan("r", as_="t").union_all(
        dc.scan("s", as_="t")
      ).select({
        "a": dc.ctx("t", "att1"),
        "b": dc.ctx("t", "att2")
      }).to_memo()
    rewrite = PullUpUnion()
    self.assertTrue(rewrite(memo.root_idx, memo))

    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.UNION_ALL)
    
    new_1 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_1.func, dc.SELECT)
    
    new_2 = memo.get_group(new_0.args[1]).get_node(0)
    self.assertEqual(new_2.func, dc.SELECT)

  def test_pull_accross_join(self):
    memo = dc.scan("r", as_="t").union_all(
        dc.scan("s", as_="t")
      ).inner_join(
        dc.scan("u"),
        dc.ctx("t", "a1"),
        dc.ctx("u", "a2")
      ).to_memo()
    rewrite = PullUpUnion()
    self.assertTrue(rewrite(memo.root_idx, memo))

    new_0 = memo.root.get_node(1)
    self.assertEqual(new_0.func, dc.UNION_ALL)
    
    new_1 = memo.get_group(new_0.args[0]).get_node(0)
    self.assertEqual(new_1.func, dc.INNER_JOIN)
    
    new_2 = memo.get_group(new_0.args[1]).get_node(0)
    self.assertEqual(new_2.func, dc.INNER_JOIN)

  def test_pre_aggregate(self):
    memo = dc.scan("r", as_="t").union_all(
        dc.scan("s", as_="t")
      ).group_by({
        "p1": dc.key(dc.ctx("t", "p1")),
        "sp2": dc.sum(dc.ctx("t", "p2")),
        "sp3": dc.count(dc.ctx("t", "p3")),
      }, as_="g").to_memo()
    rewrite = PullUpUnion()
    self.assertTrue(rewrite(memo.root_idx, memo))
