# Adding a new function you have to update:
# - function sets in dc.__init__
# - the default_cost_model
# - all drivers that implement the function
# - memo.Group defs and reads inference
# - Scheduler.set_read_paths
# - dsl.fix_definitions

READ_CTX = "READ_CTX"

TO_BOOL = "TO_BOOL"
TO_INT = "TO_INT"
TO_DOUBLE = "TO_DOUBLE"

BOOL = "BOOL"
NOT = "NOT"
AND = "AND"
OR = "OR"
EQ = "EQ"
NE = "NE"
GT = "GT"
GE = "GE"
LT = "LT"
LE = "LE"

INT = "INT"
FLOAT = "FLOAT"
ADD = "ADD"
SUB = "SUB"
MULT = "MULT"
DIV = "DIV"
MOD = "MOD"
NEG = "NEG"

STRING = "STRING"

GET_YEAR = "GET_YEAR"
GET_MONTH = "GET_MONTH"
GET_DAY = "GET_DAY"

GRAPH_NODE = "GRAPH_NODE"
GRAPH_RELATION = "GRAPH_RELATION"

SCAN = "SCAN"
SELECT = "SELECT"
MATCH = "MATCH"
FILTER = "FILTER"
CROSS_JOIN = "CROSS_JOIN"
INNER_JOIN = "INNER_JOIN"
LEFT_JOIN = "LEFT_JOIN"
RIGHT_JOIN = "RIGHT_JOIN"
FULL_JOIN = "FULL_JOIN"
UNION_ALL = "UNION_ALL"
LIMIT = "LIMIT"
OFFSET = "OFFSET"
ORDER_BY = "ORDER_BY"
GROUP_BY = "GROUP_BY"

INTERMEDIATE = "INTERMEDIATE"