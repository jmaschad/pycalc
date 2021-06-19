import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DCLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SCOL=1, DOT=2, OPEN_PAR=3, CLOSE_PAR=4, COMMA=5, ASSIGN=6, STAR=7, PLUS=8, 
		MINUS=9, TILDE=10, PIPE2=11, DIV=12, MOD=13, LT2=14, GT2=15, AMP=16, PIPE=17, 
		LT=18, LT_EQ=19, GT=20, GT_EQ=21, EQ1=22, EQ2=23, NOT_EQ1=24, NOT_EQ2=25, 
		K_ALL=26, K_AND=27, K_AS=28, K_ASC=29, K_BETWEEN=30, K_BY=31, K_CASE=32, 
		K_CAST=33, K_CROSS=34, K_DESC=35, K_DISTINCT=36, K_DROP=37, K_ELSE=38, 
		K_END=39, K_ESCAPE=40, K_EXCEPT=41, K_EXTRACT=42, K_FROM=43, K_GLOB=44, 
		K_GROUP=45, K_HAVING=46, K_IN=47, K_INNER=48, K_INTERSECT=49, K_IS=50, 
		K_ISNULL=51, K_JOIN=52, K_LEFT=53, K_LIKE=54, K_LIMIT=55, K_MATCH=56, 
		K_NATURAL=57, K_NOT=58, K_NOTNULL=59, K_NULL=60, K_OFFSET=61, K_ON=62, 
		K_OR=63, K_ORDER=64, K_OUTER=65, K_RECURSIVE=66, K_REGEXP=67, K_ROW=68, 
		K_SELECT=69, K_THEN=70, K_UNION=71, K_UNIQUE=72, K_USING=73, K_VALUE=74, 
		K_VALUES=75, K_WHEN=76, K_WHERE=77, K_WITH=78, K_YEAR=79, K_MONTH=80, 
		K_DAY=81, K_HOUR=82, K_MINUTE=83, K_SECOND=84, LET_IDENT=85, IDENT=86, 
		NUMERIC_LITERAL=87, STRING_LITERAL=88, SINGLE_LINE_COMMENT=89, MULTILINE_COMMENT=90, 
		SPACES=91, ERROR=92;
	public static final int
		RULE_queryRule = 0, RULE_exprRule = 1, RULE_booleanExprRule = 2, RULE_baseExprRule = 3, 
		RULE_sqlQueryRule = 4, RULE_tableExpressionRule = 5, RULE_selectClauseRule = 6, 
		RULE_selectValueClauseRule = 7, RULE_fromClauseRule = 8, RULE_whereClauseRule = 9, 
		RULE_groupByClauseRule = 10, RULE_joinClauseRule = 11, RULE_tableRule = 12, 
		RULE_tableAliasRule = 13, RULE_joinOperatorRule = 14, RULE_joinConstraintRule = 15, 
		RULE_commonTableExpressionRule = 16, RULE_resultColumnRule = 17, RULE_compoundOperatorRule = 18, 
		RULE_orderByClauseRule = 19, RULE_orderingTermRule = 20, RULE_limitClauseRule = 21, 
		RULE_typeNameRule = 22, RULE_signedNumberRule = 23, RULE_keywordRule = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"queryRule", "exprRule", "booleanExprRule", "baseExprRule", "sqlQueryRule", 
			"tableExpressionRule", "selectClauseRule", "selectValueClauseRule", "fromClauseRule", 
			"whereClauseRule", "groupByClauseRule", "joinClauseRule", "tableRule", 
			"tableAliasRule", "joinOperatorRule", "joinConstraintRule", "commonTableExpressionRule", 
			"resultColumnRule", "compoundOperatorRule", "orderByClauseRule", "orderingTermRule", 
			"limitClauseRule", "typeNameRule", "signedNumberRule", "keywordRule"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'.'", "'('", "')'", "','", "':='", "'*'", "'+'", "'-'", 
			"'~'", "'||'", "'/'", "'%'", "'<<'", "'>>'", "'&'", "'|'", "'<'", "'<='", 
			"'>'", "'>='", "'='", "'=='", "'!='", "'<>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SCOL", "DOT", "OPEN_PAR", "CLOSE_PAR", "COMMA", "ASSIGN", "STAR", 
			"PLUS", "MINUS", "TILDE", "PIPE2", "DIV", "MOD", "LT2", "GT2", "AMP", 
			"PIPE", "LT", "LT_EQ", "GT", "GT_EQ", "EQ1", "EQ2", "NOT_EQ1", "NOT_EQ2", 
			"K_ALL", "K_AND", "K_AS", "K_ASC", "K_BETWEEN", "K_BY", "K_CASE", "K_CAST", 
			"K_CROSS", "K_DESC", "K_DISTINCT", "K_DROP", "K_ELSE", "K_END", "K_ESCAPE", 
			"K_EXCEPT", "K_EXTRACT", "K_FROM", "K_GLOB", "K_GROUP", "K_HAVING", "K_IN", 
			"K_INNER", "K_INTERSECT", "K_IS", "K_ISNULL", "K_JOIN", "K_LEFT", "K_LIKE", 
			"K_LIMIT", "K_MATCH", "K_NATURAL", "K_NOT", "K_NOTNULL", "K_NULL", "K_OFFSET", 
			"K_ON", "K_OR", "K_ORDER", "K_OUTER", "K_RECURSIVE", "K_REGEXP", "K_ROW", 
			"K_SELECT", "K_THEN", "K_UNION", "K_UNIQUE", "K_USING", "K_VALUE", "K_VALUES", 
			"K_WHEN", "K_WHERE", "K_WITH", "K_YEAR", "K_MONTH", "K_DAY", "K_HOUR", 
			"K_MINUTE", "K_SECOND", "LET_IDENT", "IDENT", "NUMERIC_LITERAL", "STRING_LITERAL", 
			"SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", "ERROR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DCL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DCLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class QueryRuleContext extends ParserRuleContext {
		public ExprRuleContext exprRule() {
			return getRuleContext(ExprRuleContext.class,0);
		}
		public TerminalNode EOF() { return getToken(DCLParser.EOF, 0); }
		public QueryRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryRule; }
	}

	public final QueryRuleContext queryRule() throws RecognitionException {
		QueryRuleContext _localctx = new QueryRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_queryRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			exprRule();
			setState(51);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprRuleContext extends ParserRuleContext {
		public ExprRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprRule; }
	 
		public ExprRuleContext() { }
		public void copyFrom(ExprRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BooleanExpressionContext extends ExprRuleContext {
		public BooleanExprRuleContext booleanExprRule() {
			return getRuleContext(BooleanExprRuleContext.class,0);
		}
		public BooleanExpressionContext(ExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class SqlExpressionContext extends ExprRuleContext {
		public SqlQueryRuleContext sqlQueryRule() {
			return getRuleContext(SqlQueryRuleContext.class,0);
		}
		public SqlExpressionContext(ExprRuleContext ctx) { copyFrom(ctx); }
	}

	public final ExprRuleContext exprRule() throws RecognitionException {
		ExprRuleContext _localctx = new ExprRuleContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_exprRule);
		try {
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case K_SELECT:
			case K_WITH:
				_localctx = new SqlExpressionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				sqlQueryRule();
				}
				break;
			case OPEN_PAR:
			case MINUS:
			case K_NOT:
			case K_NULL:
			case IDENT:
			case NUMERIC_LITERAL:
			case STRING_LITERAL:
				_localctx = new BooleanExpressionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(54);
				booleanExprRule(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BooleanExprRuleContext extends ParserRuleContext {
		public BooleanExprRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanExprRule; }
	 
		public BooleanExprRuleContext() { }
		public void copyFrom(BooleanExprRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NullCheckExpressionContext extends BooleanExprRuleContext {
		public Token isNull;
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public TerminalNode K_NULL() { return getToken(DCLParser.K_NULL, 0); }
		public TerminalNode K_NOTNULL() { return getToken(DCLParser.K_NOTNULL, 0); }
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public TerminalNode K_ISNULL() { return getToken(DCLParser.K_ISNULL, 0); }
		public TerminalNode K_IS() { return getToken(DCLParser.K_IS, 0); }
		public NullCheckExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class BaseExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public BaseExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class IsExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token negate;
		public BaseExprRuleContext rhs;
		public TerminalNode K_IS() { return getToken(DCLParser.K_IS, 0); }
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public IsExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class AndExpressionContext extends BooleanExprRuleContext {
		public BooleanExprRuleContext lhs;
		public BooleanExprRuleContext rhs;
		public TerminalNode K_AND() { return getToken(DCLParser.K_AND, 0); }
		public List<BooleanExprRuleContext> booleanExprRule() {
			return getRuleContexts(BooleanExprRuleContext.class);
		}
		public BooleanExprRuleContext booleanExprRule(int i) {
			return getRuleContext(BooleanExprRuleContext.class,i);
		}
		public AndExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class BetweenExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext value;
		public BaseExprRuleContext lower;
		public BaseExprRuleContext upper;
		public TerminalNode K_BETWEEN() { return getToken(DCLParser.K_BETWEEN, 0); }
		public TerminalNode K_AND() { return getToken(DCLParser.K_AND, 0); }
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public BetweenExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class StringCompExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token negate;
		public BaseExprRuleContext rhs;
		public TerminalNode K_LIKE() { return getToken(DCLParser.K_LIKE, 0); }
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public StringCompExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class HighCompExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token op;
		public BaseExprRuleContext rhs;
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode LT() { return getToken(DCLParser.LT, 0); }
		public TerminalNode LT_EQ() { return getToken(DCLParser.LT_EQ, 0); }
		public TerminalNode GT() { return getToken(DCLParser.GT, 0); }
		public TerminalNode GT_EQ() { return getToken(DCLParser.GT_EQ, 0); }
		public HighCompExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class NotExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext value;
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public NotExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class OrExpressionContext extends BooleanExprRuleContext {
		public BooleanExprRuleContext lhs;
		public BooleanExprRuleContext rhs;
		public TerminalNode K_OR() { return getToken(DCLParser.K_OR, 0); }
		public List<BooleanExprRuleContext> booleanExprRule() {
			return getRuleContexts(BooleanExprRuleContext.class);
		}
		public BooleanExprRuleContext booleanExprRule(int i) {
			return getRuleContext(BooleanExprRuleContext.class,i);
		}
		public OrExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class LowCompExpressionContext extends BooleanExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token op;
		public BaseExprRuleContext rhs;
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode EQ1() { return getToken(DCLParser.EQ1, 0); }
		public TerminalNode EQ2() { return getToken(DCLParser.EQ2, 0); }
		public TerminalNode NOT_EQ1() { return getToken(DCLParser.NOT_EQ1, 0); }
		public TerminalNode NOT_EQ2() { return getToken(DCLParser.NOT_EQ2, 0); }
		public LowCompExpressionContext(BooleanExprRuleContext ctx) { copyFrom(ctx); }
	}

	public final BooleanExprRuleContext booleanExprRule() throws RecognitionException {
		return booleanExprRule(0);
	}

	private BooleanExprRuleContext booleanExprRule(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BooleanExprRuleContext _localctx = new BooleanExprRuleContext(_ctx, _parentState);
		BooleanExprRuleContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_booleanExprRule, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				_localctx = new HighCompExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(58);
				((HighCompExpressionContext)_localctx).lhs = baseExprRule(0);
				setState(59);
				((HighCompExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LT) | (1L << LT_EQ) | (1L << GT) | (1L << GT_EQ))) != 0)) ) {
					((HighCompExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(60);
				((HighCompExpressionContext)_localctx).rhs = baseExprRule(0);
				}
				break;
			case 2:
				{
				_localctx = new LowCompExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(62);
				((LowCompExpressionContext)_localctx).lhs = baseExprRule(0);
				setState(63);
				((LowCompExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ1) | (1L << EQ2) | (1L << NOT_EQ1) | (1L << NOT_EQ2))) != 0)) ) {
					((LowCompExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(64);
				((LowCompExpressionContext)_localctx).rhs = baseExprRule(0);
				}
				break;
			case 3:
				{
				_localctx = new NotExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				match(K_NOT);
				setState(67);
				((NotExpressionContext)_localctx).value = baseExprRule(0);
				}
				break;
			case 4:
				{
				_localctx = new StringCompExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(68);
				((StringCompExpressionContext)_localctx).lhs = baseExprRule(0);
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_NOT) {
					{
					setState(69);
					((StringCompExpressionContext)_localctx).negate = match(K_NOT);
					}
				}

				setState(72);
				match(K_LIKE);
				setState(73);
				((StringCompExpressionContext)_localctx).rhs = baseExprRule(0);
				}
				break;
			case 5:
				{
				_localctx = new BetweenExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(75);
				((BetweenExpressionContext)_localctx).value = baseExprRule(0);
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_NOT) {
					{
					setState(76);
					match(K_NOT);
					}
				}

				setState(79);
				match(K_BETWEEN);
				setState(80);
				((BetweenExpressionContext)_localctx).lower = baseExprRule(0);
				setState(81);
				match(K_AND);
				setState(82);
				((BetweenExpressionContext)_localctx).upper = baseExprRule(0);
				}
				break;
			case 6:
				{
				_localctx = new NullCheckExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(84);
				baseExprRule(0);
				setState(91);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case K_ISNULL:
					{
					setState(85);
					((NullCheckExpressionContext)_localctx).isNull = match(K_ISNULL);
					}
					break;
				case K_IS:
					{
					setState(86);
					((NullCheckExpressionContext)_localctx).isNull = match(K_IS);
					setState(87);
					match(K_NULL);
					}
					break;
				case K_NOTNULL:
					{
					setState(88);
					match(K_NOTNULL);
					}
					break;
				case K_NOT:
					{
					setState(89);
					match(K_NOT);
					setState(90);
					match(K_NULL);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 7:
				{
				_localctx = new IsExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(93);
				((IsExpressionContext)_localctx).lhs = baseExprRule(0);
				setState(94);
				match(K_IS);
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_NOT) {
					{
					setState(95);
					((IsExpressionContext)_localctx).negate = match(K_NOT);
					}
				}

				setState(98);
				((IsExpressionContext)_localctx).rhs = baseExprRule(0);
				}
				break;
			case 8:
				{
				_localctx = new BaseExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(100);
				baseExprRule(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(111);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(109);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new AndExpressionContext(new BooleanExprRuleContext(_parentctx, _parentState));
						((AndExpressionContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_booleanExprRule);
						setState(103);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(104);
						match(K_AND);
						setState(105);
						((AndExpressionContext)_localctx).rhs = booleanExprRule(8);
						}
						break;
					case 2:
						{
						_localctx = new OrExpressionContext(new BooleanExprRuleContext(_parentctx, _parentState));
						((OrExpressionContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_booleanExprRule);
						setState(106);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(107);
						match(K_OR);
						setState(108);
						((OrExpressionContext)_localctx).rhs = booleanExprRule(7);
						}
						break;
					}
					} 
				}
				setState(113);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BaseExprRuleContext extends ParserRuleContext {
		public BaseExprRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_baseExprRule; }
	 
		public BaseExprRuleContext() { }
		public void copyFrom(BaseExprRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NegateExpressionContext extends BaseExprRuleContext {
		public BaseExprRuleContext value;
		public TerminalNode MINUS() { return getToken(DCLParser.MINUS, 0); }
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public NegateExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class PathExpressionContext extends BaseExprRuleContext {
		public Token IDENT;
		public List<Token> segments = new ArrayList<Token>();
		public List<TerminalNode> IDENT() { return getTokens(DCLParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(DCLParser.IDENT, i);
		}
		public List<TerminalNode> DOT() { return getTokens(DCLParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(DCLParser.DOT, i);
		}
		public PathExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class NumericLiteralContext extends BaseExprRuleContext {
		public TerminalNode NUMERIC_LITERAL() { return getToken(DCLParser.NUMERIC_LITERAL, 0); }
		public NumericLiteralContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class StringLiteralContext extends BaseExprRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(DCLParser.STRING_LITERAL, 0); }
		public StringLiteralContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class HighMathExpressionContext extends BaseExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token op;
		public BaseExprRuleContext rhs;
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode STAR() { return getToken(DCLParser.STAR, 0); }
		public TerminalNode DIV() { return getToken(DCLParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(DCLParser.MOD, 0); }
		public HighMathExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class ParenExpressionContext extends BaseExprRuleContext {
		public TerminalNode OPEN_PAR() { return getToken(DCLParser.OPEN_PAR, 0); }
		public ExprRuleContext exprRule() {
			return getRuleContext(ExprRuleContext.class,0);
		}
		public TerminalNode CLOSE_PAR() { return getToken(DCLParser.CLOSE_PAR, 0); }
		public ParenExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class NullLiteralContext extends BaseExprRuleContext {
		public TerminalNode K_NULL() { return getToken(DCLParser.K_NULL, 0); }
		public NullLiteralContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class ApplyExpressionContext extends BaseExprRuleContext {
		public Token funcName;
		public ExprRuleContext exprRule;
		public List<ExprRuleContext> args = new ArrayList<ExprRuleContext>();
		public Token starCount;
		public TerminalNode OPEN_PAR() { return getToken(DCLParser.OPEN_PAR, 0); }
		public TerminalNode CLOSE_PAR() { return getToken(DCLParser.CLOSE_PAR, 0); }
		public TerminalNode IDENT() { return getToken(DCLParser.IDENT, 0); }
		public List<ExprRuleContext> exprRule() {
			return getRuleContexts(ExprRuleContext.class);
		}
		public ExprRuleContext exprRule(int i) {
			return getRuleContext(ExprRuleContext.class,i);
		}
		public TerminalNode STAR() { return getToken(DCLParser.STAR, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public ApplyExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}
	public static class LowMathExpressionContext extends BaseExprRuleContext {
		public BaseExprRuleContext lhs;
		public Token op;
		public BaseExprRuleContext rhs;
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(DCLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(DCLParser.MINUS, 0); }
		public LowMathExpressionContext(BaseExprRuleContext ctx) { copyFrom(ctx); }
	}

	public final BaseExprRuleContext baseExprRule() throws RecognitionException {
		return baseExprRule(0);
	}

	private BaseExprRuleContext baseExprRule(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BaseExprRuleContext _localctx = new BaseExprRuleContext(_ctx, _parentState);
		BaseExprRuleContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_baseExprRule, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				_localctx = new NegateExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(115);
				match(MINUS);
				setState(116);
				((NegateExpressionContext)_localctx).value = baseExprRule(9);
				}
				break;
			case 2:
				{
				_localctx = new ApplyExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(117);
				((ApplyExpressionContext)_localctx).funcName = match(IDENT);
				setState(118);
				match(OPEN_PAR);
				setState(128);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case OPEN_PAR:
				case MINUS:
				case K_NOT:
				case K_NULL:
				case K_SELECT:
				case K_WITH:
				case IDENT:
				case NUMERIC_LITERAL:
				case STRING_LITERAL:
					{
					setState(119);
					((ApplyExpressionContext)_localctx).exprRule = exprRule();
					((ApplyExpressionContext)_localctx).args.add(((ApplyExpressionContext)_localctx).exprRule);
					setState(124);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(120);
						match(COMMA);
						setState(121);
						((ApplyExpressionContext)_localctx).exprRule = exprRule();
						((ApplyExpressionContext)_localctx).args.add(((ApplyExpressionContext)_localctx).exprRule);
						}
						}
						setState(126);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					break;
				case STAR:
					{
					setState(127);
					((ApplyExpressionContext)_localctx).starCount = match(STAR);
					}
					break;
				case CLOSE_PAR:
					break;
				default:
					break;
				}
				setState(130);
				match(CLOSE_PAR);
				}
				break;
			case 3:
				{
				_localctx = new PathExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(131);
				((PathExpressionContext)_localctx).IDENT = match(IDENT);
				((PathExpressionContext)_localctx).segments.add(((PathExpressionContext)_localctx).IDENT);
				setState(136);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(132);
						match(DOT);
						setState(133);
						((PathExpressionContext)_localctx).IDENT = match(IDENT);
						((PathExpressionContext)_localctx).segments.add(((PathExpressionContext)_localctx).IDENT);
						}
						} 
					}
					setState(138);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				}
				}
				break;
			case 4:
				{
				_localctx = new NullLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(139);
				match(K_NULL);
				}
				break;
			case 5:
				{
				_localctx = new NumericLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(140);
				match(NUMERIC_LITERAL);
				}
				break;
			case 6:
				{
				_localctx = new StringLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(141);
				match(STRING_LITERAL);
				}
				break;
			case 7:
				{
				_localctx = new ParenExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(142);
				match(OPEN_PAR);
				setState(143);
				exprRule();
				setState(144);
				match(CLOSE_PAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(156);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(154);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
					case 1:
						{
						_localctx = new HighMathExpressionContext(new BaseExprRuleContext(_parentctx, _parentState));
						((HighMathExpressionContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_baseExprRule);
						setState(148);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(149);
						((HighMathExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << DIV) | (1L << MOD))) != 0)) ) {
							((HighMathExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(150);
						((HighMathExpressionContext)_localctx).rhs = baseExprRule(9);
						}
						break;
					case 2:
						{
						_localctx = new LowMathExpressionContext(new BaseExprRuleContext(_parentctx, _parentState));
						((LowMathExpressionContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_baseExprRule);
						setState(151);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(152);
						((LowMathExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((LowMathExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(153);
						((LowMathExpressionContext)_localctx).rhs = baseExprRule(8);
						}
						break;
					}
					} 
				}
				setState(158);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class SqlQueryRuleContext extends ParserRuleContext {
		public List<TableExpressionRuleContext> tableExpressionRule() {
			return getRuleContexts(TableExpressionRuleContext.class);
		}
		public TableExpressionRuleContext tableExpressionRule(int i) {
			return getRuleContext(TableExpressionRuleContext.class,i);
		}
		public TerminalNode K_WITH() { return getToken(DCLParser.K_WITH, 0); }
		public List<CommonTableExpressionRuleContext> commonTableExpressionRule() {
			return getRuleContexts(CommonTableExpressionRuleContext.class);
		}
		public CommonTableExpressionRuleContext commonTableExpressionRule(int i) {
			return getRuleContext(CommonTableExpressionRuleContext.class,i);
		}
		public List<CompoundOperatorRuleContext> compoundOperatorRule() {
			return getRuleContexts(CompoundOperatorRuleContext.class);
		}
		public CompoundOperatorRuleContext compoundOperatorRule(int i) {
			return getRuleContext(CompoundOperatorRuleContext.class,i);
		}
		public TerminalNode K_RECURSIVE() { return getToken(DCLParser.K_RECURSIVE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public SqlQueryRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sqlQueryRule; }
	}

	public final SqlQueryRuleContext sqlQueryRule() throws RecognitionException {
		SqlQueryRuleContext _localctx = new SqlQueryRuleContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_sqlQueryRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_WITH) {
				{
				setState(159);
				match(K_WITH);
				setState(161);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_RECURSIVE) {
					{
					setState(160);
					match(K_RECURSIVE);
					}
				}

				setState(163);
				commonTableExpressionRule();
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(164);
					match(COMMA);
					setState(165);
					commonTableExpressionRule();
					}
					}
					setState(170);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(173);
			tableExpressionRule();
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 41)) & ~0x3f) == 0 && ((1L << (_la - 41)) & ((1L << (K_EXCEPT - 41)) | (1L << (K_INTERSECT - 41)) | (1L << (K_UNION - 41)))) != 0)) {
				{
				{
				setState(174);
				compoundOperatorRule();
				setState(175);
				tableExpressionRule();
				}
				}
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableExpressionRuleContext extends ParserRuleContext {
		public SelectClauseRuleContext selectClauseRule() {
			return getRuleContext(SelectClauseRuleContext.class,0);
		}
		public SelectValueClauseRuleContext selectValueClauseRule() {
			return getRuleContext(SelectValueClauseRuleContext.class,0);
		}
		public FromClauseRuleContext fromClauseRule() {
			return getRuleContext(FromClauseRuleContext.class,0);
		}
		public WhereClauseRuleContext whereClauseRule() {
			return getRuleContext(WhereClauseRuleContext.class,0);
		}
		public GroupByClauseRuleContext groupByClauseRule() {
			return getRuleContext(GroupByClauseRuleContext.class,0);
		}
		public OrderByClauseRuleContext orderByClauseRule() {
			return getRuleContext(OrderByClauseRuleContext.class,0);
		}
		public LimitClauseRuleContext limitClauseRule() {
			return getRuleContext(LimitClauseRuleContext.class,0);
		}
		public TableExpressionRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableExpressionRule; }
	}

	public final TableExpressionRuleContext tableExpressionRule() throws RecognitionException {
		TableExpressionRuleContext _localctx = new TableExpressionRuleContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tableExpressionRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(182);
				selectClauseRule();
				}
				break;
			case 2:
				{
				setState(183);
				selectValueClauseRule();
				}
				break;
			}
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_FROM) {
				{
				setState(186);
				fromClauseRule();
				}
			}

			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_WHERE) {
				{
				setState(189);
				whereClauseRule();
				}
			}

			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_GROUP) {
				{
				setState(192);
				groupByClauseRule();
				}
			}

			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_ORDER) {
				{
				setState(195);
				orderByClauseRule();
				}
			}

			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_LIMIT) {
				{
				setState(198);
				limitClauseRule();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectClauseRuleContext extends ParserRuleContext {
		public TerminalNode K_SELECT() { return getToken(DCLParser.K_SELECT, 0); }
		public List<ResultColumnRuleContext> resultColumnRule() {
			return getRuleContexts(ResultColumnRuleContext.class);
		}
		public ResultColumnRuleContext resultColumnRule(int i) {
			return getRuleContext(ResultColumnRuleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public TerminalNode K_DISTINCT() { return getToken(DCLParser.K_DISTINCT, 0); }
		public TerminalNode K_ALL() { return getToken(DCLParser.K_ALL, 0); }
		public SelectClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectClauseRule; }
	}

	public final SelectClauseRuleContext selectClauseRule() throws RecognitionException {
		SelectClauseRuleContext _localctx = new SelectClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_selectClauseRule);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(K_SELECT);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_ALL || _la==K_DISTINCT) {
				{
				setState(202);
				_la = _input.LA(1);
				if ( !(_la==K_ALL || _la==K_DISTINCT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(205);
			resultColumnRule();
			setState(210);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(206);
					match(COMMA);
					setState(207);
					resultColumnRule();
					}
					} 
				}
				setState(212);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectValueClauseRuleContext extends ParserRuleContext {
		public TerminalNode K_SELECT() { return getToken(DCLParser.K_SELECT, 0); }
		public TerminalNode K_VALUE() { return getToken(DCLParser.K_VALUE, 0); }
		public BooleanExprRuleContext booleanExprRule() {
			return getRuleContext(BooleanExprRuleContext.class,0);
		}
		public SelectValueClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectValueClauseRule; }
	}

	public final SelectValueClauseRuleContext selectValueClauseRule() throws RecognitionException {
		SelectValueClauseRuleContext _localctx = new SelectValueClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_selectValueClauseRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(K_SELECT);
			setState(214);
			match(K_VALUE);
			setState(215);
			booleanExprRule(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FromClauseRuleContext extends ParserRuleContext {
		public TerminalNode K_FROM() { return getToken(DCLParser.K_FROM, 0); }
		public List<TableRuleContext> tableRule() {
			return getRuleContexts(TableRuleContext.class);
		}
		public TableRuleContext tableRule(int i) {
			return getRuleContext(TableRuleContext.class,i);
		}
		public JoinClauseRuleContext joinClauseRule() {
			return getRuleContext(JoinClauseRuleContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public FromClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fromClauseRule; }
	}

	public final FromClauseRuleContext fromClauseRule() throws RecognitionException {
		FromClauseRuleContext _localctx = new FromClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_fromClauseRule);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(K_FROM);
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(218);
				tableRule();
				setState(223);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(219);
						match(COMMA);
						setState(220);
						tableRule();
						}
						} 
					}
					setState(225);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				}
				}
				break;
			case 2:
				{
				setState(226);
				joinClauseRule();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhereClauseRuleContext extends ParserRuleContext {
		public BooleanExprRuleContext where;
		public TerminalNode K_WHERE() { return getToken(DCLParser.K_WHERE, 0); }
		public BooleanExprRuleContext booleanExprRule() {
			return getRuleContext(BooleanExprRuleContext.class,0);
		}
		public WhereClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whereClauseRule; }
	}

	public final WhereClauseRuleContext whereClauseRule() throws RecognitionException {
		WhereClauseRuleContext _localctx = new WhereClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whereClauseRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(K_WHERE);
			setState(230);
			((WhereClauseRuleContext)_localctx).where = booleanExprRule(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GroupByClauseRuleContext extends ParserRuleContext {
		public BaseExprRuleContext baseExprRule;
		public List<BaseExprRuleContext> groupBy = new ArrayList<BaseExprRuleContext>();
		public BaseExprRuleContext having;
		public TerminalNode K_GROUP() { return getToken(DCLParser.K_GROUP, 0); }
		public TerminalNode K_BY() { return getToken(DCLParser.K_BY, 0); }
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public TerminalNode K_HAVING() { return getToken(DCLParser.K_HAVING, 0); }
		public GroupByClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groupByClauseRule; }
	}

	public final GroupByClauseRuleContext groupByClauseRule() throws RecognitionException {
		GroupByClauseRuleContext _localctx = new GroupByClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_groupByClauseRule);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(K_GROUP);
			setState(233);
			match(K_BY);
			setState(234);
			((GroupByClauseRuleContext)_localctx).baseExprRule = baseExprRule(0);
			((GroupByClauseRuleContext)_localctx).groupBy.add(((GroupByClauseRuleContext)_localctx).baseExprRule);
			setState(239);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(235);
					match(COMMA);
					setState(236);
					((GroupByClauseRuleContext)_localctx).baseExprRule = baseExprRule(0);
					((GroupByClauseRuleContext)_localctx).groupBy.add(((GroupByClauseRuleContext)_localctx).baseExprRule);
					}
					} 
				}
				setState(241);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			}
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_HAVING) {
				{
				setState(242);
				match(K_HAVING);
				setState(243);
				((GroupByClauseRuleContext)_localctx).having = baseExprRule(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class JoinClauseRuleContext extends ParserRuleContext {
		public List<TableRuleContext> tableRule() {
			return getRuleContexts(TableRuleContext.class);
		}
		public TableRuleContext tableRule(int i) {
			return getRuleContext(TableRuleContext.class,i);
		}
		public List<JoinOperatorRuleContext> joinOperatorRule() {
			return getRuleContexts(JoinOperatorRuleContext.class);
		}
		public JoinOperatorRuleContext joinOperatorRule(int i) {
			return getRuleContext(JoinOperatorRuleContext.class,i);
		}
		public List<JoinConstraintRuleContext> joinConstraintRule() {
			return getRuleContexts(JoinConstraintRuleContext.class);
		}
		public JoinConstraintRuleContext joinConstraintRule(int i) {
			return getRuleContext(JoinConstraintRuleContext.class,i);
		}
		public JoinClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinClauseRule; }
	}

	public final JoinClauseRuleContext joinClauseRule() throws RecognitionException {
		JoinClauseRuleContext _localctx = new JoinClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_joinClauseRule);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			tableRule();
			setState(254);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(247);
					joinOperatorRule();
					setState(248);
					tableRule();
					setState(250);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==K_ON || _la==K_USING) {
						{
						setState(249);
						joinConstraintRule();
						}
					}

					}
					} 
				}
				setState(256);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableRuleContext extends ParserRuleContext {
		public BaseExprRuleContext table;
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public TableAliasRuleContext tableAliasRule() {
			return getRuleContext(TableAliasRuleContext.class,0);
		}
		public TableRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableRule; }
	}

	public final TableRuleContext tableRule() throws RecognitionException {
		TableRuleContext _localctx = new TableRuleContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_tableRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			((TableRuleContext)_localctx).table = baseExprRule(0);
			setState(259);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_AS || _la==IDENT) {
				{
				setState(258);
				tableAliasRule();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableAliasRuleContext extends ParserRuleContext {
		public Token tableAlias;
		public Token IDENT;
		public List<Token> columnAlias = new ArrayList<Token>();
		public List<TerminalNode> IDENT() { return getTokens(DCLParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(DCLParser.IDENT, i);
		}
		public TerminalNode K_AS() { return getToken(DCLParser.K_AS, 0); }
		public TerminalNode OPEN_PAR() { return getToken(DCLParser.OPEN_PAR, 0); }
		public TerminalNode CLOSE_PAR() { return getToken(DCLParser.CLOSE_PAR, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public TableAliasRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableAliasRule; }
	}

	public final TableAliasRuleContext tableAliasRule() throws RecognitionException {
		TableAliasRuleContext _localctx = new TableAliasRuleContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_tableAliasRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_AS) {
				{
				setState(261);
				match(K_AS);
				}
			}

			setState(264);
			((TableAliasRuleContext)_localctx).tableAlias = match(IDENT);
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAR) {
				{
				setState(265);
				match(OPEN_PAR);
				setState(266);
				((TableAliasRuleContext)_localctx).IDENT = match(IDENT);
				((TableAliasRuleContext)_localctx).columnAlias.add(((TableAliasRuleContext)_localctx).IDENT);
				setState(271);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(267);
					match(COMMA);
					setState(268);
					((TableAliasRuleContext)_localctx).IDENT = match(IDENT);
					((TableAliasRuleContext)_localctx).columnAlias.add(((TableAliasRuleContext)_localctx).IDENT);
					}
					}
					setState(273);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(274);
				match(CLOSE_PAR);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class JoinOperatorRuleContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(DCLParser.COMMA, 0); }
		public TerminalNode K_JOIN() { return getToken(DCLParser.K_JOIN, 0); }
		public TerminalNode K_NATURAL() { return getToken(DCLParser.K_NATURAL, 0); }
		public TerminalNode K_LEFT() { return getToken(DCLParser.K_LEFT, 0); }
		public TerminalNode K_INNER() { return getToken(DCLParser.K_INNER, 0); }
		public TerminalNode K_CROSS() { return getToken(DCLParser.K_CROSS, 0); }
		public TerminalNode K_OUTER() { return getToken(DCLParser.K_OUTER, 0); }
		public JoinOperatorRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinOperatorRule; }
	}

	public final JoinOperatorRuleContext joinOperatorRule() throws RecognitionException {
		JoinOperatorRuleContext _localctx = new JoinOperatorRuleContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_joinOperatorRule);
		int _la;
		try {
			setState(290);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				match(COMMA);
				}
				break;
			case K_CROSS:
			case K_INNER:
			case K_JOIN:
			case K_LEFT:
			case K_NATURAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_NATURAL) {
					{
					setState(278);
					match(K_NATURAL);
					}
				}

				setState(287);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case K_LEFT:
					{
					setState(281);
					match(K_LEFT);
					setState(283);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==K_OUTER) {
						{
						setState(282);
						match(K_OUTER);
						}
					}

					}
					break;
				case K_INNER:
					{
					setState(285);
					match(K_INNER);
					}
					break;
				case K_CROSS:
					{
					setState(286);
					match(K_CROSS);
					}
					break;
				case K_JOIN:
					break;
				default:
					break;
				}
				setState(289);
				match(K_JOIN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class JoinConstraintRuleContext extends ParserRuleContext {
		public JoinConstraintRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinConstraintRule; }
	 
		public JoinConstraintRuleContext() { }
		public void copyFrom(JoinConstraintRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class JoinUsingConstraintContext extends JoinConstraintRuleContext {
		public TerminalNode K_USING() { return getToken(DCLParser.K_USING, 0); }
		public TerminalNode OPEN_PAR() { return getToken(DCLParser.OPEN_PAR, 0); }
		public List<TerminalNode> IDENT() { return getTokens(DCLParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(DCLParser.IDENT, i);
		}
		public TerminalNode CLOSE_PAR() { return getToken(DCLParser.CLOSE_PAR, 0); }
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public JoinUsingConstraintContext(JoinConstraintRuleContext ctx) { copyFrom(ctx); }
	}
	public static class JoinOnConstraintContext extends JoinConstraintRuleContext {
		public TerminalNode K_ON() { return getToken(DCLParser.K_ON, 0); }
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public JoinOnConstraintContext(JoinConstraintRuleContext ctx) { copyFrom(ctx); }
	}

	public final JoinConstraintRuleContext joinConstraintRule() throws RecognitionException {
		JoinConstraintRuleContext _localctx = new JoinConstraintRuleContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_joinConstraintRule);
		int _la;
		try {
			setState(305);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case K_ON:
				_localctx = new JoinOnConstraintContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				match(K_ON);
				setState(293);
				baseExprRule(0);
				}
				break;
			case K_USING:
				_localctx = new JoinUsingConstraintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(294);
				match(K_USING);
				setState(295);
				match(OPEN_PAR);
				setState(296);
				match(IDENT);
				setState(301);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(297);
					match(COMMA);
					setState(298);
					match(IDENT);
					}
					}
					setState(303);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(304);
				match(CLOSE_PAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommonTableExpressionRuleContext extends ParserRuleContext {
		public List<TerminalNode> IDENT() { return getTokens(DCLParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(DCLParser.IDENT, i);
		}
		public TerminalNode K_AS() { return getToken(DCLParser.K_AS, 0); }
		public List<TerminalNode> OPEN_PAR() { return getTokens(DCLParser.OPEN_PAR); }
		public TerminalNode OPEN_PAR(int i) {
			return getToken(DCLParser.OPEN_PAR, i);
		}
		public SqlQueryRuleContext sqlQueryRule() {
			return getRuleContext(SqlQueryRuleContext.class,0);
		}
		public List<TerminalNode> CLOSE_PAR() { return getTokens(DCLParser.CLOSE_PAR); }
		public TerminalNode CLOSE_PAR(int i) {
			return getToken(DCLParser.CLOSE_PAR, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public CommonTableExpressionRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commonTableExpressionRule; }
	}

	public final CommonTableExpressionRuleContext commonTableExpressionRule() throws RecognitionException {
		CommonTableExpressionRuleContext _localctx = new CommonTableExpressionRuleContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_commonTableExpressionRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(IDENT);
			setState(318);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAR) {
				{
				setState(308);
				match(OPEN_PAR);
				setState(309);
				match(IDENT);
				setState(314);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(310);
					match(COMMA);
					setState(311);
					match(IDENT);
					}
					}
					setState(316);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(317);
				match(CLOSE_PAR);
				}
			}

			setState(320);
			match(K_AS);
			setState(321);
			match(OPEN_PAR);
			setState(322);
			sqlQueryRule();
			setState(323);
			match(CLOSE_PAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ResultColumnRuleContext extends ParserRuleContext {
		public ResultColumnRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_resultColumnRule; }
	 
		public ResultColumnRuleContext() { }
		public void copyFrom(ResultColumnRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StarResultContext extends ResultColumnRuleContext {
		public TerminalNode STAR() { return getToken(DCLParser.STAR, 0); }
		public StarResultContext(ResultColumnRuleContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressionResultContext extends ResultColumnRuleContext {
		public Token columnAlias;
		public BooleanExprRuleContext booleanExprRule() {
			return getRuleContext(BooleanExprRuleContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(DCLParser.IDENT, 0); }
		public TerminalNode K_AS() { return getToken(DCLParser.K_AS, 0); }
		public ExpressionResultContext(ResultColumnRuleContext ctx) { copyFrom(ctx); }
	}
	public static class TableStarResultContext extends ResultColumnRuleContext {
		public Token tableName;
		public TerminalNode DOT() { return getToken(DCLParser.DOT, 0); }
		public TerminalNode STAR() { return getToken(DCLParser.STAR, 0); }
		public TerminalNode IDENT() { return getToken(DCLParser.IDENT, 0); }
		public TableStarResultContext(ResultColumnRuleContext ctx) { copyFrom(ctx); }
	}

	public final ResultColumnRuleContext resultColumnRule() throws RecognitionException {
		ResultColumnRuleContext _localctx = new ResultColumnRuleContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_resultColumnRule);
		int _la;
		try {
			setState(336);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				_localctx = new StarResultContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(325);
				match(STAR);
				}
				break;
			case 2:
				_localctx = new TableStarResultContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(326);
				((TableStarResultContext)_localctx).tableName = match(IDENT);
				setState(327);
				match(DOT);
				setState(328);
				match(STAR);
				}
				break;
			case 3:
				_localctx = new ExpressionResultContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(329);
				booleanExprRule(0);
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==K_AS || _la==IDENT) {
					{
					setState(331);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==K_AS) {
						{
						setState(330);
						match(K_AS);
						}
					}

					setState(333);
					((ExpressionResultContext)_localctx).columnAlias = match(IDENT);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompoundOperatorRuleContext extends ParserRuleContext {
		public CompoundOperatorRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundOperatorRule; }
	 
		public CompoundOperatorRuleContext() { }
		public void copyFrom(CompoundOperatorRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IntersectContext extends CompoundOperatorRuleContext {
		public TerminalNode K_INTERSECT() { return getToken(DCLParser.K_INTERSECT, 0); }
		public IntersectContext(CompoundOperatorRuleContext ctx) { copyFrom(ctx); }
	}
	public static class UnionContext extends CompoundOperatorRuleContext {
		public TerminalNode K_UNION() { return getToken(DCLParser.K_UNION, 0); }
		public UnionContext(CompoundOperatorRuleContext ctx) { copyFrom(ctx); }
	}
	public static class ExceptContext extends CompoundOperatorRuleContext {
		public TerminalNode K_EXCEPT() { return getToken(DCLParser.K_EXCEPT, 0); }
		public ExceptContext(CompoundOperatorRuleContext ctx) { copyFrom(ctx); }
	}
	public static class UnionAllContext extends CompoundOperatorRuleContext {
		public TerminalNode K_UNION() { return getToken(DCLParser.K_UNION, 0); }
		public TerminalNode K_ALL() { return getToken(DCLParser.K_ALL, 0); }
		public UnionAllContext(CompoundOperatorRuleContext ctx) { copyFrom(ctx); }
	}

	public final CompoundOperatorRuleContext compoundOperatorRule() throws RecognitionException {
		CompoundOperatorRuleContext _localctx = new CompoundOperatorRuleContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_compoundOperatorRule);
		try {
			setState(343);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				_localctx = new UnionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				match(K_UNION);
				}
				break;
			case 2:
				_localctx = new UnionAllContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				match(K_UNION);
				setState(340);
				match(K_ALL);
				}
				break;
			case 3:
				_localctx = new IntersectContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(341);
				match(K_INTERSECT);
				}
				break;
			case 4:
				_localctx = new ExceptContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(342);
				match(K_EXCEPT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OrderByClauseRuleContext extends ParserRuleContext {
		public TerminalNode K_ORDER() { return getToken(DCLParser.K_ORDER, 0); }
		public TerminalNode K_BY() { return getToken(DCLParser.K_BY, 0); }
		public List<OrderingTermRuleContext> orderingTermRule() {
			return getRuleContexts(OrderingTermRuleContext.class);
		}
		public OrderingTermRuleContext orderingTermRule(int i) {
			return getRuleContext(OrderingTermRuleContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DCLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DCLParser.COMMA, i);
		}
		public OrderByClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orderByClauseRule; }
	}

	public final OrderByClauseRuleContext orderByClauseRule() throws RecognitionException {
		OrderByClauseRuleContext _localctx = new OrderByClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_orderByClauseRule);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			match(K_ORDER);
			setState(346);
			match(K_BY);
			setState(347);
			orderingTermRule();
			setState(352);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(348);
					match(COMMA);
					setState(349);
					orderingTermRule();
					}
					} 
				}
				setState(354);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,48,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OrderingTermRuleContext extends ParserRuleContext {
		public Token order;
		public BaseExprRuleContext baseExprRule() {
			return getRuleContext(BaseExprRuleContext.class,0);
		}
		public TerminalNode K_ASC() { return getToken(DCLParser.K_ASC, 0); }
		public TerminalNode K_DESC() { return getToken(DCLParser.K_DESC, 0); }
		public OrderingTermRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orderingTermRule; }
	}

	public final OrderingTermRuleContext orderingTermRule() throws RecognitionException {
		OrderingTermRuleContext _localctx = new OrderingTermRuleContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_orderingTermRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			baseExprRule(0);
			setState(357);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==K_ASC || _la==K_DESC) {
				{
				setState(356);
				((OrderingTermRuleContext)_localctx).order = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==K_ASC || _la==K_DESC) ) {
					((OrderingTermRuleContext)_localctx).order = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LimitClauseRuleContext extends ParserRuleContext {
		public BaseExprRuleContext limit;
		public BaseExprRuleContext offset;
		public TerminalNode K_LIMIT() { return getToken(DCLParser.K_LIMIT, 0); }
		public List<BaseExprRuleContext> baseExprRule() {
			return getRuleContexts(BaseExprRuleContext.class);
		}
		public BaseExprRuleContext baseExprRule(int i) {
			return getRuleContext(BaseExprRuleContext.class,i);
		}
		public TerminalNode K_OFFSET() { return getToken(DCLParser.K_OFFSET, 0); }
		public TerminalNode COMMA() { return getToken(DCLParser.COMMA, 0); }
		public LimitClauseRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_limitClauseRule; }
	}

	public final LimitClauseRuleContext limitClauseRule() throws RecognitionException {
		LimitClauseRuleContext _localctx = new LimitClauseRuleContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_limitClauseRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(K_LIMIT);
			setState(360);
			((LimitClauseRuleContext)_localctx).limit = baseExprRule(0);
			setState(363);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				{
				setState(361);
				_la = _input.LA(1);
				if ( !(_la==COMMA || _la==K_OFFSET) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(362);
				((LimitClauseRuleContext)_localctx).offset = baseExprRule(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeNameRuleContext extends ParserRuleContext {
		public List<TerminalNode> IDENT() { return getTokens(DCLParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(DCLParser.IDENT, i);
		}
		public TerminalNode OPEN_PAR() { return getToken(DCLParser.OPEN_PAR, 0); }
		public List<SignedNumberRuleContext> signedNumberRule() {
			return getRuleContexts(SignedNumberRuleContext.class);
		}
		public SignedNumberRuleContext signedNumberRule(int i) {
			return getRuleContext(SignedNumberRuleContext.class,i);
		}
		public TerminalNode CLOSE_PAR() { return getToken(DCLParser.CLOSE_PAR, 0); }
		public TerminalNode COMMA() { return getToken(DCLParser.COMMA, 0); }
		public TypeNameRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeNameRule; }
	}

	public final TypeNameRuleContext typeNameRule() throws RecognitionException {
		TypeNameRuleContext _localctx = new TypeNameRuleContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_typeNameRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(365);
				match(IDENT);
				}
				}
				setState(368); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IDENT );
			setState(380);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,52,_ctx) ) {
			case 1:
				{
				setState(370);
				match(OPEN_PAR);
				setState(371);
				signedNumberRule();
				setState(372);
				match(CLOSE_PAR);
				}
				break;
			case 2:
				{
				setState(374);
				match(OPEN_PAR);
				setState(375);
				signedNumberRule();
				setState(376);
				match(COMMA);
				setState(377);
				signedNumberRule();
				setState(378);
				match(CLOSE_PAR);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SignedNumberRuleContext extends ParserRuleContext {
		public TerminalNode NUMERIC_LITERAL() { return getToken(DCLParser.NUMERIC_LITERAL, 0); }
		public TerminalNode PLUS() { return getToken(DCLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(DCLParser.MINUS, 0); }
		public SignedNumberRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signedNumberRule; }
	}

	public final SignedNumberRuleContext signedNumberRule() throws RecognitionException {
		SignedNumberRuleContext _localctx = new SignedNumberRuleContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_signedNumberRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(383);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
				setState(382);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(385);
			match(NUMERIC_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KeywordRuleContext extends ParserRuleContext {
		public TerminalNode K_ALL() { return getToken(DCLParser.K_ALL, 0); }
		public TerminalNode K_AND() { return getToken(DCLParser.K_AND, 0); }
		public TerminalNode K_AS() { return getToken(DCLParser.K_AS, 0); }
		public TerminalNode K_ASC() { return getToken(DCLParser.K_ASC, 0); }
		public TerminalNode K_BETWEEN() { return getToken(DCLParser.K_BETWEEN, 0); }
		public TerminalNode K_BY() { return getToken(DCLParser.K_BY, 0); }
		public TerminalNode K_CASE() { return getToken(DCLParser.K_CASE, 0); }
		public TerminalNode K_CAST() { return getToken(DCLParser.K_CAST, 0); }
		public TerminalNode K_CROSS() { return getToken(DCLParser.K_CROSS, 0); }
		public TerminalNode K_DESC() { return getToken(DCLParser.K_DESC, 0); }
		public TerminalNode K_DISTINCT() { return getToken(DCLParser.K_DISTINCT, 0); }
		public TerminalNode K_DROP() { return getToken(DCLParser.K_DROP, 0); }
		public TerminalNode K_ELSE() { return getToken(DCLParser.K_ELSE, 0); }
		public TerminalNode K_END() { return getToken(DCLParser.K_END, 0); }
		public TerminalNode K_ESCAPE() { return getToken(DCLParser.K_ESCAPE, 0); }
		public TerminalNode K_EXCEPT() { return getToken(DCLParser.K_EXCEPT, 0); }
		public TerminalNode K_FROM() { return getToken(DCLParser.K_FROM, 0); }
		public TerminalNode K_GLOB() { return getToken(DCLParser.K_GLOB, 0); }
		public TerminalNode K_GROUP() { return getToken(DCLParser.K_GROUP, 0); }
		public TerminalNode K_HAVING() { return getToken(DCLParser.K_HAVING, 0); }
		public TerminalNode K_IN() { return getToken(DCLParser.K_IN, 0); }
		public TerminalNode K_INNER() { return getToken(DCLParser.K_INNER, 0); }
		public TerminalNode K_INTERSECT() { return getToken(DCLParser.K_INTERSECT, 0); }
		public TerminalNode K_IS() { return getToken(DCLParser.K_IS, 0); }
		public TerminalNode K_ISNULL() { return getToken(DCLParser.K_ISNULL, 0); }
		public TerminalNode K_JOIN() { return getToken(DCLParser.K_JOIN, 0); }
		public TerminalNode K_LEFT() { return getToken(DCLParser.K_LEFT, 0); }
		public TerminalNode K_LIKE() { return getToken(DCLParser.K_LIKE, 0); }
		public TerminalNode K_LIMIT() { return getToken(DCLParser.K_LIMIT, 0); }
		public TerminalNode K_MATCH() { return getToken(DCLParser.K_MATCH, 0); }
		public TerminalNode K_NATURAL() { return getToken(DCLParser.K_NATURAL, 0); }
		public TerminalNode K_NOT() { return getToken(DCLParser.K_NOT, 0); }
		public TerminalNode K_NOTNULL() { return getToken(DCLParser.K_NOTNULL, 0); }
		public TerminalNode K_NULL() { return getToken(DCLParser.K_NULL, 0); }
		public TerminalNode K_OFFSET() { return getToken(DCLParser.K_OFFSET, 0); }
		public TerminalNode K_ON() { return getToken(DCLParser.K_ON, 0); }
		public TerminalNode K_OR() { return getToken(DCLParser.K_OR, 0); }
		public TerminalNode K_ORDER() { return getToken(DCLParser.K_ORDER, 0); }
		public TerminalNode K_OUTER() { return getToken(DCLParser.K_OUTER, 0); }
		public TerminalNode K_RECURSIVE() { return getToken(DCLParser.K_RECURSIVE, 0); }
		public TerminalNode K_REGEXP() { return getToken(DCLParser.K_REGEXP, 0); }
		public TerminalNode K_SELECT() { return getToken(DCLParser.K_SELECT, 0); }
		public TerminalNode K_THEN() { return getToken(DCLParser.K_THEN, 0); }
		public TerminalNode K_UNION() { return getToken(DCLParser.K_UNION, 0); }
		public TerminalNode K_UNIQUE() { return getToken(DCLParser.K_UNIQUE, 0); }
		public TerminalNode K_USING() { return getToken(DCLParser.K_USING, 0); }
		public TerminalNode K_VALUES() { return getToken(DCLParser.K_VALUES, 0); }
		public TerminalNode K_WHEN() { return getToken(DCLParser.K_WHEN, 0); }
		public TerminalNode K_WHERE() { return getToken(DCLParser.K_WHERE, 0); }
		public TerminalNode K_WITH() { return getToken(DCLParser.K_WITH, 0); }
		public TerminalNode K_YEAR() { return getToken(DCLParser.K_YEAR, 0); }
		public TerminalNode K_MONTH() { return getToken(DCLParser.K_MONTH, 0); }
		public TerminalNode K_DAY() { return getToken(DCLParser.K_DAY, 0); }
		public TerminalNode K_HOUR() { return getToken(DCLParser.K_HOUR, 0); }
		public TerminalNode K_MINUTE() { return getToken(DCLParser.K_MINUTE, 0); }
		public TerminalNode K_SECOND() { return getToken(DCLParser.K_SECOND, 0); }
		public KeywordRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keywordRule; }
	}

	public final KeywordRuleContext keywordRule() throws RecognitionException {
		KeywordRuleContext _localctx = new KeywordRuleContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_keywordRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(387);
			_la = _input.LA(1);
			if ( !(((((_la - 26)) & ~0x3f) == 0 && ((1L << (_la - 26)) & ((1L << (K_ALL - 26)) | (1L << (K_AND - 26)) | (1L << (K_AS - 26)) | (1L << (K_ASC - 26)) | (1L << (K_BETWEEN - 26)) | (1L << (K_BY - 26)) | (1L << (K_CASE - 26)) | (1L << (K_CAST - 26)) | (1L << (K_CROSS - 26)) | (1L << (K_DESC - 26)) | (1L << (K_DISTINCT - 26)) | (1L << (K_DROP - 26)) | (1L << (K_ELSE - 26)) | (1L << (K_END - 26)) | (1L << (K_ESCAPE - 26)) | (1L << (K_EXCEPT - 26)) | (1L << (K_FROM - 26)) | (1L << (K_GLOB - 26)) | (1L << (K_GROUP - 26)) | (1L << (K_HAVING - 26)) | (1L << (K_IN - 26)) | (1L << (K_INNER - 26)) | (1L << (K_INTERSECT - 26)) | (1L << (K_IS - 26)) | (1L << (K_ISNULL - 26)) | (1L << (K_JOIN - 26)) | (1L << (K_LEFT - 26)) | (1L << (K_LIKE - 26)) | (1L << (K_LIMIT - 26)) | (1L << (K_MATCH - 26)) | (1L << (K_NATURAL - 26)) | (1L << (K_NOT - 26)) | (1L << (K_NOTNULL - 26)) | (1L << (K_NULL - 26)) | (1L << (K_OFFSET - 26)) | (1L << (K_ON - 26)) | (1L << (K_OR - 26)) | (1L << (K_ORDER - 26)) | (1L << (K_OUTER - 26)) | (1L << (K_RECURSIVE - 26)) | (1L << (K_REGEXP - 26)) | (1L << (K_SELECT - 26)) | (1L << (K_THEN - 26)) | (1L << (K_UNION - 26)) | (1L << (K_UNIQUE - 26)) | (1L << (K_USING - 26)) | (1L << (K_VALUES - 26)) | (1L << (K_WHEN - 26)) | (1L << (K_WHERE - 26)) | (1L << (K_WITH - 26)) | (1L << (K_YEAR - 26)) | (1L << (K_MONTH - 26)) | (1L << (K_DAY - 26)) | (1L << (K_HOUR - 26)) | (1L << (K_MINUTE - 26)) | (1L << (K_SECOND - 26)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return booleanExprRule_sempred((BooleanExprRuleContext)_localctx, predIndex);
		case 3:
			return baseExprRule_sempred((BaseExprRuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean booleanExprRule_sempred(BooleanExprRuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		}
		return true;
	}
	private boolean baseExprRule_sempred(BaseExprRuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3^\u0188\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\5\4I\n\4\3\4\3\4\3\4\3\4\3\4\5\4P\n\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4^\n\4\3\4\3\4\3\4\5\4c\n\4\3"+
		"\4\3\4\3\4\5\4h\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4p\n\4\f\4\16\4s\13\4\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080\13\5\3\5\5\5\u0083"+
		"\n\5\3\5\3\5\3\5\3\5\7\5\u0089\n\5\f\5\16\5\u008c\13\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\5\5\u0095\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u009d\n\5\f\5\16"+
		"\5\u00a0\13\5\3\6\3\6\5\6\u00a4\n\6\3\6\3\6\3\6\7\6\u00a9\n\6\f\6\16\6"+
		"\u00ac\13\6\5\6\u00ae\n\6\3\6\3\6\3\6\3\6\7\6\u00b4\n\6\f\6\16\6\u00b7"+
		"\13\6\3\7\3\7\5\7\u00bb\n\7\3\7\5\7\u00be\n\7\3\7\5\7\u00c1\n\7\3\7\5"+
		"\7\u00c4\n\7\3\7\5\7\u00c7\n\7\3\7\5\7\u00ca\n\7\3\b\3\b\5\b\u00ce\n\b"+
		"\3\b\3\b\3\b\7\b\u00d3\n\b\f\b\16\b\u00d6\13\b\3\t\3\t\3\t\3\t\3\n\3\n"+
		"\3\n\3\n\7\n\u00e0\n\n\f\n\16\n\u00e3\13\n\3\n\5\n\u00e6\n\n\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\7\f\u00f0\n\f\f\f\16\f\u00f3\13\f\3\f\3\f\5"+
		"\f\u00f7\n\f\3\r\3\r\3\r\3\r\5\r\u00fd\n\r\7\r\u00ff\n\r\f\r\16\r\u0102"+
		"\13\r\3\16\3\16\5\16\u0106\n\16\3\17\5\17\u0109\n\17\3\17\3\17\3\17\3"+
		"\17\3\17\7\17\u0110\n\17\f\17\16\17\u0113\13\17\3\17\5\17\u0116\n\17\3"+
		"\20\3\20\5\20\u011a\n\20\3\20\3\20\5\20\u011e\n\20\3\20\3\20\5\20\u0122"+
		"\n\20\3\20\5\20\u0125\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u012e"+
		"\n\21\f\21\16\21\u0131\13\21\3\21\5\21\u0134\n\21\3\22\3\22\3\22\3\22"+
		"\3\22\7\22\u013b\n\22\f\22\16\22\u013e\13\22\3\22\5\22\u0141\n\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u014e\n\23\3\23"+
		"\5\23\u0151\n\23\5\23\u0153\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u015a\n"+
		"\24\3\25\3\25\3\25\3\25\3\25\7\25\u0161\n\25\f\25\16\25\u0164\13\25\3"+
		"\26\3\26\5\26\u0168\n\26\3\27\3\27\3\27\3\27\5\27\u016e\n\27\3\30\6\30"+
		"\u0171\n\30\r\30\16\30\u0172\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3"+
		"\30\3\30\5\30\u017f\n\30\3\31\5\31\u0182\n\31\3\31\3\31\3\32\3\32\3\32"+
		"\2\4\6\b\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\n"+
		"\3\2\24\27\3\2\30\33\4\2\t\t\16\17\3\2\n\13\4\2\34\34&&\4\2\37\37%%\4"+
		"\2\7\7??\6\2\34+-EGKMV\2\u01b8\2\64\3\2\2\2\49\3\2\2\2\6g\3\2\2\2\b\u0094"+
		"\3\2\2\2\n\u00ad\3\2\2\2\f\u00ba\3\2\2\2\16\u00cb\3\2\2\2\20\u00d7\3\2"+
		"\2\2\22\u00db\3\2\2\2\24\u00e7\3\2\2\2\26\u00ea\3\2\2\2\30\u00f8\3\2\2"+
		"\2\32\u0103\3\2\2\2\34\u0108\3\2\2\2\36\u0124\3\2\2\2 \u0133\3\2\2\2\""+
		"\u0135\3\2\2\2$\u0152\3\2\2\2&\u0159\3\2\2\2(\u015b\3\2\2\2*\u0165\3\2"+
		"\2\2,\u0169\3\2\2\2.\u0170\3\2\2\2\60\u0181\3\2\2\2\62\u0185\3\2\2\2\64"+
		"\65\5\4\3\2\65\66\7\2\2\3\66\3\3\2\2\2\67:\5\n\6\28:\5\6\4\29\67\3\2\2"+
		"\298\3\2\2\2:\5\3\2\2\2;<\b\4\1\2<=\5\b\5\2=>\t\2\2\2>?\5\b\5\2?h\3\2"+
		"\2\2@A\5\b\5\2AB\t\3\2\2BC\5\b\5\2Ch\3\2\2\2DE\7<\2\2Eh\5\b\5\2FH\5\b"+
		"\5\2GI\7<\2\2HG\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\78\2\2KL\5\b\5\2Lh\3\2\2"+
		"\2MO\5\b\5\2NP\7<\2\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QR\7 \2\2RS\5\b\5\2"+
		"ST\7\35\2\2TU\5\b\5\2Uh\3\2\2\2V]\5\b\5\2W^\7\65\2\2XY\7\64\2\2Y^\7>\2"+
		"\2Z^\7=\2\2[\\\7<\2\2\\^\7>\2\2]W\3\2\2\2]X\3\2\2\2]Z\3\2\2\2][\3\2\2"+
		"\2^h\3\2\2\2_`\5\b\5\2`b\7\64\2\2ac\7<\2\2ba\3\2\2\2bc\3\2\2\2cd\3\2\2"+
		"\2de\5\b\5\2eh\3\2\2\2fh\5\b\5\2g;\3\2\2\2g@\3\2\2\2gD\3\2\2\2gF\3\2\2"+
		"\2gM\3\2\2\2gV\3\2\2\2g_\3\2\2\2gf\3\2\2\2hq\3\2\2\2ij\f\t\2\2jk\7\35"+
		"\2\2kp\5\6\4\nlm\f\b\2\2mn\7A\2\2np\5\6\4\toi\3\2\2\2ol\3\2\2\2ps\3\2"+
		"\2\2qo\3\2\2\2qr\3\2\2\2r\7\3\2\2\2sq\3\2\2\2tu\b\5\1\2uv\7\13\2\2v\u0095"+
		"\5\b\5\13wx\7X\2\2x\u0082\7\5\2\2y~\5\4\3\2z{\7\7\2\2{}\5\4\3\2|z\3\2"+
		"\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0083\3\2\2\2\u0080~\3"+
		"\2\2\2\u0081\u0083\7\t\2\2\u0082y\3\2\2\2\u0082\u0081\3\2\2\2\u0082\u0083"+
		"\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0095\7\6\2\2\u0085\u008a\7X\2\2\u0086"+
		"\u0087\7\4\2\2\u0087\u0089\7X\2\2\u0088\u0086\3\2\2\2\u0089\u008c\3\2"+
		"\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0095\3\2\2\2\u008c"+
		"\u008a\3\2\2\2\u008d\u0095\7>\2\2\u008e\u0095\7Y\2\2\u008f\u0095\7Z\2"+
		"\2\u0090\u0091\7\5\2\2\u0091\u0092\5\4\3\2\u0092\u0093\7\6\2\2\u0093\u0095"+
		"\3\2\2\2\u0094t\3\2\2\2\u0094w\3\2\2\2\u0094\u0085\3\2\2\2\u0094\u008d"+
		"\3\2\2\2\u0094\u008e\3\2\2\2\u0094\u008f\3\2\2\2\u0094\u0090\3\2\2\2\u0095"+
		"\u009e\3\2\2\2\u0096\u0097\f\n\2\2\u0097\u0098\t\4\2\2\u0098\u009d\5\b"+
		"\5\13\u0099\u009a\f\t\2\2\u009a\u009b\t\5\2\2\u009b\u009d\5\b\5\n\u009c"+
		"\u0096\3\2\2\2\u009c\u0099\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2"+
		"\2\2\u009e\u009f\3\2\2\2\u009f\t\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a3"+
		"\7P\2\2\u00a2\u00a4\7D\2\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4"+
		"\u00a5\3\2\2\2\u00a5\u00aa\5\"\22\2\u00a6\u00a7\7\7\2\2\u00a7\u00a9\5"+
		"\"\22\2\u00a8\u00a6\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa"+
		"\u00ab\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00a1\3\2"+
		"\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b5\5\f\7\2\u00b0"+
		"\u00b1\5&\24\2\u00b1\u00b2\5\f\7\2\u00b2\u00b4\3\2\2\2\u00b3\u00b0\3\2"+
		"\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6"+
		"\13\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\5\16\b\2\u00b9\u00bb\5\20"+
		"\t\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc"+
		"\u00be\5\22\n\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3"+
		"\2\2\2\u00bf\u00c1\5\24\13\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1"+
		"\u00c3\3\2\2\2\u00c2\u00c4\5\26\f\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3"+
		"\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c7\5(\25\2\u00c6\u00c5\3\2\2\2\u00c6"+
		"\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00ca\5,\27\2\u00c9\u00c8\3\2"+
		"\2\2\u00c9\u00ca\3\2\2\2\u00ca\r\3\2\2\2\u00cb\u00cd\7G\2\2\u00cc\u00ce"+
		"\t\6\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf"+
		"\u00d4\5$\23\2\u00d0\u00d1\7\7\2\2\u00d1\u00d3\5$\23\2\u00d2\u00d0\3\2"+
		"\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5"+
		"\17\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7G\2\2\u00d8\u00d9\7L\2\2"+
		"\u00d9\u00da\5\6\4\2\u00da\21\3\2\2\2\u00db\u00e5\7-\2\2\u00dc\u00e1\5"+
		"\32\16\2\u00dd\u00de\7\7\2\2\u00de\u00e0\5\32\16\2\u00df\u00dd\3\2\2\2"+
		"\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e6"+
		"\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e6\5\30\r\2\u00e5\u00dc\3\2\2\2"+
		"\u00e5\u00e4\3\2\2\2\u00e6\23\3\2\2\2\u00e7\u00e8\7O\2\2\u00e8\u00e9\5"+
		"\6\4\2\u00e9\25\3\2\2\2\u00ea\u00eb\7/\2\2\u00eb\u00ec\7!\2\2\u00ec\u00f1"+
		"\5\b\5\2\u00ed\u00ee\7\7\2\2\u00ee\u00f0\5\b\5\2\u00ef\u00ed\3\2\2\2\u00f0"+
		"\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f6\3\2"+
		"\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7\60\2\2\u00f5\u00f7\5\b\5\2\u00f6"+
		"\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\27\3\2\2\2\u00f8\u0100\5\32\16"+
		"\2\u00f9\u00fa\5\36\20\2\u00fa\u00fc\5\32\16\2\u00fb\u00fd\5 \21\2\u00fc"+
		"\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f9\3\2"+
		"\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101"+
		"\31\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0105\5\b\5\2\u0104\u0106\5\34\17"+
		"\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\33\3\2\2\2\u0107\u0109"+
		"\7\36\2\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3\2\2\2"+
		"\u010a\u0115\7X\2\2\u010b\u010c\7\5\2\2\u010c\u0111\7X\2\2\u010d\u010e"+
		"\7\7\2\2\u010e\u0110\7X\2\2\u010f\u010d\3\2\2\2\u0110\u0113\3\2\2\2\u0111"+
		"\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2"+
		"\2\2\u0114\u0116\7\6\2\2\u0115\u010b\3\2\2\2\u0115\u0116\3\2\2\2\u0116"+
		"\35\3\2\2\2\u0117\u0125\7\7\2\2\u0118\u011a\7;\2\2\u0119\u0118\3\2\2\2"+
		"\u0119\u011a\3\2\2\2\u011a\u0121\3\2\2\2\u011b\u011d\7\67\2\2\u011c\u011e"+
		"\7C\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0122\3\2\2\2\u011f"+
		"\u0122\7\62\2\2\u0120\u0122\7$\2\2\u0121\u011b\3\2\2\2\u0121\u011f\3\2"+
		"\2\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123"+
		"\u0125\7\66\2\2\u0124\u0117\3\2\2\2\u0124\u0119\3\2\2\2\u0125\37\3\2\2"+
		"\2\u0126\u0127\7@\2\2\u0127\u0134\5\b\5\2\u0128\u0129\7K\2\2\u0129\u012a"+
		"\7\5\2\2\u012a\u012f\7X\2\2\u012b\u012c\7\7\2\2\u012c\u012e\7X\2\2\u012d"+
		"\u012b\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2"+
		"\2\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0134\7\6\2\2\u0133"+
		"\u0126\3\2\2\2\u0133\u0128\3\2\2\2\u0134!\3\2\2\2\u0135\u0140\7X\2\2\u0136"+
		"\u0137\7\5\2\2\u0137\u013c\7X\2\2\u0138\u0139\7\7\2\2\u0139\u013b\7X\2"+
		"\2\u013a\u0138\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d"+
		"\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\7\6\2\2\u0140"+
		"\u0136\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\7\36"+
		"\2\2\u0143\u0144\7\5\2\2\u0144\u0145\5\n\6\2\u0145\u0146\7\6\2\2\u0146"+
		"#\3\2\2\2\u0147\u0153\7\t\2\2\u0148\u0149\7X\2\2\u0149\u014a\7\4\2\2\u014a"+
		"\u0153\7\t\2\2\u014b\u0150\5\6\4\2\u014c\u014e\7\36\2\2\u014d\u014c\3"+
		"\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\7X\2\2\u0150"+
		"\u014d\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0147\3\2"+
		"\2\2\u0152\u0148\3\2\2\2\u0152\u014b\3\2\2\2\u0153%\3\2\2\2\u0154\u015a"+
		"\7I\2\2\u0155\u0156\7I\2\2\u0156\u015a\7\34\2\2\u0157\u015a\7\63\2\2\u0158"+
		"\u015a\7+\2\2\u0159\u0154\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0157\3\2"+
		"\2\2\u0159\u0158\3\2\2\2\u015a\'\3\2\2\2\u015b\u015c\7B\2\2\u015c\u015d"+
		"\7!\2\2\u015d\u0162\5*\26\2\u015e\u015f\7\7\2\2\u015f\u0161\5*\26\2\u0160"+
		"\u015e\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2"+
		"\2\2\u0163)\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0167\5\b\5\2\u0166\u0168"+
		"\t\7\2\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168+\3\2\2\2\u0169"+
		"\u016a\79\2\2\u016a\u016d\5\b\5\2\u016b\u016c\t\b\2\2\u016c\u016e\5\b"+
		"\5\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e-\3\2\2\2\u016f\u0171"+
		"\7X\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172"+
		"\u0173\3\2\2\2\u0173\u017e\3\2\2\2\u0174\u0175\7\5\2\2\u0175\u0176\5\60"+
		"\31\2\u0176\u0177\7\6\2\2\u0177\u017f\3\2\2\2\u0178\u0179\7\5\2\2\u0179"+
		"\u017a\5\60\31\2\u017a\u017b\7\7\2\2\u017b\u017c\5\60\31\2\u017c\u017d"+
		"\7\6\2\2\u017d\u017f\3\2\2\2\u017e\u0174\3\2\2\2\u017e\u0178\3\2\2\2\u017e"+
		"\u017f\3\2\2\2\u017f/\3\2\2\2\u0180\u0182\t\5\2\2\u0181\u0180\3\2\2\2"+
		"\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\7Y\2\2\u0184\61\3"+
		"\2\2\2\u0185\u0186\t\t\2\2\u0186\63\3\2\2\289HO]bgoq~\u0082\u008a\u0094"+
		"\u009c\u009e\u00a3\u00aa\u00ad\u00b5\u00ba\u00bd\u00c0\u00c3\u00c6\u00c9"+
		"\u00cd\u00d4\u00e1\u00e5\u00f1\u00f6\u00fc\u0100\u0105\u0108\u0111\u0115"+
		"\u0119\u011d\u0121\u0124\u012f\u0133\u013c\u0140\u014d\u0150\u0152\u0159"+
		"\u0162\u0167\u016d\u0172\u017e\u0181";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}