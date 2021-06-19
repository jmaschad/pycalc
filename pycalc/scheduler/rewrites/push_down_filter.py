from pycalc.scheduler.rewrites.rewrite import Rewrite
from pycalc import dc
from pycalc.scheduler.memo import Node

class ExtractPredicates:
  def __init__(self, predicate, one_shot=False):
    self._predicate = predicate
    self._one_shot = one_shot

  def __call__(self, group_idx, memo):
    for node in memo.get_group(group_idx):
      if node.func == dc.AND:
        for lhs, lhs_matches in self(node.args[0], memo):
          if self._one_shot and lhs_matches:
            yield self._compose_matches(node, lhs, lhs_matches, node.args[1], [], memo)
            continue

          for rhs, rhs_matches in self(node.args[1], memo):
            if self._one_shot and rhs_matches:
              yield self._compose_matches(node, node.args[0], [], rhs, rhs_matches, memo)
              continue
      
            yield self._compose_matches(node, lhs, lhs_matches, rhs, rhs_matches, memo)
      else:
        if self._predicate(node, group_idx, memo):
          yield (None, [node])
        else:
          yield (group_idx, [])

  def _compose_matches(self, and_node, lhs, lhs_matches, rhs, rhs_matches, memo):
    if lhs is not None and rhs is not None:
      new_node = Node(dc.AND, (lhs, rhs), and_node.attrs)
      return (memo.append(new_node), lhs_matches + rhs_matches)
    elif lhs is not None:
      return (lhs, lhs_matches + rhs_matches)
    elif rhs is not None:
      return (rhs, lhs_matches + rhs_matches)
    else:
      return (None, lhs_matches + rhs_matches)

class IsJoinPred:
  def __init__(self, lhs, rhs):
    self._lhs = lhs
    self._rhs = rhs

  def __call__(self, node, group_idx, memo):
    if node.func != dc.EQ:
      return False

    # Match independent of the order of the sub-expressions
    return (
      (
        memo.covers(self._lhs, node.args[0]) and 
        memo.covers(self._rhs, node.args[1])
      ) or (
        memo.covers(self._lhs, node.args[1]) and 
        memo.covers(self._rhs, node.args[0])
      )
    )

class PushDownFilter(Rewrite):
  
  def _rewrites(self, group_idx, memo):
    for filter_node in memo.get_group(group_idx):
      if filter_node.func == dc.FILTER:
        self._old_filter = filter_node
        for new_join in self._join_rewrites(filter_node.args[0], memo):
          if self._new_predicate:
            yield Node(
              dc.FILTER,
              (memo.append(new_join), self._new_predicate),
              filter_node.attrs
            )
          else:
            yield new_join

  def _join_rewrites(self, group_idx, memo):
    for join_node in memo.get_group(group_idx):
      if join_node.func in dc.SQL_JOIN_OPS:
        old_predicate = self._old_filter.args[1]
        lhs = join_node.args[0]
        rhs = join_node.args[1]

        # push down lhs predicates
        extract_lhs = ExtractPredicates(
          lambda node, group_idx, memo: memo.covers(join_node.args[0], group_idx)
        )
        for new_predicate1, lhs_predicates in extract_lhs(old_predicate, memo):
          self._new_predicate = new_predicate1
          if lhs_predicates:
            lhs_pred = self._compose_preds(lhs_predicates, memo)
            lhs = memo.append(
              Node(dc.FILTER, (lhs, lhs_pred))
            )
          # no predicates left to push, done
          if not new_predicate1:
            yield self._make_join(lhs, rhs, join_node)
            continue

          # push down rhs predicates
          extract_rhs = ExtractPredicates(
            lambda node, group_idx, memo: memo.covers(join_node.args[1], group_idx)
          )
          for new_predicate2, rhs_predicates in extract_rhs(new_predicate1, memo):
            self._new_predicate = new_predicate2
            if rhs_predicates:
              rhs_pred = self._compose_preds(rhs_predicates, memo)
              rhs = memo.append(
                Node(dc.FILTER, (rhs, rhs_pred))
              )
            # push down complete
            if not new_predicate2 or join_node.func != dc.CROSS_JOIN:
              yield self._make_join(lhs, rhs, join_node)
              continue

            # push one predicate into a cross join
            extract_join = ExtractPredicates(
              IsJoinPred(join_node.args[0], join_node.args[1]),
              one_shot=True
            )
            for new_predicate3, join_predicates in extract_join(new_predicate2, memo):
              self._new_predicate = new_predicate3
              if len(join_predicates) > 1:
                raise RuntimeError

              if join_predicates:
                join_pred = join_predicates[0]
                lhs_pred = join_pred.args[0]
                rhs_pred = join_pred.args[1]
                if not memo.covers(lhs, lhs_pred):
                  lhs_pred, rhs_pred = rhs_pred, lhs_pred

                if not (memo.covers(lhs, lhs_pred) and memo.covers(rhs, rhs_pred)):
                  raise RuntimeError

                yield Node(
                  dc.INNER_JOIN,
                  (lhs, rhs, lhs_pred, rhs_pred),
                  join_node.attrs
                )
              else:
                yield self._make_join(lhs, rhs, join_node)
            
  def _make_join(self, lhs, rhs, join_node):
    return Node(
              join_node.func, 
              self._make_args(lhs, rhs, join_node.args[2:]),
              join_node.attrs
            )  
  
  def _compose_preds(self, preds, memo):
    new_pred = memo.append(preds[0])
    for pred in preds[1:]:
      new_pred = memo.append(
        Node(dc.AND, (new_pred, memo.append(pred)))
      )
    return new_pred
