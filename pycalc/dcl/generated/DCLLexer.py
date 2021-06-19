from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2b")
        buf.write("\u0326\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3D\3D\3")
        buf.write("D\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3J\3J\3")
        buf.write("J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3")
        buf.write("S\3S\3S\3S\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3V\3V\3V\3")
        buf.write("V\3W\3W\3W\3W\3W\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Y\3Z\3Z\3Z\3[\3[\7[\u0294\n[\f[\16[\u0297\13[\3\\\6")
        buf.write("\\\u029a\n\\\r\\\16\\\u029b\3\\\3\\\7\\\u02a0\n\\\f\\")
        buf.write("\16\\\u02a3\13\\\5\\\u02a5\n\\\3\\\3\\\5\\\u02a9\n\\\3")
        buf.write("\\\6\\\u02ac\n\\\r\\\16\\\u02ad\5\\\u02b0\n\\\3\\\3\\")
        buf.write("\6\\\u02b4\n\\\r\\\16\\\u02b5\3\\\3\\\5\\\u02ba\n\\\3")
        buf.write("\\\6\\\u02bd\n\\\r\\\16\\\u02be\5\\\u02c1\n\\\5\\\u02c3")
        buf.write("\n\\\3]\3]\3]\3]\7]\u02c9\n]\f]\16]\u02cc\13]\3]\3]\3")
        buf.write("^\3^\3^\3^\7^\u02d4\n^\f^\16^\u02d7\13^\3^\3^\3_\3_\3")
        buf.write("_\3_\7_\u02df\n_\f_\16_\u02e2\13_\3_\3_\3_\5_\u02e7\n")
        buf.write("_\3_\3_\3`\3`\3`\3`\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3")
        buf.write("f\3g\3g\3h\3h\3i\3i\3j\3j\3k\3k\3l\3l\3m\3m\3n\3n\3o\3")
        buf.write("o\3p\3p\3q\3q\3r\3r\3s\3s\3t\3t\3u\3u\3v\3v\3w\3w\3x\3")
        buf.write("x\3y\3y\3z\3z\3{\3{\3|\3|\3\u02e0\2}\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1")
        buf.write("Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1")
        buf.write("\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cf")
        buf.write("\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db\2\u00dd")
        buf.write("\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\u00e7\2\u00e9\2\u00eb")
        buf.write("\2\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5\2\u00f7b\3\2")
        buf.write("#\5\2C\\aac|\6\2\62;C\\aac|\4\2--//\3\2))\4\2\f\f\17\17")
        buf.write("\5\2\13\r\17\17\"\"\3\2\62;\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\2\u031b\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00f7\3\2\2\2\3\u00f9\3\2\2")
        buf.write("\2\5\u00fc\3\2\2\2\7\u00fe\3\2\2\2\t\u0101\3\2\2\2\13")
        buf.write("\u0103\3\2\2\2\r\u0105\3\2\2\2\17\u0107\3\2\2\2\21\u0109")
        buf.write("\3\2\2\2\23\u010b\3\2\2\2\25\u010d\3\2\2\2\27\u0110\3")
        buf.write("\2\2\2\31\u0112\3\2\2\2\33\u0114\3\2\2\2\35\u0116\3\2")
        buf.write("\2\2\37\u0118\3\2\2\2!\u011b\3\2\2\2#\u011d\3\2\2\2%\u011f")
        buf.write("\3\2\2\2\'\u0122\3\2\2\2)\u0125\3\2\2\2+\u0127\3\2\2\2")
        buf.write("-\u0129\3\2\2\2/\u012b\3\2\2\2\61\u012e\3\2\2\2\63\u0130")
        buf.write("\3\2\2\2\65\u0133\3\2\2\2\67\u0135\3\2\2\29\u0138\3\2")
        buf.write("\2\2;\u013b\3\2\2\2=\u013e\3\2\2\2?\u0142\3\2\2\2A\u0146")
        buf.write("\3\2\2\2C\u0149\3\2\2\2E\u014d\3\2\2\2G\u0155\3\2\2\2")
        buf.write("I\u0158\3\2\2\2K\u015d\3\2\2\2M\u0162\3\2\2\2O\u0168\3")
        buf.write("\2\2\2Q\u016d\3\2\2\2S\u0176\3\2\2\2U\u017b\3\2\2\2W\u0180")
        buf.write("\3\2\2\2Y\u0184\3\2\2\2[\u018b\3\2\2\2]\u0192\3\2\2\2")
        buf.write("_\u019a\3\2\2\2a\u019f\3\2\2\2c\u01a4\3\2\2\2e\u01aa\3")
        buf.write("\2\2\2g\u01b1\3\2\2\2i\u01b4\3\2\2\2k\u01ba\3\2\2\2m\u01c4")
        buf.write("\3\2\2\2o\u01c7\3\2\2\2q\u01ce\3\2\2\2s\u01d3\3\2\2\2")
        buf.write("u\u01d8\3\2\2\2w\u01dd\3\2\2\2y\u01e3\3\2\2\2{\u01e9\3")
        buf.write("\2\2\2}\u01f1\3\2\2\2\177\u01f5\3\2\2\2\u0081\u01fd\3")
        buf.write("\2\2\2\u0083\u0202\3\2\2\2\u0085\u0209\3\2\2\2\u0087\u020c")
        buf.write("\3\2\2\2\u0089\u020f\3\2\2\2\u008b\u0215\3\2\2\2\u008d")
        buf.write("\u021b\3\2\2\2\u008f\u0225\3\2\2\2\u0091\u022c\3\2\2\2")
        buf.write("\u0093\u0230\3\2\2\2\u0095\u0237\3\2\2\2\u0097\u023c\3")
        buf.write("\2\2\2\u0099\u0242\3\2\2\2\u009b\u0249\3\2\2\2\u009d\u024f")
        buf.write("\3\2\2\2\u009f\u0255\3\2\2\2\u00a1\u025c\3\2\2\2\u00a3")
        buf.write("\u0261\3\2\2\2\u00a5\u0267\3\2\2\2\u00a7\u026c\3\2\2\2")
        buf.write("\u00a9\u0271\3\2\2\2\u00ab\u0277\3\2\2\2\u00ad\u027b\3")
        buf.write("\2\2\2\u00af\u0280\3\2\2\2\u00b1\u0287\3\2\2\2\u00b3\u028e")
        buf.write("\3\2\2\2\u00b5\u0291\3\2\2\2\u00b7\u02c2\3\2\2\2\u00b9")
        buf.write("\u02c4\3\2\2\2\u00bb\u02cf\3\2\2\2\u00bd\u02da\3\2\2\2")
        buf.write("\u00bf\u02ea\3\2\2\2\u00c1\u02ee\3\2\2\2\u00c3\u02f0\3")
        buf.write("\2\2\2\u00c5\u02f2\3\2\2\2\u00c7\u02f4\3\2\2\2\u00c9\u02f6")
        buf.write("\3\2\2\2\u00cb\u02f8\3\2\2\2\u00cd\u02fa\3\2\2\2\u00cf")
        buf.write("\u02fc\3\2\2\2\u00d1\u02fe\3\2\2\2\u00d3\u0300\3\2\2\2")
        buf.write("\u00d5\u0302\3\2\2\2\u00d7\u0304\3\2\2\2\u00d9\u0306\3")
        buf.write("\2\2\2\u00db\u0308\3\2\2\2\u00dd\u030a\3\2\2\2\u00df\u030c")
        buf.write("\3\2\2\2\u00e1\u030e\3\2\2\2\u00e3\u0310\3\2\2\2\u00e5")
        buf.write("\u0312\3\2\2\2\u00e7\u0314\3\2\2\2\u00e9\u0316\3\2\2\2")
        buf.write("\u00eb\u0318\3\2\2\2\u00ed\u031a\3\2\2\2\u00ef\u031c\3")
        buf.write("\2\2\2\u00f1\u031e\3\2\2\2\u00f3\u0320\3\2\2\2\u00f5\u0322")
        buf.write("\3\2\2\2\u00f7\u0324\3\2\2\2\u00f9\u00fa\7/\2\2\u00fa")
        buf.write("\u00fb\7@\2\2\u00fb\4\3\2\2\2\u00fc\u00fd\7<\2\2\u00fd")
        buf.write("\6\3\2\2\2\u00fe\u00ff\7]\2\2\u00ff\u0100\7<\2\2\u0100")
        buf.write("\b\3\2\2\2\u0101\u0102\7_\2\2\u0102\n\3\2\2\2\u0103\u0104")
        buf.write("\7=\2\2\u0104\f\3\2\2\2\u0105\u0106\7\60\2\2\u0106\16")
        buf.write("\3\2\2\2\u0107\u0108\7*\2\2\u0108\20\3\2\2\2\u0109\u010a")
        buf.write("\7+\2\2\u010a\22\3\2\2\2\u010b\u010c\7.\2\2\u010c\24\3")
        buf.write("\2\2\2\u010d\u010e\7<\2\2\u010e\u010f\7?\2\2\u010f\26")
        buf.write("\3\2\2\2\u0110\u0111\7,\2\2\u0111\30\3\2\2\2\u0112\u0113")
        buf.write("\7-\2\2\u0113\32\3\2\2\2\u0114\u0115\7/\2\2\u0115\34\3")
        buf.write("\2\2\2\u0116\u0117\7\u0080\2\2\u0117\36\3\2\2\2\u0118")
        buf.write("\u0119\7~\2\2\u0119\u011a\7~\2\2\u011a \3\2\2\2\u011b")
        buf.write("\u011c\7\61\2\2\u011c\"\3\2\2\2\u011d\u011e\7\'\2\2\u011e")
        buf.write("$\3\2\2\2\u011f\u0120\7>\2\2\u0120\u0121\7>\2\2\u0121")
        buf.write("&\3\2\2\2\u0122\u0123\7@\2\2\u0123\u0124\7@\2\2\u0124")
        buf.write("(\3\2\2\2\u0125\u0126\7(\2\2\u0126*\3\2\2\2\u0127\u0128")
        buf.write("\7~\2\2\u0128,\3\2\2\2\u0129\u012a\7>\2\2\u012a.\3\2\2")
        buf.write("\2\u012b\u012c\7>\2\2\u012c\u012d\7?\2\2\u012d\60\3\2")
        buf.write("\2\2\u012e\u012f\7@\2\2\u012f\62\3\2\2\2\u0130\u0131\7")
        buf.write("@\2\2\u0131\u0132\7?\2\2\u0132\64\3\2\2\2\u0133\u0134")
        buf.write("\7?\2\2\u0134\66\3\2\2\2\u0135\u0136\7?\2\2\u0136\u0137")
        buf.write("\7?\2\2\u01378\3\2\2\2\u0138\u0139\7#\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a:\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d")
        buf.write("\7@\2\2\u013d<\3\2\2\2\u013e\u013f\5\u00c3b\2\u013f\u0140")
        buf.write("\5\u00d9m\2\u0140\u0141\5\u00d9m\2\u0141>\3\2\2\2\u0142")
        buf.write("\u0143\5\u00c3b\2\u0143\u0144\5\u00ddo\2\u0144\u0145\5")
        buf.write("\u00c9e\2\u0145@\3\2\2\2\u0146\u0147\5\u00c3b\2\u0147")
        buf.write("\u0148\5\u00e7t\2\u0148B\3\2\2\2\u0149\u014a\5\u00c3b")
        buf.write("\2\u014a\u014b\5\u00e7t\2\u014b\u014c\5\u00c7d\2\u014c")
        buf.write("D\3\2\2\2\u014d\u014e\5\u00c5c\2\u014e\u014f\5\u00cbf")
        buf.write("\2\u014f\u0150\5\u00e9u\2\u0150\u0151\5\u00efx\2\u0151")
        buf.write("\u0152\5\u00cbf\2\u0152\u0153\5\u00cbf\2\u0153\u0154\5")
        buf.write("\u00ddo\2\u0154F\3\2\2\2\u0155\u0156\5\u00c5c\2\u0156")
        buf.write("\u0157\5\u00f3z\2\u0157H\3\2\2\2\u0158\u0159\5\u00c7d")
        buf.write("\2\u0159\u015a\5\u00c3b\2\u015a\u015b\5\u00e7t\2\u015b")
        buf.write("\u015c\5\u00cbf\2\u015cJ\3\2\2\2\u015d\u015e\5\u00c7d")
        buf.write("\2\u015e\u015f\5\u00c3b\2\u015f\u0160\5\u00e7t\2\u0160")
        buf.write("\u0161\5\u00e9u\2\u0161L\3\2\2\2\u0162\u0163\5\u00c7d")
        buf.write("\2\u0163\u0164\5\u00e5s\2\u0164\u0165\5\u00dfp\2\u0165")
        buf.write("\u0166\5\u00e7t\2\u0166\u0167\5\u00e7t\2\u0167N\3\2\2")
        buf.write("\2\u0168\u0169\5\u00c9e\2\u0169\u016a\5\u00cbf\2\u016a")
        buf.write("\u016b\5\u00e7t\2\u016b\u016c\5\u00c7d\2\u016cP\3\2\2")
        buf.write("\2\u016d\u016e\5\u00c9e\2\u016e\u016f\5\u00d3j\2\u016f")
        buf.write("\u0170\5\u00e7t\2\u0170\u0171\5\u00e9u\2\u0171\u0172\5")
        buf.write("\u00d3j\2\u0172\u0173\5\u00ddo\2\u0173\u0174\5\u00c7d")
        buf.write("\2\u0174\u0175\5\u00e9u\2\u0175R\3\2\2\2\u0176\u0177\5")
        buf.write("\u00c9e\2\u0177\u0178\5\u00e5s\2\u0178\u0179\5\u00dfp")
        buf.write("\2\u0179\u017a\5\u00e1q\2\u017aT\3\2\2\2\u017b\u017c\5")
        buf.write("\u00cbf\2\u017c\u017d\5\u00d9m\2\u017d\u017e\5\u00e7t")
        buf.write("\2\u017e\u017f\5\u00cbf\2\u017fV\3\2\2\2\u0180\u0181\5")
        buf.write("\u00cbf\2\u0181\u0182\5\u00ddo\2\u0182\u0183\5\u00c9e")
        buf.write("\2\u0183X\3\2\2\2\u0184\u0185\5\u00cbf\2\u0185\u0186\5")
        buf.write("\u00e7t\2\u0186\u0187\5\u00c7d\2\u0187\u0188\5\u00c3b")
        buf.write("\2\u0188\u0189\5\u00e1q\2\u0189\u018a\5\u00cbf\2\u018a")
        buf.write("Z\3\2\2\2\u018b\u018c\5\u00cbf\2\u018c\u018d\5\u00f1y")
        buf.write("\2\u018d\u018e\5\u00c7d\2\u018e\u018f\5\u00cbf\2\u018f")
        buf.write("\u0190\5\u00e1q\2\u0190\u0191\5\u00e9u\2\u0191\\\3\2\2")
        buf.write("\2\u0192\u0193\5\u00cbf\2\u0193\u0194\5\u00f1y\2\u0194")
        buf.write("\u0195\5\u00e9u\2\u0195\u0196\5\u00e5s\2\u0196\u0197\5")
        buf.write("\u00c3b\2\u0197\u0198\5\u00c7d\2\u0198\u0199\5\u00e9u")
        buf.write("\2\u0199^\3\2\2\2\u019a\u019b\5\u00cdg\2\u019b\u019c\5")
        buf.write("\u00e5s\2\u019c\u019d\5\u00dfp\2\u019d\u019e\5\u00dbn")
        buf.write("\2\u019e`\3\2\2\2\u019f\u01a0\5\u00cfh\2\u01a0\u01a1\5")
        buf.write("\u00d9m\2\u01a1\u01a2\5\u00dfp\2\u01a2\u01a3\5\u00c5c")
        buf.write("\2\u01a3b\3\2\2\2\u01a4\u01a5\5\u00cfh\2\u01a5\u01a6\5")
        buf.write("\u00e5s\2\u01a6\u01a7\5\u00dfp\2\u01a7\u01a8\5\u00ebv")
        buf.write("\2\u01a8\u01a9\5\u00e1q\2\u01a9d\3\2\2\2\u01aa\u01ab\5")
        buf.write("\u00d1i\2\u01ab\u01ac\5\u00c3b\2\u01ac\u01ad\5\u00edw")
        buf.write("\2\u01ad\u01ae\5\u00d3j\2\u01ae\u01af\5\u00ddo\2\u01af")
        buf.write("\u01b0\5\u00cfh\2\u01b0f\3\2\2\2\u01b1\u01b2\5\u00d3j")
        buf.write("\2\u01b2\u01b3\5\u00ddo\2\u01b3h\3\2\2\2\u01b4\u01b5\5")
        buf.write("\u00d3j\2\u01b5\u01b6\5\u00ddo\2\u01b6\u01b7\5\u00ddo")
        buf.write("\2\u01b7\u01b8\5\u00cbf\2\u01b8\u01b9\5\u00e5s\2\u01b9")
        buf.write("j\3\2\2\2\u01ba\u01bb\5\u00d3j\2\u01bb\u01bc\5\u00ddo")
        buf.write("\2\u01bc\u01bd\5\u00e9u\2\u01bd\u01be\5\u00cbf\2\u01be")
        buf.write("\u01bf\5\u00e5s\2\u01bf\u01c0\5\u00e7t\2\u01c0\u01c1\5")
        buf.write("\u00cbf\2\u01c1\u01c2\5\u00c7d\2\u01c2\u01c3\5\u00e9u")
        buf.write("\2\u01c3l\3\2\2\2\u01c4\u01c5\5\u00d3j\2\u01c5\u01c6\5")
        buf.write("\u00e7t\2\u01c6n\3\2\2\2\u01c7\u01c8\5\u00d3j\2\u01c8")
        buf.write("\u01c9\5\u00e7t\2\u01c9\u01ca\5\u00ddo\2\u01ca\u01cb\5")
        buf.write("\u00ebv\2\u01cb\u01cc\5\u00d9m\2\u01cc\u01cd\5\u00d9m")
        buf.write("\2\u01cdp\3\2\2\2\u01ce\u01cf\5\u00d5k\2\u01cf\u01d0\5")
        buf.write("\u00dfp\2\u01d0\u01d1\5\u00d3j\2\u01d1\u01d2\5\u00ddo")
        buf.write("\2\u01d2r\3\2\2\2\u01d3\u01d4\5\u00d9m\2\u01d4\u01d5\5")
        buf.write("\u00cbf\2\u01d5\u01d6\5\u00cdg\2\u01d6\u01d7\5\u00e9u")
        buf.write("\2\u01d7t\3\2\2\2\u01d8\u01d9\5\u00d9m\2\u01d9\u01da\5")
        buf.write("\u00d3j\2\u01da\u01db\5\u00d7l\2\u01db\u01dc\5\u00cbf")
        buf.write("\2\u01dcv\3\2\2\2\u01dd\u01de\5\u00d9m\2\u01de\u01df\5")
        buf.write("\u00d3j\2\u01df\u01e0\5\u00dbn\2\u01e0\u01e1\5\u00d3j")
        buf.write("\2\u01e1\u01e2\5\u00e9u\2\u01e2x\3\2\2\2\u01e3\u01e4\5")
        buf.write("\u00dbn\2\u01e4\u01e5\5\u00c3b\2\u01e5\u01e6\5\u00e9u")
        buf.write("\2\u01e6\u01e7\5\u00c7d\2\u01e7\u01e8\5\u00d1i\2\u01e8")
        buf.write("z\3\2\2\2\u01e9\u01ea\5\u00ddo\2\u01ea\u01eb\5\u00c3b")
        buf.write("\2\u01eb\u01ec\5\u00e9u\2\u01ec\u01ed\5\u00ebv\2\u01ed")
        buf.write("\u01ee\5\u00e5s\2\u01ee\u01ef\5\u00c3b\2\u01ef\u01f0\5")
        buf.write("\u00d9m\2\u01f0|\3\2\2\2\u01f1\u01f2\5\u00ddo\2\u01f2")
        buf.write("\u01f3\5\u00dfp\2\u01f3\u01f4\5\u00e9u\2\u01f4~\3\2\2")
        buf.write("\2\u01f5\u01f6\5\u00ddo\2\u01f6\u01f7\5\u00dfp\2\u01f7")
        buf.write("\u01f8\5\u00e9u\2\u01f8\u01f9\5\u00ddo\2\u01f9\u01fa\5")
        buf.write("\u00ebv\2\u01fa\u01fb\5\u00d9m\2\u01fb\u01fc\5\u00d9m")
        buf.write("\2\u01fc\u0080\3\2\2\2\u01fd\u01fe\5\u00ddo\2\u01fe\u01ff")
        buf.write("\5\u00ebv\2\u01ff\u0200\5\u00d9m\2\u0200\u0201\5\u00d9")
        buf.write("m\2\u0201\u0082\3\2\2\2\u0202\u0203\5\u00dfp\2\u0203\u0204")
        buf.write("\5\u00cdg\2\u0204\u0205\5\u00cdg\2\u0205\u0206\5\u00e7")
        buf.write("t\2\u0206\u0207\5\u00cbf\2\u0207\u0208\5\u00e9u\2\u0208")
        buf.write("\u0084\3\2\2\2\u0209\u020a\5\u00dfp\2\u020a\u020b\5\u00dd")
        buf.write("o\2\u020b\u0086\3\2\2\2\u020c\u020d\5\u00dfp\2\u020d\u020e")
        buf.write("\5\u00e5s\2\u020e\u0088\3\2\2\2\u020f\u0210\5\u00dfp\2")
        buf.write("\u0210\u0211\5\u00e5s\2\u0211\u0212\5\u00c9e\2\u0212\u0213")
        buf.write("\5\u00cbf\2\u0213\u0214\5\u00e5s\2\u0214\u008a\3\2\2\2")
        buf.write("\u0215\u0216\5\u00dfp\2\u0216\u0217\5\u00ebv\2\u0217\u0218")
        buf.write("\5\u00e9u\2\u0218\u0219\5\u00cbf\2\u0219\u021a\5\u00e5")
        buf.write("s\2\u021a\u008c\3\2\2\2\u021b\u021c\5\u00e5s\2\u021c\u021d")
        buf.write("\5\u00cbf\2\u021d\u021e\5\u00c7d\2\u021e\u021f\5\u00eb")
        buf.write("v\2\u021f\u0220\5\u00e5s\2\u0220\u0221\5\u00e7t\2\u0221")
        buf.write("\u0222\5\u00d3j\2\u0222\u0223\5\u00edw\2\u0223\u0224\5")
        buf.write("\u00cbf\2\u0224\u008e\3\2\2\2\u0225\u0226\5\u00e5s\2\u0226")
        buf.write("\u0227\5\u00cbf\2\u0227\u0228\5\u00cfh\2\u0228\u0229\5")
        buf.write("\u00cbf\2\u0229\u022a\5\u00f1y\2\u022a\u022b\5\u00e1q")
        buf.write("\2\u022b\u0090\3\2\2\2\u022c\u022d\5\u00e5s\2\u022d\u022e")
        buf.write("\5\u00dfp\2\u022e\u022f\5\u00efx\2\u022f\u0092\3\2\2\2")
        buf.write("\u0230\u0231\5\u00e7t\2\u0231\u0232\5\u00cbf\2\u0232\u0233")
        buf.write("\5\u00d9m\2\u0233\u0234\5\u00cbf\2\u0234\u0235\5\u00c7")
        buf.write("d\2\u0235\u0236\5\u00e9u\2\u0236\u0094\3\2\2\2\u0237\u0238")
        buf.write("\5\u00e9u\2\u0238\u0239\5\u00d1i\2\u0239\u023a\5\u00cb")
        buf.write("f\2\u023a\u023b\5\u00ddo\2\u023b\u0096\3\2\2\2\u023c\u023d")
        buf.write("\5\u00ebv\2\u023d\u023e\5\u00ddo\2\u023e\u023f\5\u00d3")
        buf.write("j\2\u023f\u0240\5\u00dfp\2\u0240\u0241\5\u00ddo\2\u0241")
        buf.write("\u0098\3\2\2\2\u0242\u0243\5\u00ebv\2\u0243\u0244\5\u00dd")
        buf.write("o\2\u0244\u0245\5\u00d3j\2\u0245\u0246\5\u00e3r\2\u0246")
        buf.write("\u0247\5\u00ebv\2\u0247\u0248\5\u00cbf\2\u0248\u009a\3")
        buf.write("\2\2\2\u0249\u024a\5\u00ebv\2\u024a\u024b\5\u00e7t\2\u024b")
        buf.write("\u024c\5\u00d3j\2\u024c\u024d\5\u00ddo\2\u024d\u024e\5")
        buf.write("\u00cfh\2\u024e\u009c\3\2\2\2\u024f\u0250\5\u00edw\2\u0250")
        buf.write("\u0251\5\u00c3b\2\u0251\u0252\5\u00d9m\2\u0252\u0253\5")
        buf.write("\u00ebv\2\u0253\u0254\5\u00cbf\2\u0254\u009e\3\2\2\2\u0255")
        buf.write("\u0256\5\u00edw\2\u0256\u0257\5\u00c3b\2\u0257\u0258\5")
        buf.write("\u00d9m\2\u0258\u0259\5\u00ebv\2\u0259\u025a\5\u00cbf")
        buf.write("\2\u025a\u025b\5\u00e7t\2\u025b\u00a0\3\2\2\2\u025c\u025d")
        buf.write("\5\u00efx\2\u025d\u025e\5\u00d1i\2\u025e\u025f\5\u00cb")
        buf.write("f\2\u025f\u0260\5\u00ddo\2\u0260\u00a2\3\2\2\2\u0261\u0262")
        buf.write("\5\u00efx\2\u0262\u0263\5\u00d1i\2\u0263\u0264\5\u00cb")
        buf.write("f\2\u0264\u0265\5\u00e5s\2\u0265\u0266\5\u00cbf\2\u0266")
        buf.write("\u00a4\3\2\2\2\u0267\u0268\5\u00efx\2\u0268\u0269\5\u00d3")
        buf.write("j\2\u0269\u026a\5\u00e9u\2\u026a\u026b\5\u00d1i\2\u026b")
        buf.write("\u00a6\3\2\2\2\u026c\u026d\5\u00f3z\2\u026d\u026e\5\u00cb")
        buf.write("f\2\u026e\u026f\5\u00c3b\2\u026f\u0270\5\u00e5s\2\u0270")
        buf.write("\u00a8\3\2\2\2\u0271\u0272\5\u00dbn\2\u0272\u0273\5\u00df")
        buf.write("p\2\u0273\u0274\5\u00ddo\2\u0274\u0275\5\u00e9u\2\u0275")
        buf.write("\u0276\5\u00d1i\2\u0276\u00aa\3\2\2\2\u0277\u0278\5\u00c9")
        buf.write("e\2\u0278\u0279\5\u00c3b\2\u0279\u027a\5\u00f3z\2\u027a")
        buf.write("\u00ac\3\2\2\2\u027b\u027c\5\u00d1i\2\u027c\u027d\5\u00df")
        buf.write("p\2\u027d\u027e\5\u00ebv\2\u027e\u027f\5\u00e5s\2\u027f")
        buf.write("\u00ae\3\2\2\2\u0280\u0281\5\u00dbn\2\u0281\u0282\5\u00d3")
        buf.write("j\2\u0282\u0283\5\u00ddo\2\u0283\u0284\5\u00ebv\2\u0284")
        buf.write("\u0285\5\u00e9u\2\u0285\u0286\5\u00cbf\2\u0286\u00b0\3")
        buf.write("\2\2\2\u0287\u0288\5\u00e7t\2\u0288\u0289\5\u00cbf\2\u0289")
        buf.write("\u028a\5\u00c7d\2\u028a\u028b\5\u00dfp\2\u028b\u028c\5")
        buf.write("\u00ddo\2\u028c\u028d\5\u00c9e\2\u028d\u00b2\3\2\2\2\u028e")
        buf.write("\u028f\7B\2\2\u028f\u0290\5\u00b5[\2\u0290\u00b4\3\2\2")
        buf.write("\2\u0291\u0295\t\2\2\2\u0292\u0294\t\3\2\2\u0293\u0292")
        buf.write("\3\2\2\2\u0294\u0297\3\2\2\2\u0295\u0293\3\2\2\2\u0295")
        buf.write("\u0296\3\2\2\2\u0296\u00b6\3\2\2\2\u0297\u0295\3\2\2\2")
        buf.write("\u0298\u029a\5\u00c1a\2\u0299\u0298\3\2\2\2\u029a\u029b")
        buf.write("\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029c\3\2\2\2\u029c")
        buf.write("\u02a4\3\2\2\2\u029d\u02a1\7\60\2\2\u029e\u02a0\5\u00c1")
        buf.write("a\2\u029f\u029e\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1\u029f")
        buf.write("\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a5\3\2\2\2\u02a3")
        buf.write("\u02a1\3\2\2\2\u02a4\u029d\3\2\2\2\u02a4\u02a5\3\2\2\2")
        buf.write("\u02a5\u02af\3\2\2\2\u02a6\u02a8\5\u00cbf\2\u02a7\u02a9")
        buf.write("\t\4\2\2\u02a8\u02a7\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9")
        buf.write("\u02ab\3\2\2\2\u02aa\u02ac\5\u00c1a\2\u02ab\u02aa\3\2")
        buf.write("\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae")
        buf.write("\3\2\2\2\u02ae\u02b0\3\2\2\2\u02af\u02a6\3\2\2\2\u02af")
        buf.write("\u02b0\3\2\2\2\u02b0\u02c3\3\2\2\2\u02b1\u02b3\7\60\2")
        buf.write("\2\u02b2\u02b4\5\u00c1a\2\u02b3\u02b2\3\2\2\2\u02b4\u02b5")
        buf.write("\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6")
        buf.write("\u02c0\3\2\2\2\u02b7\u02b9\5\u00cbf\2\u02b8\u02ba\t\4")
        buf.write("\2\2\u02b9\u02b8\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02bc")
        buf.write("\3\2\2\2\u02bb\u02bd\5\u00c1a\2\u02bc\u02bb\3\2\2\2\u02bd")
        buf.write("\u02be\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf\3\2\2\2")
        buf.write("\u02bf\u02c1\3\2\2\2\u02c0\u02b7\3\2\2\2\u02c0\u02c1\3")
        buf.write("\2\2\2\u02c1\u02c3\3\2\2\2\u02c2\u0299\3\2\2\2\u02c2\u02b1")
        buf.write("\3\2\2\2\u02c3\u00b8\3\2\2\2\u02c4\u02ca\7)\2\2\u02c5")
        buf.write("\u02c9\n\5\2\2\u02c6\u02c7\7)\2\2\u02c7\u02c9\7)\2\2\u02c8")
        buf.write("\u02c5\3\2\2\2\u02c8\u02c6\3\2\2\2\u02c9\u02cc\3\2\2\2")
        buf.write("\u02ca\u02c8\3\2\2\2\u02ca\u02cb\3\2\2\2\u02cb\u02cd\3")
        buf.write("\2\2\2\u02cc\u02ca\3\2\2\2\u02cd\u02ce\7)\2\2\u02ce\u00ba")
        buf.write("\3\2\2\2\u02cf\u02d0\7/\2\2\u02d0\u02d1\7/\2\2\u02d1\u02d5")
        buf.write("\3\2\2\2\u02d2\u02d4\n\6\2\2\u02d3\u02d2\3\2\2\2\u02d4")
        buf.write("\u02d7\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2")
        buf.write("\u02d6\u02d8\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02d9\b")
        buf.write("^\2\2\u02d9\u00bc\3\2\2\2\u02da\u02db\7\61\2\2\u02db\u02dc")
        buf.write("\7,\2\2\u02dc\u02e0\3\2\2\2\u02dd\u02df\13\2\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u02e2\3\2\2\2\u02e0\u02e1\3\2\2\2")
        buf.write("\u02e0\u02de\3\2\2\2\u02e1\u02e6\3\2\2\2\u02e2\u02e0\3")
        buf.write("\2\2\2\u02e3\u02e4\7,\2\2\u02e4\u02e7\7\61\2\2\u02e5\u02e7")
        buf.write("\7\2\2\3\u02e6\u02e3\3\2\2\2\u02e6\u02e5\3\2\2\2\u02e7")
        buf.write("\u02e8\3\2\2\2\u02e8\u02e9\b_\2\2\u02e9\u00be\3\2\2\2")
        buf.write("\u02ea\u02eb\t\7\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ed\b")
        buf.write("`\2\2\u02ed\u00c0\3\2\2\2\u02ee\u02ef\t\b\2\2\u02ef\u00c2")
        buf.write("\3\2\2\2\u02f0\u02f1\t\t\2\2\u02f1\u00c4\3\2\2\2\u02f2")
        buf.write("\u02f3\t\n\2\2\u02f3\u00c6\3\2\2\2\u02f4\u02f5\t\13\2")
        buf.write("\2\u02f5\u00c8\3\2\2\2\u02f6\u02f7\t\f\2\2\u02f7\u00ca")
        buf.write("\3\2\2\2\u02f8\u02f9\t\r\2\2\u02f9\u00cc\3\2\2\2\u02fa")
        buf.write("\u02fb\t\16\2\2\u02fb\u00ce\3\2\2\2\u02fc\u02fd\t\17\2")
        buf.write("\2\u02fd\u00d0\3\2\2\2\u02fe\u02ff\t\20\2\2\u02ff\u00d2")
        buf.write("\3\2\2\2\u0300\u0301\t\21\2\2\u0301\u00d4\3\2\2\2\u0302")
        buf.write("\u0303\t\22\2\2\u0303\u00d6\3\2\2\2\u0304\u0305\t\23\2")
        buf.write("\2\u0305\u00d8\3\2\2\2\u0306\u0307\t\24\2\2\u0307\u00da")
        buf.write("\3\2\2\2\u0308\u0309\t\25\2\2\u0309\u00dc\3\2\2\2\u030a")
        buf.write("\u030b\t\26\2\2\u030b\u00de\3\2\2\2\u030c\u030d\t\27\2")
        buf.write("\2\u030d\u00e0\3\2\2\2\u030e\u030f\t\30\2\2\u030f\u00e2")
        buf.write("\3\2\2\2\u0310\u0311\t\31\2\2\u0311\u00e4\3\2\2\2\u0312")
        buf.write("\u0313\t\32\2\2\u0313\u00e6\3\2\2\2\u0314\u0315\t\33\2")
        buf.write("\2\u0315\u00e8\3\2\2\2\u0316\u0317\t\34\2\2\u0317\u00ea")
        buf.write("\3\2\2\2\u0318\u0319\t\35\2\2\u0319\u00ec\3\2\2\2\u031a")
        buf.write("\u031b\t\36\2\2\u031b\u00ee\3\2\2\2\u031c\u031d\t\37\2")
        buf.write("\2\u031d\u00f0\3\2\2\2\u031e\u031f\t \2\2\u031f\u00f2")
        buf.write("\3\2\2\2\u0320\u0321\t!\2\2\u0321\u00f4\3\2\2\2\u0322")
        buf.write("\u0323\t\"\2\2\u0323\u00f6\3\2\2\2\u0324\u0325\13\2\2")
        buf.write("\2\u0325\u00f8\3\2\2\2\24\2\u0295\u029b\u02a1\u02a4\u02a8")
        buf.write("\u02ad\u02af\u02b5\u02b9\u02be\u02c0\u02c2\u02c8\u02ca")
        buf.write("\u02d5\u02e0\u02e6\3\2\3\2")
        return buf.getvalue()


class DCLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SCOL = 5
    DOT = 6
    OPEN_PAR = 7
    CLOSE_PAR = 8
    COMMA = 9
    ASSIGN = 10
    STAR = 11
    PLUS = 12
    MINUS = 13
    TILDE = 14
    PIPE2 = 15
    DIV = 16
    MOD = 17
    LT2 = 18
    GT2 = 19
    AMP = 20
    PIPE = 21
    LT = 22
    LT_EQ = 23
    GT = 24
    GT_EQ = 25
    EQ1 = 26
    EQ2 = 27
    NOT_EQ1 = 28
    NOT_EQ2 = 29
    K_ALL = 30
    K_AND = 31
    K_AS = 32
    K_ASC = 33
    K_BETWEEN = 34
    K_BY = 35
    K_CASE = 36
    K_CAST = 37
    K_CROSS = 38
    K_DESC = 39
    K_DISTINCT = 40
    K_DROP = 41
    K_ELSE = 42
    K_END = 43
    K_ESCAPE = 44
    K_EXCEPT = 45
    K_EXTRACT = 46
    K_FROM = 47
    K_GLOB = 48
    K_GROUP = 49
    K_HAVING = 50
    K_IN = 51
    K_INNER = 52
    K_INTERSECT = 53
    K_IS = 54
    K_ISNULL = 55
    K_JOIN = 56
    K_LEFT = 57
    K_LIKE = 58
    K_LIMIT = 59
    K_MATCH = 60
    K_NATURAL = 61
    K_NOT = 62
    K_NOTNULL = 63
    K_NULL = 64
    K_OFFSET = 65
    K_ON = 66
    K_OR = 67
    K_ORDER = 68
    K_OUTER = 69
    K_RECURSIVE = 70
    K_REGEXP = 71
    K_ROW = 72
    K_SELECT = 73
    K_THEN = 74
    K_UNION = 75
    K_UNIQUE = 76
    K_USING = 77
    K_VALUE = 78
    K_VALUES = 79
    K_WHEN = 80
    K_WHERE = 81
    K_WITH = 82
    K_YEAR = 83
    K_MONTH = 84
    K_DAY = 85
    K_HOUR = 86
    K_MINUTE = 87
    K_SECOND = 88
    LET_IDENT = 89
    IDENT = 90
    NUMERIC_LITERAL = 91
    STRING_LITERAL = 92
    SINGLE_LINE_COMMENT = 93
    MULTILINE_COMMENT = 94
    SPACES = 95
    ERROR = 96

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "':'", "'[:'", "']'", "';'", "'.'", "'('", "')'", "','", 
            "':='", "'*'", "'+'", "'-'", "'~'", "'||'", "'/'", "'%'", "'<<'", 
            "'>>'", "'&'", "'|'", "'<'", "'<='", "'>'", "'>='", "'='", "'=='", 
            "'!='", "'<>'" ]

    symbolicNames = [ "<INVALID>",
            "SCOL", "DOT", "OPEN_PAR", "CLOSE_PAR", "COMMA", "ASSIGN", "STAR", 
            "PLUS", "MINUS", "TILDE", "PIPE2", "DIV", "MOD", "LT2", "GT2", 
            "AMP", "PIPE", "LT", "LT_EQ", "GT", "GT_EQ", "EQ1", "EQ2", "NOT_EQ1", 
            "NOT_EQ2", "K_ALL", "K_AND", "K_AS", "K_ASC", "K_BETWEEN", "K_BY", 
            "K_CASE", "K_CAST", "K_CROSS", "K_DESC", "K_DISTINCT", "K_DROP", 
            "K_ELSE", "K_END", "K_ESCAPE", "K_EXCEPT", "K_EXTRACT", "K_FROM", 
            "K_GLOB", "K_GROUP", "K_HAVING", "K_IN", "K_INNER", "K_INTERSECT", 
            "K_IS", "K_ISNULL", "K_JOIN", "K_LEFT", "K_LIKE", "K_LIMIT", 
            "K_MATCH", "K_NATURAL", "K_NOT", "K_NOTNULL", "K_NULL", "K_OFFSET", 
            "K_ON", "K_OR", "K_ORDER", "K_OUTER", "K_RECURSIVE", "K_REGEXP", 
            "K_ROW", "K_SELECT", "K_THEN", "K_UNION", "K_UNIQUE", "K_USING", 
            "K_VALUE", "K_VALUES", "K_WHEN", "K_WHERE", "K_WITH", "K_YEAR", 
            "K_MONTH", "K_DAY", "K_HOUR", "K_MINUTE", "K_SECOND", "LET_IDENT", 
            "IDENT", "NUMERIC_LITERAL", "STRING_LITERAL", "SINGLE_LINE_COMMENT", 
            "MULTILINE_COMMENT", "SPACES", "ERROR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SCOL", "DOT", "OPEN_PAR", 
                  "CLOSE_PAR", "COMMA", "ASSIGN", "STAR", "PLUS", "MINUS", 
                  "TILDE", "PIPE2", "DIV", "MOD", "LT2", "GT2", "AMP", "PIPE", 
                  "LT", "LT_EQ", "GT", "GT_EQ", "EQ1", "EQ2", "NOT_EQ1", 
                  "NOT_EQ2", "K_ALL", "K_AND", "K_AS", "K_ASC", "K_BETWEEN", 
                  "K_BY", "K_CASE", "K_CAST", "K_CROSS", "K_DESC", "K_DISTINCT", 
                  "K_DROP", "K_ELSE", "K_END", "K_ESCAPE", "K_EXCEPT", "K_EXTRACT", 
                  "K_FROM", "K_GLOB", "K_GROUP", "K_HAVING", "K_IN", "K_INNER", 
                  "K_INTERSECT", "K_IS", "K_ISNULL", "K_JOIN", "K_LEFT", 
                  "K_LIKE", "K_LIMIT", "K_MATCH", "K_NATURAL", "K_NOT", 
                  "K_NOTNULL", "K_NULL", "K_OFFSET", "K_ON", "K_OR", "K_ORDER", 
                  "K_OUTER", "K_RECURSIVE", "K_REGEXP", "K_ROW", "K_SELECT", 
                  "K_THEN", "K_UNION", "K_UNIQUE", "K_USING", "K_VALUE", 
                  "K_VALUES", "K_WHEN", "K_WHERE", "K_WITH", "K_YEAR", "K_MONTH", 
                  "K_DAY", "K_HOUR", "K_MINUTE", "K_SECOND", "LET_IDENT", 
                  "IDENT", "NUMERIC_LITERAL", "STRING_LITERAL", "SINGLE_LINE_COMMENT", 
                  "MULTILINE_COMMENT", "SPACES", "DIGIT", "A", "B", "C", 
                  "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                  "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", 
                  "Z", "ERROR" ]

    grammarFileName = "DCL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


