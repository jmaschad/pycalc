from pycalc.dc.dsl import Agg

def key(builder):
  return Agg(builder, 'key')

def count(builder):
  return Agg(builder, 'count')

def sum(builder):
  return Agg(builder, 'sum')

def min(builder):
  return Agg(builder, 'min')

def max(builder):
  return Agg(builder, 'max')