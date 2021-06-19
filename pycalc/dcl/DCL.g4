grammar DCL;

/**
 * PARSER
 */
queryRule:
  exprRule EOF;

exprRule:
  compositeSqlQueryRule # SqlExpression
  | booleanExprRule     # BooleanExpression;

booleanExprRule:
  baseExprRule op = (LT | LT_EQ | GT | GT_EQ) baseExprRule                             # HighCompExpression
  | baseExprRule op = (EQ1 | EQ2 | NOT_EQ1 | NOT_EQ2) baseExprRule                     # LowCompExpression
  | K_NOT value = baseExprRule                                                         # NotExpression
  | booleanExprRule K_AND booleanExprRule                                              # AndExpression
  | booleanExprRule K_OR booleanExprRule                                               # OrExpression
  | baseExprRule negate = K_NOT? K_LIKE baseExprRule                                   # StringCompExpression
  | baseExprRule negate = K_NOT? K_BETWEEN baseExprRule K_AND baseExprRule             # BetweenExpression
  | baseExprRule (isNull = K_ISNULL | isNull = K_IS K_NULL | K_NOTNULL | K_NOT K_NULL) # NullCheckExpression
  | baseExprRule K_IS negate = K_NOT? baseExprRule                                     # IsExpression
  | baseExprRule                                                                       # BaseExpression;

baseExprRule:
  MINUS value = baseExprRule                                                            # NegateExpression
  | baseExprRule op = (STAR | DIV | MOD) baseExprRule                                   # HighMathExpression
  | baseExprRule op = (PLUS | MINUS) baseExprRule                                       # LowMathExpression
  | func = IDENT '(' (args += exprRule ( ',' args += exprRule)* | starCount = '*')? ')' # ApplyExpression
  | segments += IDENT ('.' segments += (IDENT | STRING_LITERAL))*                       # PathExpression
  | K_NULL                                                                              # NullLiteral
  | NUMERIC_LITERAL                                                                     # NumericLiteral
  | STRING_LITERAL                                                                      # StringLiteral
  | '(' exprRule ')'                                                                    # ParenExpression;

compositeSqlQueryRule:
  K_WITH commonTableExpressionRule (',' commonTableExpressionRule)* sqlQueryRule # WithQuery
  | sqlQueryRule                                                                 # SimpleQuery;

commonTableExpressionRule:
  alias = IDENT K_AS '(' sqlQueryRule ')';

sqlQueryRule:
  tables += tableExpressionRule (
    compoundOps += compoundOperatorRule tables += tableExpressionRule
  )*;

tableExpressionRule:
  selectClauseRule fromClauseRule whereClauseRule? groupByClauseRule? orderByClauseRule? limitClauseRule?;

selectClauseRule:
  K_SELECT distinct = K_DISTINCT? resultColumnRule (',' resultColumnRule)*;

fromClauseRule:
  K_FROM (tableRule ( ',' tableRule)* | joinClauseRule)                                      # FromTableRule
  | K_FROM system = IDENT K_MATCH patterns += graphPathRule (',' patterns += graphPathRule)* # FromMatchRule;

graphPathRule:
  fromNode = graphNodeRule '-' rel = graphRelationRule? '->' toNode = graphNodeRule;

graphNodeRule:
  '(' name = IDENT? (':' label = IDENT)? ')';

graphRelationRule:
  '[:' relType = IDENT ']';

whereClauseRule:
  K_WHERE where = booleanExprRule;

groupByClauseRule:
  K_GROUP K_BY groupBy += baseExprRule (',' groupBy += baseExprRule)* (
    K_HAVING having = baseExprRule
  )?;

joinClauseRule:
  tableRule (joinOperatorRule tableRule joinConstraintRule?)*;

tableRule:
  table = baseExprRule tableAliasRule?;

tableAliasRule:
  K_AS? tableAlias = IDENT ('(' columnAlias += IDENT ( ',' columnAlias += IDENT)* ')')?;

joinOperatorRule:
  ','
  | K_NATURAL? (K_LEFT K_OUTER? | K_INNER | K_CROSS)? K_JOIN;

joinConstraintRule:
  K_ON baseExprRule                    # JoinOnConstraint
  | K_USING '(' IDENT (',' IDENT)* ')' # JoinUsingConstraint;

resultColumnRule:
  '*'                                            # StarResult
  | booleanExprRule (K_AS? columnAlias = IDENT)? # ExpressionResult;

compoundOperatorRule:
  K_UNION         # Union
  | K_UNION K_ALL # UnionAll
  | K_INTERSECT   # Intersect
  | K_EXCEPT      # Except;

orderByClauseRule:
  K_ORDER K_BY expr += orderingTermRule (',' expr += orderingTermRule)*;

orderingTermRule:
  column = NUMERIC_LITERAL order = (K_ASC | K_DESC)?;

limitClauseRule:
  K_LIMIT limit = NUMERIC_LITERAL (( K_OFFSET | ',') offset = NUMERIC_LITERAL)?;

typeNameRule:
  IDENT+ ('(' signedNumberRule ')' | '(' signedNumberRule ',' signedNumberRule ')')?;

signedNumberRule: ('+' | '-')? NUMERIC_LITERAL;

