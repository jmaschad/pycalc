import logging
from os import path
from time import time

import pandas as pd

logger = logging.getLogger("pyproc_ops")

def as_(value, alias):
  if not isinstance(value, pd.DataFrame):
    raise TypeError

  columns = value.columns
  if columns.nlevels > 2:
    raise RuntimeError

  new_columns = None
  if columns.nlevels > 1:
    logger.debug("Update multi-level index")
    logger.debug("nlevels: %d", columns.nlevels)
    logger.debug("indices: %s", columns.to_list())
    new_columns = columns.set_levels([alias], level=0)
  else:
    tpls = [(alias, col) for col in columns.to_list()]
    new_columns = pd.MultiIndex.from_tuples(tpls)

  logger.debug("as: %s -> %s", columns.to_list(), new_columns.to_list())

  value.columns = new_columns
  return value

def scan(path, columns):
  logger.debug("scan(%s)", path)
  start = time()
  frame = pd.read_parquet(path, columns=columns)
  frame_size = int(frame.memory_usage().sum() / 2**10)
  logger.info("Scan %d KB from %s in %.3f seconds", frame_size, path, time() - start)
  return frame

def select(value, exprs, labels):
  logger.debug("select")
  if not isinstance(value, pd.DataFrame):
    raise TypeError

  frame_def = {}
  for (label, expr) in zip(labels, exprs):
    frame_def[label] = expr(value)

  return pd.DataFrame(frame_def)

def filter(value, fun):
  logger.debug("filter(%s)", value.columns.to_list())
  if not isinstance(value, pd.DataFrame):
    raise TypeError

  return value[fun(value)]

def join(lhs, rhs, how, lhs_keygen, rhs_keygen):
  logger.debug("%s_join(%s, %s)", how, lhs.columns.to_list(), rhs.columns.to_list())
  if not isinstance(lhs, pd.DataFrame) or not isinstance(rhs, pd.DataFrame):
    raise TypeError
  res = lhs.merge(rhs, left_on=lhs_keygen(lhs), right_on=rhs_keygen(rhs), how=how)
  del res["key_0"]
  return res

def union_all(first, second):
  logger.debug("union(%s)", first.columns.to_list())
  if not isinstance(first, pd.DataFrame) or not isinstance(second, pd.DataFrame):
    raise TypeError
  return pd.concat([first, second])

def limit(value, count):
  logger.debug("limit(%s, %d)", value.columns.to_list(), count)
  if not isinstance(value, pd.DataFrame):
    raise TypeError
  return value[:count]

def offset(container, offset):
  raise NotImplementedError

def orderby(value, cols, asc):
  logger.debug("orderby(%s, %s)", value.columns.to_list(), cols)
  if not isinstance(value, pd.DataFrame):
    raise TypeError

  sort_cols = [value.columns[col] for col in cols]
  return value.sort_values(sort_cols, ascending=asc)

def groupby(value, keys, aggs):
  logger.debug("groupby(%s, %s)", value.columns.to_list(), aggs)
  if not isinstance(value, pd.DataFrame):
    raise TypeError
  return value.groupby(by=keys).agg(aggs)

def read_ctx(ctx, path):
  if not path:
    raise RuntimeError
  logger.debug(f"ctx(\"%s\") in %s", path, ctx.columns.to_list())
  value = ctx
  for elem in path:
    value = value[elem]
  return value

def get_year(value):
  if not isinstance(value, pd.Series):
    raise TypeError
  return value.dt.year

def get_month(value):
  if not isinstance(value, pd.Series):
    raise TypeError
  return value.dt.month

def get_day(value):
  if not isinstance(value, pd.Series):
    raise TypeError
  return value.dt.day
