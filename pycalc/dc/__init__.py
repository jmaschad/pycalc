from pycalc.dc.builtins import *
from pycalc.dc.dsl import *
from pycalc.dc.functions import *


CTX_EXPR = set([
  READ_CTX,
])

BOOL_EXPR = set([
  BOOL,
  NOT,
  AND,
  OR,
  EQ,
  NE,
  GT,
  GE,
  LT,
  LE,
])

NUMERIC_EXPR = set([
  INT,
  FLOAT,
  ADD,
  SUB,
  MULT,
  DIV,
  MOD,
  NEG,
])

STRING_EXPR = set([
  STRING,
])

DATE_EXPR = set([
  GET_YEAR,
  GET_MONTH,
  GET_DAY,
])

CAST_EXPR = set([
  TO_BOOL,
  TO_INT,
  TO_DOUBLE,
])

PATH_EXPR = set([
  GRAPH_NODE, 
  GRAPH_RELATION,
])

BASIC_EXPR = CTX_EXPR | BOOL_EXPR | NUMERIC_EXPR | STRING_EXPR | DATE_EXPR | CAST_EXPR

EXPRESSIONS = BASIC_EXPR | PATH_EXPR

SQL_JOIN_OPS = set([
    CROSS_JOIN,
    INNER_JOIN,
    LEFT_JOIN,
    RIGHT_JOIN,
    FULL_JOIN,
])

SQL_TRANS_OPS = set([
    SELECT,
    FILTER,
    LIMIT,
    OFFSET,
    ORDER_BY,
    GROUP_BY,
    UNION_ALL
]) | SQL_JOIN_OPS

SQL_OPS = SQL_TRANS_OPS | set([SCAN])

VALUE_OPS = SQL_OPS | set([MATCH])