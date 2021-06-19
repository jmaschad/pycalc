import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DCLLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SCOL", "DOT", "OPEN_PAR", "CLOSE_PAR", "COMMA", "ASSIGN", "STAR", "PLUS", 
			"MINUS", "TILDE", "PIPE2", "DIV", "MOD", "LT2", "GT2", "AMP", "PIPE", 
			"LT", "LT_EQ", "GT", "GT_EQ", "EQ1", "EQ2", "NOT_EQ1", "NOT_EQ2", "K_ALL", 
			"K_AND", "K_AS", "K_ASC", "K_BETWEEN", "K_BY", "K_CASE", "K_CAST", "K_CROSS", 
			"K_DESC", "K_DISTINCT", "K_DROP", "K_ELSE", "K_END", "K_ESCAPE", "K_EXCEPT", 
			"K_EXTRACT", "K_FROM", "K_GLOB", "K_GROUP", "K_HAVING", "K_IN", "K_INNER", 
			"K_INTERSECT", "K_IS", "K_ISNULL", "K_JOIN", "K_LEFT", "K_LIKE", "K_LIMIT", 
			"K_MATCH", "K_NATURAL", "K_NOT", "K_NOTNULL", "K_NULL", "K_OFFSET", "K_ON", 
			"K_OR", "K_ORDER", "K_OUTER", "K_RECURSIVE", "K_REGEXP", "K_ROW", "K_SELECT", 
			"K_THEN", "K_UNION", "K_UNIQUE", "K_USING", "K_VALUE", "K_VALUES", "K_WHEN", 
			"K_WHERE", "K_WITH", "K_YEAR", "K_MONTH", "K_DAY", "K_HOUR", "K_MINUTE", 
			"K_SECOND", "LET_IDENT", "IDENT", "NUMERIC_LITERAL", "STRING_LITERAL", 
			"SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", "DIGIT", "A", "B", 
			"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
			"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ERROR"
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


	public DCLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "DCL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2^\u0314\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\t"+
		"k\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4"+
		"w\tw\4x\tx\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b"+
		"\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32"+
		"\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!"+
		"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3"+
		"%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)"+
		"\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,"+
		"\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60"+
		"\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62"+
		"\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65"+
		"\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\3"+
		"8\38\38\38\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3"+
		"<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3"+
		"@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3"+
		"C\3C\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3"+
		"G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3J\3K\3K\3"+
		"K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3O\3"+
		"O\3O\3O\3O\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3S\3"+
		"S\3T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3U\3V\3V\3V\3W\3W\7W\u0282\n"+
		"W\fW\16W\u0285\13W\3X\6X\u0288\nX\rX\16X\u0289\3X\3X\7X\u028e\nX\fX\16"+
		"X\u0291\13X\5X\u0293\nX\3X\3X\5X\u0297\nX\3X\6X\u029a\nX\rX\16X\u029b"+
		"\5X\u029e\nX\3X\3X\6X\u02a2\nX\rX\16X\u02a3\3X\3X\5X\u02a8\nX\3X\6X\u02ab"+
		"\nX\rX\16X\u02ac\5X\u02af\nX\5X\u02b1\nX\3Y\3Y\3Y\3Y\7Y\u02b7\nY\fY\16"+
		"Y\u02ba\13Y\3Y\3Y\3Z\3Z\3Z\3Z\7Z\u02c2\nZ\fZ\16Z\u02c5\13Z\3Z\3Z\3[\3"+
		"[\3[\3[\7[\u02cd\n[\f[\16[\u02d0\13[\3[\3[\3[\5[\u02d5\n[\3[\3[\3\\\3"+
		"\\\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3"+
		"f\3g\3g\3h\3h\3i\3i\3j\3j\3k\3k\3l\3l\3m\3m\3n\3n\3o\3o\3p\3p\3q\3q\3"+
		"r\3r\3s\3s\3t\3t\3u\3u\3v\3v\3w\3w\3x\3x\3\u02ce\2y\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'"+
		"\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'"+
		"M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177"+
		"A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093"+
		"K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7"+
		"U\u00a9V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9\2\u00bb"+
		"\2\u00bd\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd"+
		"\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df"+
		"\2\u00e1\2\u00e3\2\u00e5\2\u00e7\2\u00e9\2\u00eb\2\u00ed\2\u00ef^\3\2"+
		"#\5\2C\\aac|\6\2\62;C\\aac|\4\2--//\3\2))\4\2\f\f\17\17\5\2\13\r\17\17"+
		"\"\"\3\2\62;\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4"+
		"\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr"+
		"r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2"+
		"[[{{\4\2\\\\||\2\u0309\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2"+
		"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2"+
		"\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2"+
		"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3"+
		"\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2"+
		"\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2"+
		"w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2"+
		"\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b"+
		"\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2"+
		"\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d"+
		"\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2"+
		"\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af"+
		"\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2"+
		"\2\2\u00ef\3\2\2\2\3\u00f1\3\2\2\2\5\u00f3\3\2\2\2\7\u00f5\3\2\2\2\t\u00f7"+
		"\3\2\2\2\13\u00f9\3\2\2\2\r\u00fb\3\2\2\2\17\u00fe\3\2\2\2\21\u0100\3"+
		"\2\2\2\23\u0102\3\2\2\2\25\u0104\3\2\2\2\27\u0106\3\2\2\2\31\u0109\3\2"+
		"\2\2\33\u010b\3\2\2\2\35\u010d\3\2\2\2\37\u0110\3\2\2\2!\u0113\3\2\2\2"+
		"#\u0115\3\2\2\2%\u0117\3\2\2\2\'\u0119\3\2\2\2)\u011c\3\2\2\2+\u011e\3"+
		"\2\2\2-\u0121\3\2\2\2/\u0123\3\2\2\2\61\u0126\3\2\2\2\63\u0129\3\2\2\2"+
		"\65\u012c\3\2\2\2\67\u0130\3\2\2\29\u0134\3\2\2\2;\u0137\3\2\2\2=\u013b"+
		"\3\2\2\2?\u0143\3\2\2\2A\u0146\3\2\2\2C\u014b\3\2\2\2E\u0150\3\2\2\2G"+
		"\u0156\3\2\2\2I\u015b\3\2\2\2K\u0164\3\2\2\2M\u0169\3\2\2\2O\u016e\3\2"+
		"\2\2Q\u0172\3\2\2\2S\u0179\3\2\2\2U\u0180\3\2\2\2W\u0188\3\2\2\2Y\u018d"+
		"\3\2\2\2[\u0192\3\2\2\2]\u0198\3\2\2\2_\u019f\3\2\2\2a\u01a2\3\2\2\2c"+
		"\u01a8\3\2\2\2e\u01b2\3\2\2\2g\u01b5\3\2\2\2i\u01bc\3\2\2\2k\u01c1\3\2"+
		"\2\2m\u01c6\3\2\2\2o\u01cb\3\2\2\2q\u01d1\3\2\2\2s\u01d7\3\2\2\2u\u01df"+
		"\3\2\2\2w\u01e3\3\2\2\2y\u01eb\3\2\2\2{\u01f0\3\2\2\2}\u01f7\3\2\2\2\177"+
		"\u01fa\3\2\2\2\u0081\u01fd\3\2\2\2\u0083\u0203\3\2\2\2\u0085\u0209\3\2"+
		"\2\2\u0087\u0213\3\2\2\2\u0089\u021a\3\2\2\2\u008b\u021e\3\2\2\2\u008d"+
		"\u0225\3\2\2\2\u008f\u022a\3\2\2\2\u0091\u0230\3\2\2\2\u0093\u0237\3\2"+
		"\2\2\u0095\u023d\3\2\2\2\u0097\u0243\3\2\2\2\u0099\u024a\3\2\2\2\u009b"+
		"\u024f\3\2\2\2\u009d\u0255\3\2\2\2\u009f\u025a\3\2\2\2\u00a1\u025f\3\2"+
		"\2\2\u00a3\u0265\3\2\2\2\u00a5\u0269\3\2\2\2\u00a7\u026e\3\2\2\2\u00a9"+
		"\u0275\3\2\2\2\u00ab\u027c\3\2\2\2\u00ad\u027f\3\2\2\2\u00af\u02b0\3\2"+
		"\2\2\u00b1\u02b2\3\2\2\2\u00b3\u02bd\3\2\2\2\u00b5\u02c8\3\2\2\2\u00b7"+
		"\u02d8\3\2\2\2\u00b9\u02dc\3\2\2\2\u00bb\u02de\3\2\2\2\u00bd\u02e0\3\2"+
		"\2\2\u00bf\u02e2\3\2\2\2\u00c1\u02e4\3\2\2\2\u00c3\u02e6\3\2\2\2\u00c5"+
		"\u02e8\3\2\2\2\u00c7\u02ea\3\2\2\2\u00c9\u02ec\3\2\2\2\u00cb\u02ee\3\2"+
		"\2\2\u00cd\u02f0\3\2\2\2\u00cf\u02f2\3\2\2\2\u00d1\u02f4\3\2\2\2\u00d3"+
		"\u02f6\3\2\2\2\u00d5\u02f8\3\2\2\2\u00d7\u02fa\3\2\2\2\u00d9\u02fc\3\2"+
		"\2\2\u00db\u02fe\3\2\2\2\u00dd\u0300\3\2\2\2\u00df\u0302\3\2\2\2\u00e1"+
		"\u0304\3\2\2\2\u00e3\u0306\3\2\2\2\u00e5\u0308\3\2\2\2\u00e7\u030a\3\2"+
		"\2\2\u00e9\u030c\3\2\2\2\u00eb\u030e\3\2\2\2\u00ed\u0310\3\2\2\2\u00ef"+
		"\u0312\3\2\2\2\u00f1\u00f2\7=\2\2\u00f2\4\3\2\2\2\u00f3\u00f4\7\60\2\2"+
		"\u00f4\6\3\2\2\2\u00f5\u00f6\7*\2\2\u00f6\b\3\2\2\2\u00f7\u00f8\7+\2\2"+
		"\u00f8\n\3\2\2\2\u00f9\u00fa\7.\2\2\u00fa\f\3\2\2\2\u00fb\u00fc\7<\2\2"+
		"\u00fc\u00fd\7?\2\2\u00fd\16\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\20\3\2\2"+
		"\2\u0100\u0101\7-\2\2\u0101\22\3\2\2\2\u0102\u0103\7/\2\2\u0103\24\3\2"+
		"\2\2\u0104\u0105\7\u0080\2\2\u0105\26\3\2\2\2\u0106\u0107\7~\2\2\u0107"+
		"\u0108\7~\2\2\u0108\30\3\2\2\2\u0109\u010a\7\61\2\2\u010a\32\3\2\2\2\u010b"+
		"\u010c\7\'\2\2\u010c\34\3\2\2\2\u010d\u010e\7>\2\2\u010e\u010f\7>\2\2"+
		"\u010f\36\3\2\2\2\u0110\u0111\7@\2\2\u0111\u0112\7@\2\2\u0112 \3\2\2\2"+
		"\u0113\u0114\7(\2\2\u0114\"\3\2\2\2\u0115\u0116\7~\2\2\u0116$\3\2\2\2"+
		"\u0117\u0118\7>\2\2\u0118&\3\2\2\2\u0119\u011a\7>\2\2\u011a\u011b\7?\2"+
		"\2\u011b(\3\2\2\2\u011c\u011d\7@\2\2\u011d*\3\2\2\2\u011e\u011f\7@\2\2"+
		"\u011f\u0120\7?\2\2\u0120,\3\2\2\2\u0121\u0122\7?\2\2\u0122.\3\2\2\2\u0123"+
		"\u0124\7?\2\2\u0124\u0125\7?\2\2\u0125\60\3\2\2\2\u0126\u0127\7#\2\2\u0127"+
		"\u0128\7?\2\2\u0128\62\3\2\2\2\u0129\u012a\7>\2\2\u012a\u012b\7@\2\2\u012b"+
		"\64\3\2\2\2\u012c\u012d\5\u00bb^\2\u012d\u012e\5\u00d1i\2\u012e\u012f"+
		"\5\u00d1i\2\u012f\66\3\2\2\2\u0130\u0131\5\u00bb^\2\u0131\u0132\5\u00d5"+
		"k\2\u0132\u0133\5\u00c1a\2\u01338\3\2\2\2\u0134\u0135\5\u00bb^\2\u0135"+
		"\u0136\5\u00dfp\2\u0136:\3\2\2\2\u0137\u0138\5\u00bb^\2\u0138\u0139\5"+
		"\u00dfp\2\u0139\u013a\5\u00bf`\2\u013a<\3\2\2\2\u013b\u013c\5\u00bd_\2"+
		"\u013c\u013d\5\u00c3b\2\u013d\u013e\5\u00e1q\2\u013e\u013f\5\u00e7t\2"+
		"\u013f\u0140\5\u00c3b\2\u0140\u0141\5\u00c3b\2\u0141\u0142\5\u00d5k\2"+
		"\u0142>\3\2\2\2\u0143\u0144\5\u00bd_\2\u0144\u0145\5\u00ebv\2\u0145@\3"+
		"\2\2\2\u0146\u0147\5\u00bf`\2\u0147\u0148\5\u00bb^\2\u0148\u0149\5\u00df"+
		"p\2\u0149\u014a\5\u00c3b\2\u014aB\3\2\2\2\u014b\u014c\5\u00bf`\2\u014c"+
		"\u014d\5\u00bb^\2\u014d\u014e\5\u00dfp\2\u014e\u014f\5\u00e1q\2\u014f"+
		"D\3\2\2\2\u0150\u0151\5\u00bf`\2\u0151\u0152\5\u00ddo\2\u0152\u0153\5"+
		"\u00d7l\2\u0153\u0154\5\u00dfp\2\u0154\u0155\5\u00dfp\2\u0155F\3\2\2\2"+
		"\u0156\u0157\5\u00c1a\2\u0157\u0158\5\u00c3b\2\u0158\u0159\5\u00dfp\2"+
		"\u0159\u015a\5\u00bf`\2\u015aH\3\2\2\2\u015b\u015c\5\u00c1a\2\u015c\u015d"+
		"\5\u00cbf\2\u015d\u015e\5\u00dfp\2\u015e\u015f\5\u00e1q\2\u015f\u0160"+
		"\5\u00cbf\2\u0160\u0161\5\u00d5k\2\u0161\u0162\5\u00bf`\2\u0162\u0163"+
		"\5\u00e1q\2\u0163J\3\2\2\2\u0164\u0165\5\u00c1a\2\u0165\u0166\5\u00dd"+
		"o\2\u0166\u0167\5\u00d7l\2\u0167\u0168\5\u00d9m\2\u0168L\3\2\2\2\u0169"+
		"\u016a\5\u00c3b\2\u016a\u016b\5\u00d1i\2\u016b\u016c\5\u00dfp\2\u016c"+
		"\u016d\5\u00c3b\2\u016dN\3\2\2\2\u016e\u016f\5\u00c3b\2\u016f\u0170\5"+
		"\u00d5k\2\u0170\u0171\5\u00c1a\2\u0171P\3\2\2\2\u0172\u0173\5\u00c3b\2"+
		"\u0173\u0174\5\u00dfp\2\u0174\u0175\5\u00bf`\2\u0175\u0176\5\u00bb^\2"+
		"\u0176\u0177\5\u00d9m\2\u0177\u0178\5\u00c3b\2\u0178R\3\2\2\2\u0179\u017a"+
		"\5\u00c3b\2\u017a\u017b\5\u00e9u\2\u017b\u017c\5\u00bf`\2\u017c\u017d"+
		"\5\u00c3b\2\u017d\u017e\5\u00d9m\2\u017e\u017f\5\u00e1q\2\u017fT\3\2\2"+
		"\2\u0180\u0181\5\u00c3b\2\u0181\u0182\5\u00e9u\2\u0182\u0183\5\u00e1q"+
		"\2\u0183\u0184\5\u00ddo\2\u0184\u0185\5\u00bb^\2\u0185\u0186\5\u00bf`"+
		"\2\u0186\u0187\5\u00e1q\2\u0187V\3\2\2\2\u0188\u0189\5\u00c5c\2\u0189"+
		"\u018a\5\u00ddo\2\u018a\u018b\5\u00d7l\2\u018b\u018c\5\u00d3j\2\u018c"+
		"X\3\2\2\2\u018d\u018e\5\u00c7d\2\u018e\u018f\5\u00d1i\2\u018f\u0190\5"+
		"\u00d7l\2\u0190\u0191\5\u00bd_\2\u0191Z\3\2\2\2\u0192\u0193\5\u00c7d\2"+
		"\u0193\u0194\5\u00ddo\2\u0194\u0195\5\u00d7l\2\u0195\u0196\5\u00e3r\2"+
		"\u0196\u0197\5\u00d9m\2\u0197\\\3\2\2\2\u0198\u0199\5\u00c9e\2\u0199\u019a"+
		"\5\u00bb^\2\u019a\u019b\5\u00e5s\2\u019b\u019c\5\u00cbf\2\u019c\u019d"+
		"\5\u00d5k\2\u019d\u019e\5\u00c7d\2\u019e^\3\2\2\2\u019f\u01a0\5\u00cb"+
		"f\2\u01a0\u01a1\5\u00d5k\2\u01a1`\3\2\2\2\u01a2\u01a3\5\u00cbf\2\u01a3"+
		"\u01a4\5\u00d5k\2\u01a4\u01a5\5\u00d5k\2\u01a5\u01a6\5\u00c3b\2\u01a6"+
		"\u01a7\5\u00ddo\2\u01a7b\3\2\2\2\u01a8\u01a9\5\u00cbf\2\u01a9\u01aa\5"+
		"\u00d5k\2\u01aa\u01ab\5\u00e1q\2\u01ab\u01ac\5\u00c3b\2\u01ac\u01ad\5"+
		"\u00ddo\2\u01ad\u01ae\5\u00dfp\2\u01ae\u01af\5\u00c3b\2\u01af\u01b0\5"+
		"\u00bf`\2\u01b0\u01b1\5\u00e1q\2\u01b1d\3\2\2\2\u01b2\u01b3\5\u00cbf\2"+
		"\u01b3\u01b4\5\u00dfp\2\u01b4f\3\2\2\2\u01b5\u01b6\5\u00cbf\2\u01b6\u01b7"+
		"\5\u00dfp\2\u01b7\u01b8\5\u00d5k\2\u01b8\u01b9\5\u00e3r\2\u01b9\u01ba"+
		"\5\u00d1i\2\u01ba\u01bb\5\u00d1i\2\u01bbh\3\2\2\2\u01bc\u01bd\5\u00cd"+
		"g\2\u01bd\u01be\5\u00d7l\2\u01be\u01bf\5\u00cbf\2\u01bf\u01c0\5\u00d5"+
		"k\2\u01c0j\3\2\2\2\u01c1\u01c2\5\u00d1i\2\u01c2\u01c3\5\u00c3b\2\u01c3"+
		"\u01c4\5\u00c5c\2\u01c4\u01c5\5\u00e1q\2\u01c5l\3\2\2\2\u01c6\u01c7\5"+
		"\u00d1i\2\u01c7\u01c8\5\u00cbf\2\u01c8\u01c9\5\u00cfh\2\u01c9\u01ca\5"+
		"\u00c3b\2\u01can\3\2\2\2\u01cb\u01cc\5\u00d1i\2\u01cc\u01cd\5\u00cbf\2"+
		"\u01cd\u01ce\5\u00d3j\2\u01ce\u01cf\5\u00cbf\2\u01cf\u01d0\5\u00e1q\2"+
		"\u01d0p\3\2\2\2\u01d1\u01d2\5\u00d3j\2\u01d2\u01d3\5\u00bb^\2\u01d3\u01d4"+
		"\5\u00e1q\2\u01d4\u01d5\5\u00bf`\2\u01d5\u01d6\5\u00c9e\2\u01d6r\3\2\2"+
		"\2\u01d7\u01d8\5\u00d5k\2\u01d8\u01d9\5\u00bb^\2\u01d9\u01da\5\u00e1q"+
		"\2\u01da\u01db\5\u00e3r\2\u01db\u01dc\5\u00ddo\2\u01dc\u01dd\5\u00bb^"+
		"\2\u01dd\u01de\5\u00d1i\2\u01det\3\2\2\2\u01df\u01e0\5\u00d5k\2\u01e0"+
		"\u01e1\5\u00d7l\2\u01e1\u01e2\5\u00e1q\2\u01e2v\3\2\2\2\u01e3\u01e4\5"+
		"\u00d5k\2\u01e4\u01e5\5\u00d7l\2\u01e5\u01e6\5\u00e1q\2\u01e6\u01e7\5"+
		"\u00d5k\2\u01e7\u01e8\5\u00e3r\2\u01e8\u01e9\5\u00d1i\2\u01e9\u01ea\5"+
		"\u00d1i\2\u01eax\3\2\2\2\u01eb\u01ec\5\u00d5k\2\u01ec\u01ed\5\u00e3r\2"+
		"\u01ed\u01ee\5\u00d1i\2\u01ee\u01ef\5\u00d1i\2\u01efz\3\2\2\2\u01f0\u01f1"+
		"\5\u00d7l\2\u01f1\u01f2\5\u00c5c\2\u01f2\u01f3\5\u00c5c\2\u01f3\u01f4"+
		"\5\u00dfp\2\u01f4\u01f5\5\u00c3b\2\u01f5\u01f6\5\u00e1q\2\u01f6|\3\2\2"+
		"\2\u01f7\u01f8\5\u00d7l\2\u01f8\u01f9\5\u00d5k\2\u01f9~\3\2\2\2\u01fa"+
		"\u01fb\5\u00d7l\2\u01fb\u01fc\5\u00ddo\2\u01fc\u0080\3\2\2\2\u01fd\u01fe"+
		"\5\u00d7l\2\u01fe\u01ff\5\u00ddo\2\u01ff\u0200\5\u00c1a\2\u0200\u0201"+
		"\5\u00c3b\2\u0201\u0202\5\u00ddo\2\u0202\u0082\3\2\2\2\u0203\u0204\5\u00d7"+
		"l\2\u0204\u0205\5\u00e3r\2\u0205\u0206\5\u00e1q\2\u0206\u0207\5\u00c3"+
		"b\2\u0207\u0208\5\u00ddo\2\u0208\u0084\3\2\2\2\u0209\u020a\5\u00ddo\2"+
		"\u020a\u020b\5\u00c3b\2\u020b\u020c\5\u00bf`\2\u020c\u020d\5\u00e3r\2"+
		"\u020d\u020e\5\u00ddo\2\u020e\u020f\5\u00dfp\2\u020f\u0210\5\u00cbf\2"+
		"\u0210\u0211\5\u00e5s\2\u0211\u0212\5\u00c3b\2\u0212\u0086\3\2\2\2\u0213"+
		"\u0214\5\u00ddo\2\u0214\u0215\5\u00c3b\2\u0215\u0216\5\u00c7d\2\u0216"+
		"\u0217\5\u00c3b\2\u0217\u0218\5\u00e9u\2\u0218\u0219\5\u00d9m\2\u0219"+
		"\u0088\3\2\2\2\u021a\u021b\5\u00ddo\2\u021b\u021c\5\u00d7l\2\u021c\u021d"+
		"\5\u00e7t\2\u021d\u008a\3\2\2\2\u021e\u021f\5\u00dfp\2\u021f\u0220\5\u00c3"+
		"b\2\u0220\u0221\5\u00d1i\2\u0221\u0222\5\u00c3b\2\u0222\u0223\5\u00bf"+
		"`\2\u0223\u0224\5\u00e1q\2\u0224\u008c\3\2\2\2\u0225\u0226\5\u00e1q\2"+
		"\u0226\u0227\5\u00c9e\2\u0227\u0228\5\u00c3b\2\u0228\u0229\5\u00d5k\2"+
		"\u0229\u008e\3\2\2\2\u022a\u022b\5\u00e3r\2\u022b\u022c\5\u00d5k\2\u022c"+
		"\u022d\5\u00cbf\2\u022d\u022e\5\u00d7l\2\u022e\u022f\5\u00d5k\2\u022f"+
		"\u0090\3\2\2\2\u0230\u0231\5\u00e3r\2\u0231\u0232\5\u00d5k\2\u0232\u0233"+
		"\5\u00cbf\2\u0233\u0234\5\u00dbn\2\u0234\u0235\5\u00e3r\2\u0235\u0236"+
		"\5\u00c3b\2\u0236\u0092\3\2\2\2\u0237\u0238\5\u00e3r\2\u0238\u0239\5\u00df"+
		"p\2\u0239\u023a\5\u00cbf\2\u023a\u023b\5\u00d5k\2\u023b\u023c\5\u00c7"+
		"d\2\u023c\u0094\3\2\2\2\u023d\u023e\5\u00e5s\2\u023e\u023f\5\u00bb^\2"+
		"\u023f\u0240\5\u00d1i\2\u0240\u0241\5\u00e3r\2\u0241\u0242\5\u00c3b\2"+
		"\u0242\u0096\3\2\2\2\u0243\u0244\5\u00e5s\2\u0244\u0245\5\u00bb^\2\u0245"+
		"\u0246\5\u00d1i\2\u0246\u0247\5\u00e3r\2\u0247\u0248\5\u00c3b\2\u0248"+
		"\u0249\5\u00dfp\2\u0249\u0098\3\2\2\2\u024a\u024b\5\u00e7t\2\u024b\u024c"+
		"\5\u00c9e\2\u024c\u024d\5\u00c3b\2\u024d\u024e\5\u00d5k\2\u024e\u009a"+
		"\3\2\2\2\u024f\u0250\5\u00e7t\2\u0250\u0251\5\u00c9e\2\u0251\u0252\5\u00c3"+
		"b\2\u0252\u0253\5\u00ddo\2\u0253\u0254\5\u00c3b\2\u0254\u009c\3\2\2\2"+
		"\u0255\u0256\5\u00e7t\2\u0256\u0257\5\u00cbf\2\u0257\u0258\5\u00e1q\2"+
		"\u0258\u0259\5\u00c9e\2\u0259\u009e\3\2\2\2\u025a\u025b\5\u00ebv\2\u025b"+
		"\u025c\5\u00c3b\2\u025c\u025d\5\u00bb^\2\u025d\u025e\5\u00ddo\2\u025e"+
		"\u00a0\3\2\2\2\u025f\u0260\5\u00d3j\2\u0260\u0261\5\u00d7l\2\u0261\u0262"+
		"\5\u00d5k\2\u0262\u0263\5\u00e1q\2\u0263\u0264\5\u00c9e\2\u0264\u00a2"+
		"\3\2\2\2\u0265\u0266\5\u00c1a\2\u0266\u0267\5\u00bb^\2\u0267\u0268\5\u00eb"+
		"v\2\u0268\u00a4\3\2\2\2\u0269\u026a\5\u00c9e\2\u026a\u026b\5\u00d7l\2"+
		"\u026b\u026c\5\u00e3r\2\u026c\u026d\5\u00ddo\2\u026d\u00a6\3\2\2\2\u026e"+
		"\u026f\5\u00d3j\2\u026f\u0270\5\u00cbf\2\u0270\u0271\5\u00d5k\2\u0271"+
		"\u0272\5\u00e3r\2\u0272\u0273\5\u00e1q\2\u0273\u0274\5\u00c3b\2\u0274"+
		"\u00a8\3\2\2\2\u0275\u0276\5\u00dfp\2\u0276\u0277\5\u00c3b\2\u0277\u0278"+
		"\5\u00bf`\2\u0278\u0279\5\u00d7l\2\u0279\u027a\5\u00d5k\2\u027a\u027b"+
		"\5\u00c1a\2\u027b\u00aa\3\2\2\2\u027c\u027d\7B\2\2\u027d\u027e\5\u00ad"+
		"W\2\u027e\u00ac\3\2\2\2\u027f\u0283\t\2\2\2\u0280\u0282\t\3\2\2\u0281"+
		"\u0280\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284\3\2"+
		"\2\2\u0284\u00ae\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u0288\5\u00b9]\2\u0287"+
		"\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u028a\3\2"+
		"\2\2\u028a\u0292\3\2\2\2\u028b\u028f\7\60\2\2\u028c\u028e\5\u00b9]\2\u028d"+
		"\u028c\3\2\2\2\u028e\u0291\3\2\2\2\u028f\u028d\3\2\2\2\u028f\u0290\3\2"+
		"\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0292\u028b\3\2\2\2\u0292"+
		"\u0293\3\2\2\2\u0293\u029d\3\2\2\2\u0294\u0296\5\u00c3b\2\u0295\u0297"+
		"\t\4\2\2\u0296\u0295\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0299\3\2\2\2\u0298"+
		"\u029a\5\u00b9]\2\u0299\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u0299"+
		"\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u029e\3\2\2\2\u029d\u0294\3\2\2\2\u029d"+
		"\u029e\3\2\2\2\u029e\u02b1\3\2\2\2\u029f\u02a1\7\60\2\2\u02a0\u02a2\5"+
		"\u00b9]\2\u02a1\u02a0\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a1\3\2\2\2"+
		"\u02a3\u02a4\3\2\2\2\u02a4\u02ae\3\2\2\2\u02a5\u02a7\5\u00c3b\2\u02a6"+
		"\u02a8\t\4\2\2\u02a7\u02a6\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8\u02aa\3\2"+
		"\2\2\u02a9\u02ab\5\u00b9]\2\u02aa\u02a9\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac"+
		"\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02af\3\2\2\2\u02ae\u02a5\3\2"+
		"\2\2\u02ae\u02af\3\2\2\2\u02af\u02b1\3\2\2\2\u02b0\u0287\3\2\2\2\u02b0"+
		"\u029f\3\2\2\2\u02b1\u00b0\3\2\2\2\u02b2\u02b8\7)\2\2\u02b3\u02b7\n\5"+
		"\2\2\u02b4\u02b5\7)\2\2\u02b5\u02b7\7)\2\2\u02b6\u02b3\3\2\2\2\u02b6\u02b4"+
		"\3\2\2\2\u02b7\u02ba\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9"+
		"\u02bb\3\2\2\2\u02ba\u02b8\3\2\2\2\u02bb\u02bc\7)\2\2\u02bc\u00b2\3\2"+
		"\2\2\u02bd\u02be\7/\2\2\u02be\u02bf\7/\2\2\u02bf\u02c3\3\2\2\2\u02c0\u02c2"+
		"\n\6\2\2\u02c1\u02c0\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3"+
		"\u02c4\3\2\2\2\u02c4\u02c6\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c6\u02c7\bZ"+
		"\2\2\u02c7\u00b4\3\2\2\2\u02c8\u02c9\7\61\2\2\u02c9\u02ca\7,\2\2\u02ca"+
		"\u02ce\3\2\2\2\u02cb\u02cd\13\2\2\2\u02cc\u02cb\3\2\2\2\u02cd\u02d0\3"+
		"\2\2\2\u02ce\u02cf\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf\u02d4\3\2\2\2\u02d0"+
		"\u02ce\3\2\2\2\u02d1\u02d2\7,\2\2\u02d2\u02d5\7\61\2\2\u02d3\u02d5\7\2"+
		"\2\3\u02d4\u02d1\3\2\2\2\u02d4\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6"+
		"\u02d7\b[\2\2\u02d7\u00b6\3\2\2\2\u02d8\u02d9\t\7\2\2\u02d9\u02da\3\2"+
		"\2\2\u02da\u02db\b\\\2\2\u02db\u00b8\3\2\2\2\u02dc\u02dd\t\b\2\2\u02dd"+
		"\u00ba\3\2\2\2\u02de\u02df\t\t\2\2\u02df\u00bc\3\2\2\2\u02e0\u02e1\t\n"+
		"\2\2\u02e1\u00be\3\2\2\2\u02e2\u02e3\t\13\2\2\u02e3\u00c0\3\2\2\2\u02e4"+
		"\u02e5\t\f\2\2\u02e5\u00c2\3\2\2\2\u02e6\u02e7\t\r\2\2\u02e7\u00c4\3\2"+
		"\2\2\u02e8\u02e9\t\16\2\2\u02e9\u00c6\3\2\2\2\u02ea\u02eb\t\17\2\2\u02eb"+
		"\u00c8\3\2\2\2\u02ec\u02ed\t\20\2\2\u02ed\u00ca\3\2\2\2\u02ee\u02ef\t"+
		"\21\2\2\u02ef\u00cc\3\2\2\2\u02f0\u02f1\t\22\2\2\u02f1\u00ce\3\2\2\2\u02f2"+
		"\u02f3\t\23\2\2\u02f3\u00d0\3\2\2\2\u02f4\u02f5\t\24\2\2\u02f5\u00d2\3"+
		"\2\2\2\u02f6\u02f7\t\25\2\2\u02f7\u00d4\3\2\2\2\u02f8\u02f9\t\26\2\2\u02f9"+
		"\u00d6\3\2\2\2\u02fa\u02fb\t\27\2\2\u02fb\u00d8\3\2\2\2\u02fc\u02fd\t"+
		"\30\2\2\u02fd\u00da\3\2\2\2\u02fe\u02ff\t\31\2\2\u02ff\u00dc\3\2\2\2\u0300"+
		"\u0301\t\32\2\2\u0301\u00de\3\2\2\2\u0302\u0303\t\33\2\2\u0303\u00e0\3"+
		"\2\2\2\u0304\u0305\t\34\2\2\u0305\u00e2\3\2\2\2\u0306\u0307\t\35\2\2\u0307"+
		"\u00e4\3\2\2\2\u0308\u0309\t\36\2\2\u0309\u00e6\3\2\2\2\u030a\u030b\t"+
		"\37\2\2\u030b\u00e8\3\2\2\2\u030c\u030d\t \2\2\u030d\u00ea\3\2\2\2\u030e"+
		"\u030f\t!\2\2\u030f\u00ec\3\2\2\2\u0310\u0311\t\"\2\2\u0311\u00ee\3\2"+
		"\2\2\u0312\u0313\13\2\2\2\u0313\u00f0\3\2\2\2\24\2\u0283\u0289\u028f\u0292"+
		"\u0296\u029b\u029d\u02a3\u02a7\u02ac\u02ae\u02b0\u02b6\u02b8\u02c3\u02ce"+
		"\u02d4\3\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}