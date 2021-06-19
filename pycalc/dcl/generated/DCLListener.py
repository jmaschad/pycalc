from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DCLParser import DCLParser
else:
    from DCLParser import DCLParser

# This class defines a complete listener for a parse tree produced by DCLParser.
class DCLListener(ParseTreeListener):

    # Enter a parse tree produced by DCLParser#queryRule.
    def enterQueryRule(self, ctx:DCLParser.QueryRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#queryRule.
    def exitQueryRule(self, ctx:DCLParser.QueryRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#SqlExpression.
    def enterSqlExpression(self, ctx:DCLParser.SqlExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#SqlExpression.
    def exitSqlExpression(self, ctx:DCLParser.SqlExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#BooleanExpression.
    def enterBooleanExpression(self, ctx:DCLParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#BooleanExpression.
    def exitBooleanExpression(self, ctx:DCLParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#NullCheckExpression.
    def enterNullCheckExpression(self, ctx:DCLParser.NullCheckExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#NullCheckExpression.
    def exitNullCheckExpression(self, ctx:DCLParser.NullCheckExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#BaseExpression.
    def enterBaseExpression(self, ctx:DCLParser.BaseExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#BaseExpression.
    def exitBaseExpression(self, ctx:DCLParser.BaseExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#IsExpression.
    def enterIsExpression(self, ctx:DCLParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#IsExpression.
    def exitIsExpression(self, ctx:DCLParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#AndExpression.
    def enterAndExpression(self, ctx:DCLParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#AndExpression.
    def exitAndExpression(self, ctx:DCLParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#BetweenExpression.
    def enterBetweenExpression(self, ctx:DCLParser.BetweenExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#BetweenExpression.
    def exitBetweenExpression(self, ctx:DCLParser.BetweenExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#StringCompExpression.
    def enterStringCompExpression(self, ctx:DCLParser.StringCompExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#StringCompExpression.
    def exitStringCompExpression(self, ctx:DCLParser.StringCompExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#HighCompExpression.
    def enterHighCompExpression(self, ctx:DCLParser.HighCompExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#HighCompExpression.
    def exitHighCompExpression(self, ctx:DCLParser.HighCompExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#NotExpression.
    def enterNotExpression(self, ctx:DCLParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#NotExpression.
    def exitNotExpression(self, ctx:DCLParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#OrExpression.
    def enterOrExpression(self, ctx:DCLParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#OrExpression.
    def exitOrExpression(self, ctx:DCLParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#LowCompExpression.
    def enterLowCompExpression(self, ctx:DCLParser.LowCompExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#LowCompExpression.
    def exitLowCompExpression(self, ctx:DCLParser.LowCompExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#NegateExpression.
    def enterNegateExpression(self, ctx:DCLParser.NegateExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#NegateExpression.
    def exitNegateExpression(self, ctx:DCLParser.NegateExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#PathExpression.
    def enterPathExpression(self, ctx:DCLParser.PathExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#PathExpression.
    def exitPathExpression(self, ctx:DCLParser.PathExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#NumericLiteral.
    def enterNumericLiteral(self, ctx:DCLParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by DCLParser#NumericLiteral.
    def exitNumericLiteral(self, ctx:DCLParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by DCLParser#StringLiteral.
    def enterStringLiteral(self, ctx:DCLParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by DCLParser#StringLiteral.
    def exitStringLiteral(self, ctx:DCLParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by DCLParser#HighMathExpression.
    def enterHighMathExpression(self, ctx:DCLParser.HighMathExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#HighMathExpression.
    def exitHighMathExpression(self, ctx:DCLParser.HighMathExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#ParenExpression.
    def enterParenExpression(self, ctx:DCLParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#ParenExpression.
    def exitParenExpression(self, ctx:DCLParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#NullLiteral.
    def enterNullLiteral(self, ctx:DCLParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by DCLParser#NullLiteral.
    def exitNullLiteral(self, ctx:DCLParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by DCLParser#ApplyExpression.
    def enterApplyExpression(self, ctx:DCLParser.ApplyExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#ApplyExpression.
    def exitApplyExpression(self, ctx:DCLParser.ApplyExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#LowMathExpression.
    def enterLowMathExpression(self, ctx:DCLParser.LowMathExpressionContext):
        pass

    # Exit a parse tree produced by DCLParser#LowMathExpression.
    def exitLowMathExpression(self, ctx:DCLParser.LowMathExpressionContext):
        pass


    # Enter a parse tree produced by DCLParser#WithQuery.
    def enterWithQuery(self, ctx:DCLParser.WithQueryContext):
        pass

    # Exit a parse tree produced by DCLParser#WithQuery.
    def exitWithQuery(self, ctx:DCLParser.WithQueryContext):
        pass


    # Enter a parse tree produced by DCLParser#SimpleQuery.
    def enterSimpleQuery(self, ctx:DCLParser.SimpleQueryContext):
        pass

    # Exit a parse tree produced by DCLParser#SimpleQuery.
    def exitSimpleQuery(self, ctx:DCLParser.SimpleQueryContext):
        pass


    # Enter a parse tree produced by DCLParser#commonTableExpressionRule.
    def enterCommonTableExpressionRule(self, ctx:DCLParser.CommonTableExpressionRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#commonTableExpressionRule.
    def exitCommonTableExpressionRule(self, ctx:DCLParser.CommonTableExpressionRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#sqlQueryRule.
    def enterSqlQueryRule(self, ctx:DCLParser.SqlQueryRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#sqlQueryRule.
    def exitSqlQueryRule(self, ctx:DCLParser.SqlQueryRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#tableExpressionRule.
    def enterTableExpressionRule(self, ctx:DCLParser.TableExpressionRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#tableExpressionRule.
    def exitTableExpressionRule(self, ctx:DCLParser.TableExpressionRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#selectClauseRule.
    def enterSelectClauseRule(self, ctx:DCLParser.SelectClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#selectClauseRule.
    def exitSelectClauseRule(self, ctx:DCLParser.SelectClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#FromTableRule.
    def enterFromTableRule(self, ctx:DCLParser.FromTableRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#FromTableRule.
    def exitFromTableRule(self, ctx:DCLParser.FromTableRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#FromMatchRule.
    def enterFromMatchRule(self, ctx:DCLParser.FromMatchRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#FromMatchRule.
    def exitFromMatchRule(self, ctx:DCLParser.FromMatchRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#graphPathRule.
    def enterGraphPathRule(self, ctx:DCLParser.GraphPathRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#graphPathRule.
    def exitGraphPathRule(self, ctx:DCLParser.GraphPathRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#graphNodeRule.
    def enterGraphNodeRule(self, ctx:DCLParser.GraphNodeRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#graphNodeRule.
    def exitGraphNodeRule(self, ctx:DCLParser.GraphNodeRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#graphRelationRule.
    def enterGraphRelationRule(self, ctx:DCLParser.GraphRelationRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#graphRelationRule.
    def exitGraphRelationRule(self, ctx:DCLParser.GraphRelationRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#whereClauseRule.
    def enterWhereClauseRule(self, ctx:DCLParser.WhereClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#whereClauseRule.
    def exitWhereClauseRule(self, ctx:DCLParser.WhereClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#groupByClauseRule.
    def enterGroupByClauseRule(self, ctx:DCLParser.GroupByClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#groupByClauseRule.
    def exitGroupByClauseRule(self, ctx:DCLParser.GroupByClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#joinClauseRule.
    def enterJoinClauseRule(self, ctx:DCLParser.JoinClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#joinClauseRule.
    def exitJoinClauseRule(self, ctx:DCLParser.JoinClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#tableRule.
    def enterTableRule(self, ctx:DCLParser.TableRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#tableRule.
    def exitTableRule(self, ctx:DCLParser.TableRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#tableAliasRule.
    def enterTableAliasRule(self, ctx:DCLParser.TableAliasRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#tableAliasRule.
    def exitTableAliasRule(self, ctx:DCLParser.TableAliasRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#joinOperatorRule.
    def enterJoinOperatorRule(self, ctx:DCLParser.JoinOperatorRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#joinOperatorRule.
    def exitJoinOperatorRule(self, ctx:DCLParser.JoinOperatorRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#JoinOnConstraint.
    def enterJoinOnConstraint(self, ctx:DCLParser.JoinOnConstraintContext):
        pass

    # Exit a parse tree produced by DCLParser#JoinOnConstraint.
    def exitJoinOnConstraint(self, ctx:DCLParser.JoinOnConstraintContext):
        pass


    # Enter a parse tree produced by DCLParser#JoinUsingConstraint.
    def enterJoinUsingConstraint(self, ctx:DCLParser.JoinUsingConstraintContext):
        pass

    # Exit a parse tree produced by DCLParser#JoinUsingConstraint.
    def exitJoinUsingConstraint(self, ctx:DCLParser.JoinUsingConstraintContext):
        pass


    # Enter a parse tree produced by DCLParser#StarResult.
    def enterStarResult(self, ctx:DCLParser.StarResultContext):
        pass

    # Exit a parse tree produced by DCLParser#StarResult.
    def exitStarResult(self, ctx:DCLParser.StarResultContext):
        pass


    # Enter a parse tree produced by DCLParser#ExpressionResult.
    def enterExpressionResult(self, ctx:DCLParser.ExpressionResultContext):
        pass

    # Exit a parse tree produced by DCLParser#ExpressionResult.
    def exitExpressionResult(self, ctx:DCLParser.ExpressionResultContext):
        pass


    # Enter a parse tree produced by DCLParser#Union.
    def enterUnion(self, ctx:DCLParser.UnionContext):
        pass

    # Exit a parse tree produced by DCLParser#Union.
    def exitUnion(self, ctx:DCLParser.UnionContext):
        pass


    # Enter a parse tree produced by DCLParser#UnionAll.
    def enterUnionAll(self, ctx:DCLParser.UnionAllContext):
        pass

    # Exit a parse tree produced by DCLParser#UnionAll.
    def exitUnionAll(self, ctx:DCLParser.UnionAllContext):
        pass


    # Enter a parse tree produced by DCLParser#Intersect.
    def enterIntersect(self, ctx:DCLParser.IntersectContext):
        pass

    # Exit a parse tree produced by DCLParser#Intersect.
    def exitIntersect(self, ctx:DCLParser.IntersectContext):
        pass


    # Enter a parse tree produced by DCLParser#Except.
    def enterExcept(self, ctx:DCLParser.ExceptContext):
        pass

    # Exit a parse tree produced by DCLParser#Except.
    def exitExcept(self, ctx:DCLParser.ExceptContext):
        pass


    # Enter a parse tree produced by DCLParser#orderByClauseRule.
    def enterOrderByClauseRule(self, ctx:DCLParser.OrderByClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#orderByClauseRule.
    def exitOrderByClauseRule(self, ctx:DCLParser.OrderByClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#orderingTermRule.
    def enterOrderingTermRule(self, ctx:DCLParser.OrderingTermRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#orderingTermRule.
    def exitOrderingTermRule(self, ctx:DCLParser.OrderingTermRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#limitClauseRule.
    def enterLimitClauseRule(self, ctx:DCLParser.LimitClauseRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#limitClauseRule.
    def exitLimitClauseRule(self, ctx:DCLParser.LimitClauseRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#typeNameRule.
    def enterTypeNameRule(self, ctx:DCLParser.TypeNameRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#typeNameRule.
    def exitTypeNameRule(self, ctx:DCLParser.TypeNameRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#signedNumberRule.
    def enterSignedNumberRule(self, ctx:DCLParser.SignedNumberRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#signedNumberRule.
    def exitSignedNumberRule(self, ctx:DCLParser.SignedNumberRuleContext):
        pass


    # Enter a parse tree produced by DCLParser#keywordRule.
    def enterKeywordRule(self, ctx:DCLParser.KeywordRuleContext):
        pass

    # Exit a parse tree produced by DCLParser#keywordRule.
    def exitKeywordRule(self, ctx:DCLParser.KeywordRuleContext):
        pass



del DCLParser