keywordRule:
  K_ALL
  | K_AND
  | K_AS
  | K_ASC
  | K_BETWEEN
  | K_BY
  | K_CASE
  | K_CAST
  | K_CROSS
  | K_DESC
  | K_DISTINCT
  | K_DROP
  | K_ELSE
  | K_END
  | K_ESCAPE
  | K_EXCEPT
  | K_FROM
  | K_GLOB
  | K_GROUP
  | K_HAVING
  | K_IN
  | K_INNER
  | K_INTERSECT
  | K_IS
  | K_ISNULL
  | K_JOIN
  | K_LEFT
  | K_LIKE
  | K_LIMIT
  | K_MATCH
  | K_NATURAL
  | K_NOT
  | K_NOTNULL
  | K_NULL
  | K_OFFSET
  | K_ON
  | K_OR
  | K_ORDER
  | K_OUTER
  | K_RECURSIVE
  | K_REGEXP
  | K_SELECT
  | K_THEN
  | K_UNION
  | K_UNIQUE
  | K_USING
  | K_VALUES
  | K_WHEN
  | K_WHERE
  | K_WITH
  | K_YEAR
  | K_MONTH
  | K_DAY
  | K_HOUR
  | K_MINUTE
  | K_SECOND;

/**
 * LEXER
 */

SCOL:
  ';';
DOT:
  '.';
OPEN_PAR:
  '(';
CLOSE_PAR:
  ')';
COMMA:
  ',';
ASSIGN:
  ':=';
STAR:
  '*';
PLUS:
  '+';
MINUS:
  '-';
TILDE:
  '~';
PIPE2:
  '||';
DIV:
  '/';
MOD:
  '%';
LT2:
  '<<';
GT2:
  '>>';
AMP:
  '&';
PIPE:
  '|';
LT:
  '<';
LT_EQ:
  '<=';
GT:
  '>';
GT_EQ:
  '>=';
EQ1:
  '=';
EQ2:
  '==';
NOT_EQ1:
  '!=';
NOT_EQ2:
  '<>';

K_ALL:
  A L L;
K_AND:
  A N D;
K_AS:
  A S;
K_ASC:
  A S C;
K_BETWEEN:
  B E T W E E N;
K_BY:
  B Y;
K_CASE:
  C A S E;
K_CAST:
  C A S T;
K_CROSS:
  C R O S S;
K_DESC:
  D E S C;
K_DISTINCT:
  D I S T I N C T;
K_DROP:
  D R O P;
K_ELSE:
  E L S E;
K_END:
  E N D;
K_ESCAPE:
  E S C A P E;
K_EXCEPT:
  E X C E P T;
K_EXTRACT:
  E X T R A C T;
K_FROM:
  F R O M;
K_GLOB:
  G L O B;
K_GROUP:
  G R O U P;
K_HAVING:
  H A V I N G;
K_IN:
  I N;
K_INNER:
  I N N E R;
K_INTERSECT:
  I N T E R S E C T;
K_IS:
  I S;
K_ISNULL:
  I S N U L L;
K_JOIN:
  J O I N;
K_LEFT:
  L E F T;
K_LIKE:
  L I K E;
K_LIMIT:
  L I M I T;
K_MATCH:
  M A T C H;
K_NATURAL:
  N A T U R A L;
K_NOT:
  N O T;
K_NOTNULL:
  N O T N U L L;
K_NULL:
  N U L L;
K_OFFSET:
  O F F S E T;
K_ON:
  O N;
K_OR:
  O R;
K_ORDER:
  O R D E R;
K_OUTER:
  O U T E R;
K_RECURSIVE:
  R E C U R S I V E;
K_REGEXP:
  R E G E X P;
K_ROW:
  R O W;
K_SELECT:
  S E L E C T;
K_THEN:
  T H E N;
K_UNION:
  U N I O N;
K_UNIQUE:
  U N I Q U E;
K_USING:
  U S I N G;
K_VALUE:
  V A L U E;
K_VALUES:
  V A L U E S;
K_WHEN:
  W H E N;
K_WHERE:
  W H E R E;
K_WITH:
  W I T H;

K_YEAR:
  Y E A R;
K_MONTH:
  M O N T H;
K_DAY:
  D A Y;
K_HOUR:
  H O U R;
K_MINUTE:
  M I N U T E;
K_SECOND:
  S E C O N D;

LET_IDENT:
  '@' IDENT;

IDENT:
  [a-zA-Z_] [a-zA-Z_0-9]*;

NUMERIC_LITERAL:
  DIGIT+ ('.' DIGIT*)? (E [-+]? DIGIT+)?
  | '.' DIGIT+ ( E [-+]? DIGIT+)?;

STRING_LITERAL:
  '\'' (~'\'' | '\'\'')* '\'';

SINGLE_LINE_COMMENT:
  '--' ~[\r\n]* -> channel(HIDDEN);

MULTILINE_COMMENT:
  '/*' .*? ('*/' | EOF) -> channel(HIDDEN);

SPACES:
  [ \u000B\t\r\n] -> channel(HIDDEN);

fragment DIGIT:
  [0-9];

fragment A:
  [aA];
fragment B:
  [bB];
fragment C:
  [cC];
fragment D:
  [dD];
fragment E:
  [eE];
fragment F:
  [fF];
fragment G:
  [gG];
fragment H:
  [hH];
fragment I:
  [iI];
fragment J:
  [jJ];
fragment K:
  [kK];
fragment L:
  [lL];
fragment M:
  [mM];
fragment N:
  [nN];
fragment O:
  [oO];
fragment P:
  [pP];
fragment Q:
  [qQ];
fragment R:
  [rR];
fragment S:
  [sS];
fragment T:
  [tT];
fragment U:
  [uU];
fragment V:
  [vV];
fragment W:
  [wW];
fragment X:
  [xX];
fragment Y:
  [yY];
fragment Z:
  [zZ];

ERROR:
  .;