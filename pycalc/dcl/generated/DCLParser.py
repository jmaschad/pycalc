# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3b")
        buf.write("\u0199\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\3\3\3\5\3@\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4O\n\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("V\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4d\n\4\3\4\3\4\3\4\5\4i\n\4\3\4\3\4\3\4\5\4n\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4v\n\4\f\4\16\4y\13\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u0083\n\5\f\5\16\5\u0086")
        buf.write("\13\5\3\5\5\5\u0089\n\5\3\5\3\5\3\5\3\5\7\5\u008f\n\5")
        buf.write("\f\5\16\5\u0092\13\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009b")
        buf.write("\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u00a3\n\5\f\5\16\5\u00a6")
        buf.write("\13\5\3\6\3\6\3\6\3\6\7\6\u00ac\n\6\f\6\16\6\u00af\13")
        buf.write("\6\3\6\3\6\3\6\5\6\u00b4\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\7\b\u00c0\n\b\f\b\16\b\u00c3\13\b\3\t\3")
        buf.write("\t\3\t\5\t\u00c8\n\t\3\t\5\t\u00cb\n\t\3\t\5\t\u00ce\n")
        buf.write("\t\3\t\5\t\u00d1\n\t\3\n\3\n\5\n\u00d5\n\n\3\n\3\n\3\n")
        buf.write("\7\n\u00da\n\n\f\n\16\n\u00dd\13\n\3\13\3\13\3\13\3\13")
        buf.write("\7\13\u00e3\n\13\f\13\16\13\u00e6\13\13\3\13\5\13\u00e9")
        buf.write("\n\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00f1\n\13\f")
        buf.write("\13\16\13\u00f4\13\13\5\13\u00f6\n\13\3\f\3\f\3\f\5\f")
        buf.write("\u00fb\n\f\3\f\3\f\3\f\3\r\3\r\5\r\u0102\n\r\3\r\3\r\5")
        buf.write("\r\u0106\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u0116\n\20\f\20\16\20\u0119")
        buf.write("\13\20\3\20\3\20\5\20\u011d\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u0123\n\21\7\21\u0125\n\21\f\21\16\21\u0128\13\21")
        buf.write("\3\22\3\22\5\22\u012c\n\22\3\23\5\23\u012f\n\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u0136\n\23\f\23\16\23\u0139\13")
        buf.write("\23\3\23\5\23\u013c\n\23\3\24\3\24\5\24\u0140\n\24\3\24")
        buf.write("\3\24\5\24\u0144\n\24\3\24\3\24\5\24\u0148\n\24\3\24\5")
        buf.write("\24\u014b\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u0154\n\25\f\25\16\25\u0157\13\25\3\25\5\25\u015a\n\25")
        buf.write("\3\26\3\26\3\26\5\26\u015f\n\26\3\26\5\26\u0162\n\26\5")
        buf.write("\26\u0164\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u016b\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\7\30\u0172\n\30\f\30\16\30\u0175")
        buf.write("\13\30\3\31\3\31\5\31\u0179\n\31\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u017f\n\32\3\33\6\33\u0182\n\33\r\33\16\33\u0183\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0190\n\33\3\34\5\34\u0193\n\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\2\4\6\b\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668\2\n\3\2\30\33\3\2\34\37\4\2\\\\")
        buf.write("^^\4\2\r\r\22\23\3\2\16\17\4\2##))\4\2\13\13CC\6\2 /\61")
        buf.write("IKOQZ\2\u01c5\2:\3\2\2\2\4?\3\2\2\2\6m\3\2\2\2\b\u009a")
        buf.write("\3\2\2\2\n\u00b3\3\2\2\2\f\u00b5\3\2\2\2\16\u00bb\3\2")
        buf.write("\2\2\20\u00c4\3\2\2\2\22\u00d2\3\2\2\2\24\u00f5\3\2\2")
        buf.write("\2\26\u00f7\3\2\2\2\30\u00ff\3\2\2\2\32\u0109\3\2\2\2")
        buf.write("\34\u010d\3\2\2\2\36\u0110\3\2\2\2 \u011e\3\2\2\2\"\u0129")
        buf.write("\3\2\2\2$\u012e\3\2\2\2&\u014a\3\2\2\2(\u0159\3\2\2\2")
        buf.write("*\u0163\3\2\2\2,\u016a\3\2\2\2.\u016c\3\2\2\2\60\u0176")
        buf.write("\3\2\2\2\62\u017a\3\2\2\2\64\u0181\3\2\2\2\66\u0192\3")
        buf.write("\2\2\28\u0196\3\2\2\2:;\5\4\3\2;<\7\2\2\3<\3\3\2\2\2=")
        buf.write("@\5\n\6\2>@\5\6\4\2?=\3\2\2\2?>\3\2\2\2@\5\3\2\2\2AB\b")
        buf.write("\4\1\2BC\5\b\5\2CD\t\2\2\2DE\5\b\5\2En\3\2\2\2FG\5\b\5")
        buf.write("\2GH\t\3\2\2HI\5\b\5\2In\3\2\2\2JK\7@\2\2Kn\5\b\5\2LN")
        buf.write("\5\b\5\2MO\7@\2\2NM\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\7<\2")
        buf.write("\2QR\5\b\5\2Rn\3\2\2\2SU\5\b\5\2TV\7@\2\2UT\3\2\2\2UV")
        buf.write("\3\2\2\2VW\3\2\2\2WX\7$\2\2XY\5\b\5\2YZ\7!\2\2Z[\5\b\5")
        buf.write("\2[n\3\2\2\2\\c\5\b\5\2]d\79\2\2^_\78\2\2_d\7B\2\2`d\7")
        buf.write("A\2\2ab\7@\2\2bd\7B\2\2c]\3\2\2\2c^\3\2\2\2c`\3\2\2\2")
        buf.write("ca\3\2\2\2dn\3\2\2\2ef\5\b\5\2fh\78\2\2gi\7@\2\2hg\3\2")
        buf.write("\2\2hi\3\2\2\2ij\3\2\2\2jk\5\b\5\2kn\3\2\2\2ln\5\b\5\2")
        buf.write("mA\3\2\2\2mF\3\2\2\2mJ\3\2\2\2mL\3\2\2\2mS\3\2\2\2m\\")
        buf.write("\3\2\2\2me\3\2\2\2ml\3\2\2\2nw\3\2\2\2op\f\t\2\2pq\7!")
        buf.write("\2\2qv\5\6\4\nrs\f\b\2\2st\7E\2\2tv\5\6\4\tuo\3\2\2\2")
        buf.write("ur\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\7\3\2\2\2yw")
        buf.write("\3\2\2\2z{\b\5\1\2{|\7\17\2\2|\u009b\5\b\5\13}~\7\\\2")
        buf.write("\2~\u0088\7\t\2\2\177\u0084\5\4\3\2\u0080\u0081\7\13\2")
        buf.write("\2\u0081\u0083\5\4\3\2\u0082\u0080\3\2\2\2\u0083\u0086")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0089\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0089\7\r\2\2")
        buf.write("\u0088\177\3\2\2\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2")
        buf.write("\2\2\u0089\u008a\3\2\2\2\u008a\u009b\7\n\2\2\u008b\u0090")
        buf.write("\7\\\2\2\u008c\u008d\7\b\2\2\u008d\u008f\t\4\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u009b\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0093\u009b\7B\2\2\u0094\u009b\7]\2\2\u0095\u009b")
        buf.write("\7^\2\2\u0096\u0097\7\t\2\2\u0097\u0098\5\4\3\2\u0098")
        buf.write("\u0099\7\n\2\2\u0099\u009b\3\2\2\2\u009az\3\2\2\2\u009a")
        buf.write("}\3\2\2\2\u009a\u008b\3\2\2\2\u009a\u0093\3\2\2\2\u009a")
        buf.write("\u0094\3\2\2\2\u009a\u0095\3\2\2\2\u009a\u0096\3\2\2\2")
        buf.write("\u009b\u00a4\3\2\2\2\u009c\u009d\f\n\2\2\u009d\u009e\t")
        buf.write("\5\2\2\u009e\u00a3\5\b\5\13\u009f\u00a0\f\t\2\2\u00a0")
        buf.write("\u00a1\t\6\2\2\u00a1\u00a3\5\b\5\n\u00a2\u009c\3\2\2\2")
        buf.write("\u00a2\u009f\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\t\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a7\u00a8\7T\2\2\u00a8\u00ad\5\f\7\2\u00a9")
        buf.write("\u00aa\7\13\2\2\u00aa\u00ac\5\f\7\2\u00ab\u00a9\3\2\2")
        buf.write("\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0")
        buf.write("\u00b1\5\16\b\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4\5\16\b")
        buf.write("\2\u00b3\u00a7\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\13\3")
        buf.write("\2\2\2\u00b5\u00b6\7\\\2\2\u00b6\u00b7\7\"\2\2\u00b7\u00b8")
        buf.write("\7\t\2\2\u00b8\u00b9\5\16\b\2\u00b9\u00ba\7\n\2\2\u00ba")
        buf.write("\r\3\2\2\2\u00bb\u00c1\5\20\t\2\u00bc\u00bd\5,\27\2\u00bd")
        buf.write("\u00be\5\20\t\2\u00be\u00c0\3\2\2\2\u00bf\u00bc\3\2\2")
        buf.write("\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\17\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write("\5\22\n\2\u00c5\u00c7\5\24\13\2\u00c6\u00c8\5\34\17\2")
        buf.write("\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3")
        buf.write("\2\2\2\u00c9\u00cb\5\36\20\2\u00ca\u00c9\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ce\5.\30\2")
        buf.write("\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3")
        buf.write("\2\2\2\u00cf\u00d1\5\62\32\2\u00d0\u00cf\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\21\3\2\2\2\u00d2\u00d4\7K\2\2\u00d3")
        buf.write("\u00d5\7*\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00db\5*\26\2\u00d7\u00d8\7")
        buf.write("\13\2\2\u00d8\u00da\5*\26\2\u00d9\u00d7\3\2\2\2\u00da")
        buf.write("\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\23\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e8\7\61")
        buf.write("\2\2\u00df\u00e4\5\"\22\2\u00e0\u00e1\7\13\2\2\u00e1\u00e3")
        buf.write("\5\"\22\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e9\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e7\u00e9\5 \21\2\u00e8\u00df\3")
        buf.write("\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00f6\3\2\2\2\u00ea\u00eb")
        buf.write("\7\61\2\2\u00eb\u00ec\7\\\2\2\u00ec\u00ed\7>\2\2\u00ed")
        buf.write("\u00f2\5\26\f\2\u00ee\u00ef\7\13\2\2\u00ef\u00f1\5\26")
        buf.write("\f\2\u00f0\u00ee\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00de\3\2\2\2\u00f5\u00ea\3\2\2\2")
        buf.write("\u00f6\25\3\2\2\2\u00f7\u00f8\5\30\r\2\u00f8\u00fa\7\17")
        buf.write("\2\2\u00f9\u00fb\5\32\16\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7\3\2\2\u00fd")
        buf.write("\u00fe\5\30\r\2\u00fe\27\3\2\2\2\u00ff\u0101\7\t\2\2\u0100")
        buf.write("\u0102\7\\\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0105\3\2\2\2\u0103\u0104\7\4\2\2\u0104\u0106\7")
        buf.write("\\\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0108\7\n\2\2\u0108\31\3\2\2\2\u0109\u010a")
        buf.write("\7\5\2\2\u010a\u010b\7\\\2\2\u010b\u010c\7\6\2\2\u010c")
        buf.write("\33\3\2\2\2\u010d\u010e\7S\2\2\u010e\u010f\5\6\4\2\u010f")
        buf.write("\35\3\2\2\2\u0110\u0111\7\63\2\2\u0111\u0112\7%\2\2\u0112")
        buf.write("\u0117\5\b\5\2\u0113\u0114\7\13\2\2\u0114\u0116\5\b\5")
        buf.write("\2\u0115\u0113\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011c\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u011a\u011b\7\64\2\2\u011b\u011d\5\b\5")
        buf.write("\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\37\3")
        buf.write("\2\2\2\u011e\u0126\5\"\22\2\u011f\u0120\5&\24\2\u0120")
        buf.write("\u0122\5\"\22\2\u0121\u0123\5(\25\2\u0122\u0121\3\2\2")
        buf.write("\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u011f")
        buf.write("\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127!\3\2\2\2\u0128\u0126\3\2\2\2\u0129")
        buf.write("\u012b\5\b\5\2\u012a\u012c\5$\23\2\u012b\u012a\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c#\3\2\2\2\u012d\u012f\7\"\2")
        buf.write("\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u013b\7\\\2\2\u0131\u0132\7\t\2\2\u0132")
        buf.write("\u0137\7\\\2\2\u0133\u0134\7\13\2\2\u0134\u0136\7\\\2")
        buf.write("\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u013a\u013c\7\n\2\2\u013b\u0131\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c%\3\2\2\2\u013d\u014b\7\13\2")
        buf.write("\2\u013e\u0140\7?\2\2\u013f\u013e\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0147\3\2\2\2\u0141\u0143\7;\2\2\u0142")
        buf.write("\u0144\7G\2\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0148\3\2\2\2\u0145\u0148\7\66\2\2\u0146\u0148")
        buf.write("\7(\2\2\u0147\u0141\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014b\7:\2\2\u014a\u013d\3\2\2\2\u014a\u013f\3")
        buf.write("\2\2\2\u014b\'\3\2\2\2\u014c\u014d\7D\2\2\u014d\u015a")
        buf.write("\5\b\5\2\u014e\u014f\7O\2\2\u014f\u0150\7\t\2\2\u0150")
        buf.write("\u0155\7\\\2\2\u0151\u0152\7\13\2\2\u0152\u0154\7\\\2")
        buf.write("\2\u0153\u0151\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0158\u015a\7\n\2\2\u0159\u014c\3\2\2\2")
        buf.write("\u0159\u014e\3\2\2\2\u015a)\3\2\2\2\u015b\u0164\7\r\2")
        buf.write("\2\u015c\u0161\5\6\4\2\u015d\u015f\7\"\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0162\7\\\2\2\u0161\u015e\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0164\3\2\2\2\u0163\u015b\3\2\2\2\u0163\u015c\3")
        buf.write("\2\2\2\u0164+\3\2\2\2\u0165\u016b\7M\2\2\u0166\u0167\7")
        buf.write("M\2\2\u0167\u016b\7 \2\2\u0168\u016b\7\67\2\2\u0169\u016b")
        buf.write("\7/\2\2\u016a\u0165\3\2\2\2\u016a\u0166\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b-\3\2\2\2\u016c")
        buf.write("\u016d\7F\2\2\u016d\u016e\7%\2\2\u016e\u0173\5\60\31\2")
        buf.write("\u016f\u0170\7\13\2\2\u0170\u0172\5\60\31\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174/\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0178\7]\2\2\u0177\u0179\t\7\2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\61\3\2\2\2\u017a\u017b\7=\2")
        buf.write("\2\u017b\u017e\7]\2\2\u017c\u017d\t\b\2\2\u017d\u017f")
        buf.write("\7]\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\63\3\2\2\2\u0180\u0182\7\\\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u018f\3\2\2\2\u0185\u0186\7\t\2\2\u0186\u0187\5")
        buf.write("\66\34\2\u0187\u0188\7\n\2\2\u0188\u0190\3\2\2\2\u0189")
        buf.write("\u018a\7\t\2\2\u018a\u018b\5\66\34\2\u018b\u018c\7\13")
        buf.write("\2\2\u018c\u018d\5\66\34\2\u018d\u018e\7\n\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u0185\3\2\2\2\u018f\u0189\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\65\3\2\2\2\u0191\u0193\t\6\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0195\7]\2\2\u0195\67\3\2\2\2\u0196\u0197\t\t\2")
        buf.write("\2\u01979\3\2\2\28?NUchmuw\u0084\u0088\u0090\u009a\u00a2")
        buf.write("\u00a4\u00ad\u00b3\u00c1\u00c7\u00ca\u00cd\u00d0\u00d4")
        buf.write("\u00db\u00e4\u00e8\u00f2\u00f5\u00fa\u0101\u0105\u0117")
        buf.write("\u011c\u0122\u0126\u012b\u012e\u0137\u013b\u013f\u0143")
        buf.write("\u0147\u014a\u0155\u0159\u015e\u0161\u0163\u016a\u0173")
        buf.write("\u0178\u017e\u0183\u018f\u0192")
        return buf.getvalue()


class DCLParser ( Parser ):

    grammarFileName = "DCL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "':'", "'[:'", "']'", "';'", "'.'", 
                     "'('", "')'", "','", "':='", "'*'", "'+'", "'-'", "'~'", 
                     "'||'", "'/'", "'%'", "'<<'", "'>>'", "'&'", "'|'", 
                     "'<'", "'<='", "'>'", "'>='", "'='", "'=='", "'!='", 
                     "'<>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SCOL", "DOT", "OPEN_PAR", "CLOSE_PAR", 
                      "COMMA", "ASSIGN", "STAR", "PLUS", "MINUS", "TILDE", 
                      "PIPE2", "DIV", "MOD", "LT2", "GT2", "AMP", "PIPE", 
                      "LT", "LT_EQ", "GT", "GT_EQ", "EQ1", "EQ2", "NOT_EQ1", 
                      "NOT_EQ2", "K_ALL", "K_AND", "K_AS", "K_ASC", "K_BETWEEN", 
                      "K_BY", "K_CASE", "K_CAST", "K_CROSS", "K_DESC", "K_DISTINCT", 
                      "K_DROP", "K_ELSE", "K_END", "K_ESCAPE", "K_EXCEPT", 
                      "K_EXTRACT", "K_FROM", "K_GLOB", "K_GROUP", "K_HAVING", 
                      "K_IN", "K_INNER", "K_INTERSECT", "K_IS", "K_ISNULL", 
                      "K_JOIN", "K_LEFT", "K_LIKE", "K_LIMIT", "K_MATCH", 
                      "K_NATURAL", "K_NOT", "K_NOTNULL", "K_NULL", "K_OFFSET", 
                      "K_ON", "K_OR", "K_ORDER", "K_OUTER", "K_RECURSIVE", 
                      "K_REGEXP", "K_ROW", "K_SELECT", "K_THEN", "K_UNION", 
                      "K_UNIQUE", "K_USING", "K_VALUE", "K_VALUES", "K_WHEN", 
                      "K_WHERE", "K_WITH", "K_YEAR", "K_MONTH", "K_DAY", 
                      "K_HOUR", "K_MINUTE", "K_SECOND", "LET_IDENT", "IDENT", 
                      "NUMERIC_LITERAL", "STRING_LITERAL", "SINGLE_LINE_COMMENT", 
                      "MULTILINE_COMMENT", "SPACES", "ERROR" ]

    RULE_queryRule = 0
    RULE_exprRule = 1
    RULE_booleanExprRule = 2
    RULE_baseExprRule = 3
    RULE_compositeSqlQueryRule = 4
    RULE_commonTableExpressionRule = 5
    RULE_sqlQueryRule = 6
    RULE_tableExpressionRule = 7
    RULE_selectClauseRule = 8
    RULE_fromClauseRule = 9
    RULE_graphPathRule = 10
    RULE_graphNodeRule = 11
    RULE_graphRelationRule = 12
    RULE_whereClauseRule = 13
    RULE_groupByClauseRule = 14
    RULE_joinClauseRule = 15
    RULE_tableRule = 16
    RULE_tableAliasRule = 17
    RULE_joinOperatorRule = 18
    RULE_joinConstraintRule = 19
    RULE_resultColumnRule = 20
    RULE_compoundOperatorRule = 21
    RULE_orderByClauseRule = 22
    RULE_orderingTermRule = 23
    RULE_limitClauseRule = 24
    RULE_typeNameRule = 25
    RULE_signedNumberRule = 26
    RULE_keywordRule = 27

    ruleNames =  [ "queryRule", "exprRule", "booleanExprRule", "baseExprRule", 
                   "compositeSqlQueryRule", "commonTableExpressionRule", 
                   "sqlQueryRule", "tableExpressionRule", "selectClauseRule", 
                   "fromClauseRule", "graphPathRule", "graphNodeRule", "graphRelationRule", 
                   "whereClauseRule", "groupByClauseRule", "joinClauseRule", 
                   "tableRule", "tableAliasRule", "joinOperatorRule", "joinConstraintRule", 
                   "resultColumnRule", "compoundOperatorRule", "orderByClauseRule", 
                   "orderingTermRule", "limitClauseRule", "typeNameRule", 
                   "signedNumberRule", "keywordRule" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SCOL=5
    DOT=6
    OPEN_PAR=7
    CLOSE_PAR=8
    COMMA=9
    ASSIGN=10
    STAR=11
    PLUS=12
    MINUS=13
    TILDE=14
    PIPE2=15
    DIV=16
    MOD=17
    LT2=18
    GT2=19
    AMP=20
    PIPE=21
    LT=22
    LT_EQ=23
    GT=24
    GT_EQ=25
    EQ1=26
    EQ2=27
    NOT_EQ1=28
    NOT_EQ2=29
    K_ALL=30
    K_AND=31
    K_AS=32
    K_ASC=33
    K_BETWEEN=34
    K_BY=35
    K_CASE=36
    K_CAST=37
    K_CROSS=38
    K_DESC=39
    K_DISTINCT=40
    K_DROP=41
    K_ELSE=42
    K_END=43
    K_ESCAPE=44
    K_EXCEPT=45
    K_EXTRACT=46
    K_FROM=47
    K_GLOB=48
    K_GROUP=49
    K_HAVING=50
    K_IN=51
    K_INNER=52
    K_INTERSECT=53
    K_IS=54
    K_ISNULL=55
    K_JOIN=56
    K_LEFT=57
    K_LIKE=58
    K_LIMIT=59
    K_MATCH=60
    K_NATURAL=61
    K_NOT=62
    K_NOTNULL=63
    K_NULL=64
    K_OFFSET=65
    K_ON=66
    K_OR=67
    K_ORDER=68
    K_OUTER=69
    K_RECURSIVE=70
    K_REGEXP=71
    K_ROW=72
    K_SELECT=73
    K_THEN=74
    K_UNION=75
    K_UNIQUE=76
    K_USING=77
    K_VALUE=78
    K_VALUES=79
    K_WHEN=80
    K_WHERE=81
    K_WITH=82
    K_YEAR=83
    K_MONTH=84
    K_DAY=85
    K_HOUR=86
    K_MINUTE=87
    K_SECOND=88
    LET_IDENT=89
    IDENT=90
    NUMERIC_LITERAL=91
    STRING_LITERAL=92
    SINGLE_LINE_COMMENT=93
    MULTILINE_COMMENT=94
    SPACES=95
    ERROR=96

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprRule(self):
            return self.getTypedRuleContext(DCLParser.ExprRuleContext,0)


        def EOF(self):
            return self.getToken(DCLParser.EOF, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_queryRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryRule" ):
                listener.enterQueryRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryRule" ):
                listener.exitQueryRule(self)




    def queryRule(self):

        localctx = DCLParser.QueryRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_queryRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.exprRule()
            self.state = 57
            self.match(DCLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_exprRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BooleanExpressionContext(ExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.ExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExprRule(self):
            return self.getTypedRuleContext(DCLParser.BooleanExprRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)


    class SqlExpressionContext(ExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.ExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compositeSqlQueryRule(self):
            return self.getTypedRuleContext(DCLParser.CompositeSqlQueryRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlExpression" ):
                listener.enterSqlExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlExpression" ):
                listener.exitSqlExpression(self)



    def exprRule(self):

        localctx = DCLParser.ExprRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exprRule)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DCLParser.K_SELECT, DCLParser.K_WITH]:
                localctx = DCLParser.SqlExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.compositeSqlQueryRule()
                pass
            elif token in [DCLParser.OPEN_PAR, DCLParser.MINUS, DCLParser.K_NOT, DCLParser.K_NULL, DCLParser.IDENT, DCLParser.NUMERIC_LITERAL, DCLParser.STRING_LITERAL]:
                localctx = DCLParser.BooleanExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.booleanExprRule(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExprRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_booleanExprRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NullCheckExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.isNull = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)

        def K_NULL(self):
            return self.getToken(DCLParser.K_NULL, 0)
        def K_NOTNULL(self):
            return self.getToken(DCLParser.K_NOTNULL, 0)
        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)
        def K_ISNULL(self):
            return self.getToken(DCLParser.K_ISNULL, 0)
        def K_IS(self):
            return self.getToken(DCLParser.K_IS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullCheckExpression" ):
                listener.enterNullCheckExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullCheckExpression" ):
                listener.exitNullCheckExpression(self)


    class BaseExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseExpression" ):
                listener.enterBaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseExpression" ):
                listener.exitBaseExpression(self)


    class IsExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.negate = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def K_IS(self):
            return self.getToken(DCLParser.K_IS, 0)
        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsExpression" ):
                listener.enterIsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsExpression" ):
                listener.exitIsExpression(self)


    class AndExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BooleanExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BooleanExprRuleContext,i)

        def K_AND(self):
            return self.getToken(DCLParser.K_AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)


    class BetweenExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.negate = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def K_BETWEEN(self):
            return self.getToken(DCLParser.K_BETWEEN, 0)
        def K_AND(self):
            return self.getToken(DCLParser.K_AND, 0)
        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenExpression" ):
                listener.enterBetweenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenExpression" ):
                listener.exitBetweenExpression(self)


    class StringCompExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.negate = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def K_LIKE(self):
            return self.getToken(DCLParser.K_LIKE, 0)
        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringCompExpression" ):
                listener.enterStringCompExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringCompExpression" ):
                listener.exitStringCompExpression(self)


    class HighCompExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def LT(self):
            return self.getToken(DCLParser.LT, 0)
        def LT_EQ(self):
            return self.getToken(DCLParser.LT_EQ, 0)
        def GT(self):
            return self.getToken(DCLParser.GT, 0)
        def GT_EQ(self):
            return self.getToken(DCLParser.GT_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHighCompExpression" ):
                listener.enterHighCompExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHighCompExpression" ):
                listener.exitHighCompExpression(self)


    class NotExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.value = None # BaseExprRuleContext
            self.copyFrom(ctx)

        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)
        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)


    class OrExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BooleanExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BooleanExprRuleContext,i)

        def K_OR(self):
            return self.getToken(DCLParser.K_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)


    class LowCompExpressionContext(BooleanExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BooleanExprRuleContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def EQ1(self):
            return self.getToken(DCLParser.EQ1, 0)
        def EQ2(self):
            return self.getToken(DCLParser.EQ2, 0)
        def NOT_EQ1(self):
            return self.getToken(DCLParser.NOT_EQ1, 0)
        def NOT_EQ2(self):
            return self.getToken(DCLParser.NOT_EQ2, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowCompExpression" ):
                listener.enterLowCompExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowCompExpression" ):
                listener.exitLowCompExpression(self)



    def booleanExprRule(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DCLParser.BooleanExprRuleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_booleanExprRule, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = DCLParser.HighCompExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.baseExprRule(0)
                self.state = 65
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DCLParser.LT) | (1 << DCLParser.LT_EQ) | (1 << DCLParser.GT) | (1 << DCLParser.GT_EQ))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.baseExprRule(0)
                pass

            elif la_ == 2:
                localctx = DCLParser.LowCompExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.baseExprRule(0)
                self.state = 69
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DCLParser.EQ1) | (1 << DCLParser.EQ2) | (1 << DCLParser.NOT_EQ1) | (1 << DCLParser.NOT_EQ2))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.baseExprRule(0)
                pass

            elif la_ == 3:
                localctx = DCLParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(DCLParser.K_NOT)
                self.state = 73
                localctx.value = self.baseExprRule(0)
                pass

            elif la_ == 4:
                localctx = DCLParser.StringCompExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.baseExprRule(0)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DCLParser.K_NOT:
                    self.state = 75
                    localctx.negate = self.match(DCLParser.K_NOT)


                self.state = 78
                self.match(DCLParser.K_LIKE)
                self.state = 79
                self.baseExprRule(0)
                pass

            elif la_ == 5:
                localctx = DCLParser.BetweenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.baseExprRule(0)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DCLParser.K_NOT:
                    self.state = 82
                    localctx.negate = self.match(DCLParser.K_NOT)


                self.state = 85
                self.match(DCLParser.K_BETWEEN)
                self.state = 86
                self.baseExprRule(0)
                self.state = 87
                self.match(DCLParser.K_AND)
                self.state = 88
                self.baseExprRule(0)
                pass

            elif la_ == 6:
                localctx = DCLParser.NullCheckExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.baseExprRule(0)
                self.state = 97
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DCLParser.K_ISNULL]:
                    self.state = 91
                    localctx.isNull = self.match(DCLParser.K_ISNULL)
                    pass
                elif token in [DCLParser.K_IS]:
                    self.state = 92
                    localctx.isNull = self.match(DCLParser.K_IS)
                    self.state = 93
                    self.match(DCLParser.K_NULL)
                    pass
                elif token in [DCLParser.K_NOTNULL]:
                    self.state = 94
                    self.match(DCLParser.K_NOTNULL)
                    pass
                elif token in [DCLParser.K_NOT]:
                    self.state = 95
                    self.match(DCLParser.K_NOT)
                    self.state = 96
                    self.match(DCLParser.K_NULL)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 7:
                localctx = DCLParser.IsExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.baseExprRule(0)
                self.state = 100
                self.match(DCLParser.K_IS)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DCLParser.K_NOT:
                    self.state = 101
                    localctx.negate = self.match(DCLParser.K_NOT)


                self.state = 104
                self.baseExprRule(0)
                pass

            elif la_ == 8:
                localctx = DCLParser.BaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.baseExprRule(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = DCLParser.AndExpressionContext(self, DCLParser.BooleanExprRuleContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExprRule)
                        self.state = 109
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 110
                        self.match(DCLParser.K_AND)
                        self.state = 111
                        self.booleanExprRule(8)
                        pass

                    elif la_ == 2:
                        localctx = DCLParser.OrExpressionContext(self, DCLParser.BooleanExprRuleContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExprRule)
                        self.state = 112
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 113
                        self.match(DCLParser.K_OR)
                        self.state = 114
                        self.booleanExprRule(7)
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BaseExprRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_baseExprRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegateExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.value = None # BaseExprRuleContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(DCLParser.MINUS, 0)
        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpression" ):
                listener.enterNegateExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpression" ):
                listener.exitNegateExpression(self)


    class PathExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self._IDENT = None # Token
            self.segments = list() # of Tokens
            self._STRING_LITERAL = None # Token
            self._tset131 = None # Token
            self.copyFrom(ctx)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.IDENT)
            else:
                return self.getToken(DCLParser.IDENT, i)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.DOT)
            else:
                return self.getToken(DCLParser.DOT, i)
        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.STRING_LITERAL)
            else:
                return self.getToken(DCLParser.STRING_LITERAL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathExpression" ):
                listener.enterPathExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathExpression" ):
                listener.exitPathExpression(self)


    class NumericLiteralContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERIC_LITERAL(self):
            return self.getToken(DCLParser.NUMERIC_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)


    class StringLiteralContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(DCLParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)


    class HighMathExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def STAR(self):
            return self.getToken(DCLParser.STAR, 0)
        def DIV(self):
            return self.getToken(DCLParser.DIV, 0)
        def MOD(self):
            return self.getToken(DCLParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHighMathExpression" ):
                listener.enterHighMathExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHighMathExpression" ):
                listener.exitHighMathExpression(self)


    class ParenExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)
        def exprRule(self):
            return self.getTypedRuleContext(DCLParser.ExprRuleContext,0)

        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)


    class NullLiteralContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_NULL(self):
            return self.getToken(DCLParser.K_NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLiteral" ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLiteral" ):
                listener.exitNullLiteral(self)


    class ApplyExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.func = None # Token
            self._exprRule = None # ExprRuleContext
            self.args = list() # of ExprRuleContexts
            self.starCount = None # Token
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)
        def IDENT(self):
            return self.getToken(DCLParser.IDENT, 0)
        def exprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.ExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.ExprRuleContext,i)

        def STAR(self):
            return self.getToken(DCLParser.STAR, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplyExpression" ):
                listener.enterApplyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplyExpression" ):
                listener.exitApplyExpression(self)


    class LowMathExpressionContext(BaseExprRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.BaseExprRuleContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)

        def PLUS(self):
            return self.getToken(DCLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(DCLParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowMathExpression" ):
                listener.enterLowMathExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowMathExpression" ):
                listener.exitLowMathExpression(self)



    def baseExprRule(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DCLParser.BaseExprRuleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_baseExprRule, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = DCLParser.NegateExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 121
                self.match(DCLParser.MINUS)
                self.state = 122
                localctx.value = self.baseExprRule(9)
                pass

            elif la_ == 2:
                localctx = DCLParser.ApplyExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                localctx.func = self.match(DCLParser.IDENT)
                self.state = 124
                self.match(DCLParser.OPEN_PAR)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DCLParser.OPEN_PAR, DCLParser.MINUS, DCLParser.K_NOT, DCLParser.K_NULL, DCLParser.K_SELECT, DCLParser.K_WITH, DCLParser.IDENT, DCLParser.NUMERIC_LITERAL, DCLParser.STRING_LITERAL]:
                    self.state = 125
                    localctx._exprRule = self.exprRule()
                    localctx.args.append(localctx._exprRule)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DCLParser.COMMA:
                        self.state = 126
                        self.match(DCLParser.COMMA)
                        self.state = 127
                        localctx._exprRule = self.exprRule()
                        localctx.args.append(localctx._exprRule)
                        self.state = 132
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                elif token in [DCLParser.STAR]:
                    self.state = 133
                    localctx.starCount = self.match(DCLParser.STAR)
                    pass
                elif token in [DCLParser.CLOSE_PAR]:
                    pass
                else:
                    pass
                self.state = 136
                self.match(DCLParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                localctx = DCLParser.PathExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                localctx._IDENT = self.match(DCLParser.IDENT)
                localctx.segments.append(localctx._IDENT)
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 138
                        self.match(DCLParser.DOT)
                        self.state = 139
                        localctx._tset131 = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==DCLParser.IDENT or _la==DCLParser.STRING_LITERAL):
                            localctx._tset131 = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        localctx.segments.append(localctx._tset131) 
                    self.state = 144
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 4:
                localctx = DCLParser.NullLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(DCLParser.K_NULL)
                pass

            elif la_ == 5:
                localctx = DCLParser.NumericLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(DCLParser.NUMERIC_LITERAL)
                pass

            elif la_ == 6:
                localctx = DCLParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(DCLParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                localctx = DCLParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(DCLParser.OPEN_PAR)
                self.state = 149
                self.exprRule()
                self.state = 150
                self.match(DCLParser.CLOSE_PAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 160
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = DCLParser.HighMathExpressionContext(self, DCLParser.BaseExprRuleContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_baseExprRule)
                        self.state = 154
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 155
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DCLParser.STAR) | (1 << DCLParser.DIV) | (1 << DCLParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 156
                        self.baseExprRule(9)
                        pass

                    elif la_ == 2:
                        localctx = DCLParser.LowMathExpressionContext(self, DCLParser.BaseExprRuleContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_baseExprRule)
                        self.state = 157
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 158
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==DCLParser.PLUS or _la==DCLParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.baseExprRule(8)
                        pass

             
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompositeSqlQueryRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_compositeSqlQueryRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleQueryContext(CompositeSqlQueryRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompositeSqlQueryRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sqlQueryRule(self):
            return self.getTypedRuleContext(DCLParser.SqlQueryRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleQuery" ):
                listener.enterSimpleQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleQuery" ):
                listener.exitSimpleQuery(self)


    class WithQueryContext(CompositeSqlQueryRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompositeSqlQueryRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_WITH(self):
            return self.getToken(DCLParser.K_WITH, 0)
        def commonTableExpressionRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.CommonTableExpressionRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.CommonTableExpressionRuleContext,i)

        def sqlQueryRule(self):
            return self.getTypedRuleContext(DCLParser.SqlQueryRuleContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithQuery" ):
                listener.enterWithQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithQuery" ):
                listener.exitWithQuery(self)



    def compositeSqlQueryRule(self):

        localctx = DCLParser.CompositeSqlQueryRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compositeSqlQueryRule)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DCLParser.K_WITH]:
                localctx = DCLParser.WithQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(DCLParser.K_WITH)
                self.state = 166
                self.commonTableExpressionRule()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DCLParser.COMMA:
                    self.state = 167
                    self.match(DCLParser.COMMA)
                    self.state = 168
                    self.commonTableExpressionRule()
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 174
                self.sqlQueryRule()
                pass
            elif token in [DCLParser.K_SELECT]:
                localctx = DCLParser.SimpleQueryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.sqlQueryRule()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommonTableExpressionRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.alias = None # Token

        def K_AS(self):
            return self.getToken(DCLParser.K_AS, 0)

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)

        def sqlQueryRule(self):
            return self.getTypedRuleContext(DCLParser.SqlQueryRuleContext,0)


        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)

        def IDENT(self):
            return self.getToken(DCLParser.IDENT, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_commonTableExpressionRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommonTableExpressionRule" ):
                listener.enterCommonTableExpressionRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommonTableExpressionRule" ):
                listener.exitCommonTableExpressionRule(self)




    def commonTableExpressionRule(self):

        localctx = DCLParser.CommonTableExpressionRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_commonTableExpressionRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            localctx.alias = self.match(DCLParser.IDENT)
            self.state = 180
            self.match(DCLParser.K_AS)
            self.state = 181
            self.match(DCLParser.OPEN_PAR)
            self.state = 182
            self.sqlQueryRule()
            self.state = 183
            self.match(DCLParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlQueryRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tableExpressionRule = None # TableExpressionRuleContext
            self.tables = list() # of TableExpressionRuleContexts
            self._compoundOperatorRule = None # CompoundOperatorRuleContext
            self.compoundOps = list() # of CompoundOperatorRuleContexts

        def tableExpressionRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.TableExpressionRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.TableExpressionRuleContext,i)


        def compoundOperatorRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.CompoundOperatorRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.CompoundOperatorRuleContext,i)


        def getRuleIndex(self):
            return DCLParser.RULE_sqlQueryRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlQueryRule" ):
                listener.enterSqlQueryRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlQueryRule" ):
                listener.exitSqlQueryRule(self)




    def sqlQueryRule(self):

        localctx = DCLParser.SqlQueryRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sqlQueryRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            localctx._tableExpressionRule = self.tableExpressionRule()
            localctx.tables.append(localctx._tableExpressionRule)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (DCLParser.K_EXCEPT - 45)) | (1 << (DCLParser.K_INTERSECT - 45)) | (1 << (DCLParser.K_UNION - 45)))) != 0):
                self.state = 186
                localctx._compoundOperatorRule = self.compoundOperatorRule()
                localctx.compoundOps.append(localctx._compoundOperatorRule)
                self.state = 187
                localctx._tableExpressionRule = self.tableExpressionRule()
                localctx.tables.append(localctx._tableExpressionRule)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableExpressionRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectClauseRule(self):
            return self.getTypedRuleContext(DCLParser.SelectClauseRuleContext,0)


        def fromClauseRule(self):
            return self.getTypedRuleContext(DCLParser.FromClauseRuleContext,0)


        def whereClauseRule(self):
            return self.getTypedRuleContext(DCLParser.WhereClauseRuleContext,0)


        def groupByClauseRule(self):
            return self.getTypedRuleContext(DCLParser.GroupByClauseRuleContext,0)


        def orderByClauseRule(self):
            return self.getTypedRuleContext(DCLParser.OrderByClauseRuleContext,0)


        def limitClauseRule(self):
            return self.getTypedRuleContext(DCLParser.LimitClauseRuleContext,0)


        def getRuleIndex(self):
            return DCLParser.RULE_tableExpressionRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableExpressionRule" ):
                listener.enterTableExpressionRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableExpressionRule" ):
                listener.exitTableExpressionRule(self)




    def tableExpressionRule(self):

        localctx = DCLParser.TableExpressionRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tableExpressionRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.selectClauseRule()
            self.state = 195
            self.fromClauseRule()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_WHERE:
                self.state = 196
                self.whereClauseRule()


            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_GROUP:
                self.state = 199
                self.groupByClauseRule()


            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_ORDER:
                self.state = 202
                self.orderByClauseRule()


            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_LIMIT:
                self.state = 205
                self.limitClauseRule()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.distinct = None # Token

        def K_SELECT(self):
            return self.getToken(DCLParser.K_SELECT, 0)

        def resultColumnRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.ResultColumnRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.ResultColumnRuleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def K_DISTINCT(self):
            return self.getToken(DCLParser.K_DISTINCT, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_selectClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectClauseRule" ):
                listener.enterSelectClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectClauseRule" ):
                listener.exitSelectClauseRule(self)




    def selectClauseRule(self):

        localctx = DCLParser.SelectClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_selectClauseRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(DCLParser.K_SELECT)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_DISTINCT:
                self.state = 209
                localctx.distinct = self.match(DCLParser.K_DISTINCT)


            self.state = 212
            self.resultColumnRule()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DCLParser.COMMA:
                self.state = 213
                self.match(DCLParser.COMMA)
                self.state = 214
                self.resultColumnRule()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_fromClauseRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FromTableRuleContext(FromClauseRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.FromClauseRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_FROM(self):
            return self.getToken(DCLParser.K_FROM, 0)
        def tableRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.TableRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.TableRuleContext,i)

        def joinClauseRule(self):
            return self.getTypedRuleContext(DCLParser.JoinClauseRuleContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromTableRule" ):
                listener.enterFromTableRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromTableRule" ):
                listener.exitFromTableRule(self)


    class FromMatchRuleContext(FromClauseRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.FromClauseRuleContext
            super().__init__(parser)
            self.system = None # Token
            self._graphPathRule = None # GraphPathRuleContext
            self.patterns = list() # of GraphPathRuleContexts
            self.copyFrom(ctx)

        def K_FROM(self):
            return self.getToken(DCLParser.K_FROM, 0)
        def K_MATCH(self):
            return self.getToken(DCLParser.K_MATCH, 0)
        def IDENT(self):
            return self.getToken(DCLParser.IDENT, 0)
        def graphPathRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.GraphPathRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.GraphPathRuleContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromMatchRule" ):
                listener.enterFromMatchRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromMatchRule" ):
                listener.exitFromMatchRule(self)



    def fromClauseRule(self):

        localctx = DCLParser.FromClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fromClauseRule)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = DCLParser.FromTableRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(DCLParser.K_FROM)
                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.tableRule()
                    self.state = 226
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 222
                            self.match(DCLParser.COMMA)
                            self.state = 223
                            self.tableRule() 
                        self.state = 228
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    pass

                elif la_ == 2:
                    self.state = 229
                    self.joinClauseRule()
                    pass


                pass

            elif la_ == 2:
                localctx = DCLParser.FromMatchRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(DCLParser.K_FROM)
                self.state = 233
                localctx.system = self.match(DCLParser.IDENT)
                self.state = 234
                self.match(DCLParser.K_MATCH)
                self.state = 235
                localctx._graphPathRule = self.graphPathRule()
                localctx.patterns.append(localctx._graphPathRule)
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 236
                        self.match(DCLParser.COMMA)
                        self.state = 237
                        localctx._graphPathRule = self.graphPathRule()
                        localctx.patterns.append(localctx._graphPathRule) 
                    self.state = 242
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphPathRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fromNode = None # GraphNodeRuleContext
            self.rel = None # GraphRelationRuleContext
            self.toNode = None # GraphNodeRuleContext

        def MINUS(self):
            return self.getToken(DCLParser.MINUS, 0)

        def graphNodeRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.GraphNodeRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.GraphNodeRuleContext,i)


        def graphRelationRule(self):
            return self.getTypedRuleContext(DCLParser.GraphRelationRuleContext,0)


        def getRuleIndex(self):
            return DCLParser.RULE_graphPathRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphPathRule" ):
                listener.enterGraphPathRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphPathRule" ):
                listener.exitGraphPathRule(self)




    def graphPathRule(self):

        localctx = DCLParser.GraphPathRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_graphPathRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            localctx.fromNode = self.graphNodeRule()
            self.state = 246
            self.match(DCLParser.MINUS)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.T__2:
                self.state = 247
                localctx.rel = self.graphRelationRule()


            self.state = 250
            self.match(DCLParser.T__0)
            self.state = 251
            localctx.toNode = self.graphNodeRule()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphNodeRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.label = None # Token

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.IDENT)
            else:
                return self.getToken(DCLParser.IDENT, i)

        def getRuleIndex(self):
            return DCLParser.RULE_graphNodeRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphNodeRule" ):
                listener.enterGraphNodeRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphNodeRule" ):
                listener.exitGraphNodeRule(self)




    def graphNodeRule(self):

        localctx = DCLParser.GraphNodeRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_graphNodeRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(DCLParser.OPEN_PAR)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.IDENT:
                self.state = 254
                localctx.name = self.match(DCLParser.IDENT)


            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.T__1:
                self.state = 257
                self.match(DCLParser.T__1)
                self.state = 258
                localctx.label = self.match(DCLParser.IDENT)


            self.state = 261
            self.match(DCLParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphRelationRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.relType = None # Token

        def IDENT(self):
            return self.getToken(DCLParser.IDENT, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_graphRelationRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphRelationRule" ):
                listener.enterGraphRelationRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphRelationRule" ):
                listener.exitGraphRelationRule(self)




    def graphRelationRule(self):

        localctx = DCLParser.GraphRelationRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_graphRelationRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(DCLParser.T__2)
            self.state = 264
            localctx.relType = self.match(DCLParser.IDENT)
            self.state = 265
            self.match(DCLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.where = None # BooleanExprRuleContext

        def K_WHERE(self):
            return self.getToken(DCLParser.K_WHERE, 0)

        def booleanExprRule(self):
            return self.getTypedRuleContext(DCLParser.BooleanExprRuleContext,0)


        def getRuleIndex(self):
            return DCLParser.RULE_whereClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClauseRule" ):
                listener.enterWhereClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClauseRule" ):
                listener.exitWhereClauseRule(self)




    def whereClauseRule(self):

        localctx = DCLParser.WhereClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whereClauseRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(DCLParser.K_WHERE)
            self.state = 268
            localctx.where = self.booleanExprRule(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupByClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._baseExprRule = None # BaseExprRuleContext
            self.groupBy = list() # of BaseExprRuleContexts
            self.having = None # BaseExprRuleContext

        def K_GROUP(self):
            return self.getToken(DCLParser.K_GROUP, 0)

        def K_BY(self):
            return self.getToken(DCLParser.K_BY, 0)

        def baseExprRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.BaseExprRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def K_HAVING(self):
            return self.getToken(DCLParser.K_HAVING, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_groupByClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupByClauseRule" ):
                listener.enterGroupByClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupByClauseRule" ):
                listener.exitGroupByClauseRule(self)




    def groupByClauseRule(self):

        localctx = DCLParser.GroupByClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_groupByClauseRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(DCLParser.K_GROUP)
            self.state = 271
            self.match(DCLParser.K_BY)
            self.state = 272
            localctx._baseExprRule = self.baseExprRule(0)
            localctx.groupBy.append(localctx._baseExprRule)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 273
                    self.match(DCLParser.COMMA)
                    self.state = 274
                    localctx._baseExprRule = self.baseExprRule(0)
                    localctx.groupBy.append(localctx._baseExprRule) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_HAVING:
                self.state = 280
                self.match(DCLParser.K_HAVING)
                self.state = 281
                localctx.having = self.baseExprRule(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.TableRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.TableRuleContext,i)


        def joinOperatorRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.JoinOperatorRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.JoinOperatorRuleContext,i)


        def joinConstraintRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.JoinConstraintRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.JoinConstraintRuleContext,i)


        def getRuleIndex(self):
            return DCLParser.RULE_joinClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinClauseRule" ):
                listener.enterJoinClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinClauseRule" ):
                listener.exitJoinClauseRule(self)




    def joinClauseRule(self):

        localctx = DCLParser.JoinClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_joinClauseRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.tableRule()
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 285
                    self.joinOperatorRule()
                    self.state = 286
                    self.tableRule()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==DCLParser.K_ON or _la==DCLParser.K_USING:
                        self.state = 287
                        self.joinConstraintRule()

             
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table = None # BaseExprRuleContext

        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)


        def tableAliasRule(self):
            return self.getTypedRuleContext(DCLParser.TableAliasRuleContext,0)


        def getRuleIndex(self):
            return DCLParser.RULE_tableRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableRule" ):
                listener.enterTableRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableRule" ):
                listener.exitTableRule(self)




    def tableRule(self):

        localctx = DCLParser.TableRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tableRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            localctx.table = self.baseExprRule(0)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_AS or _la==DCLParser.IDENT:
                self.state = 296
                self.tableAliasRule()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableAliasRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tableAlias = None # Token
            self._IDENT = None # Token
            self.columnAlias = list() # of Tokens

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.IDENT)
            else:
                return self.getToken(DCLParser.IDENT, i)

        def K_AS(self):
            return self.getToken(DCLParser.K_AS, 0)

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def getRuleIndex(self):
            return DCLParser.RULE_tableAliasRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableAliasRule" ):
                listener.enterTableAliasRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableAliasRule" ):
                listener.exitTableAliasRule(self)




    def tableAliasRule(self):

        localctx = DCLParser.TableAliasRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tableAliasRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_AS:
                self.state = 299
                self.match(DCLParser.K_AS)


            self.state = 302
            localctx.tableAlias = self.match(DCLParser.IDENT)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.OPEN_PAR:
                self.state = 303
                self.match(DCLParser.OPEN_PAR)
                self.state = 304
                localctx._IDENT = self.match(DCLParser.IDENT)
                localctx.columnAlias.append(localctx._IDENT)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DCLParser.COMMA:
                    self.state = 305
                    self.match(DCLParser.COMMA)
                    self.state = 306
                    localctx._IDENT = self.match(DCLParser.IDENT)
                    localctx.columnAlias.append(localctx._IDENT)
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 312
                self.match(DCLParser.CLOSE_PAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinOperatorRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DCLParser.COMMA, 0)

        def K_JOIN(self):
            return self.getToken(DCLParser.K_JOIN, 0)

        def K_NATURAL(self):
            return self.getToken(DCLParser.K_NATURAL, 0)

        def K_LEFT(self):
            return self.getToken(DCLParser.K_LEFT, 0)

        def K_INNER(self):
            return self.getToken(DCLParser.K_INNER, 0)

        def K_CROSS(self):
            return self.getToken(DCLParser.K_CROSS, 0)

        def K_OUTER(self):
            return self.getToken(DCLParser.K_OUTER, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_joinOperatorRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinOperatorRule" ):
                listener.enterJoinOperatorRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinOperatorRule" ):
                listener.exitJoinOperatorRule(self)




    def joinOperatorRule(self):

        localctx = DCLParser.JoinOperatorRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_joinOperatorRule)
        self._la = 0 # Token type
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DCLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(DCLParser.COMMA)
                pass
            elif token in [DCLParser.K_CROSS, DCLParser.K_INNER, DCLParser.K_JOIN, DCLParser.K_LEFT, DCLParser.K_NATURAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DCLParser.K_NATURAL:
                    self.state = 316
                    self.match(DCLParser.K_NATURAL)


                self.state = 325
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DCLParser.K_LEFT]:
                    self.state = 319
                    self.match(DCLParser.K_LEFT)
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==DCLParser.K_OUTER:
                        self.state = 320
                        self.match(DCLParser.K_OUTER)


                    pass
                elif token in [DCLParser.K_INNER]:
                    self.state = 323
                    self.match(DCLParser.K_INNER)
                    pass
                elif token in [DCLParser.K_CROSS]:
                    self.state = 324
                    self.match(DCLParser.K_CROSS)
                    pass
                elif token in [DCLParser.K_JOIN]:
                    pass
                else:
                    pass
                self.state = 327
                self.match(DCLParser.K_JOIN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinConstraintRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_joinConstraintRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class JoinUsingConstraintContext(JoinConstraintRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.JoinConstraintRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_USING(self):
            return self.getToken(DCLParser.K_USING, 0)
        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)
        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.IDENT)
            else:
                return self.getToken(DCLParser.IDENT, i)
        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinUsingConstraint" ):
                listener.enterJoinUsingConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinUsingConstraint" ):
                listener.exitJoinUsingConstraint(self)


    class JoinOnConstraintContext(JoinConstraintRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.JoinConstraintRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_ON(self):
            return self.getToken(DCLParser.K_ON, 0)
        def baseExprRule(self):
            return self.getTypedRuleContext(DCLParser.BaseExprRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinOnConstraint" ):
                listener.enterJoinOnConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinOnConstraint" ):
                listener.exitJoinOnConstraint(self)



    def joinConstraintRule(self):

        localctx = DCLParser.JoinConstraintRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_joinConstraintRule)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DCLParser.K_ON]:
                localctx = DCLParser.JoinOnConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(DCLParser.K_ON)
                self.state = 331
                self.baseExprRule(0)
                pass
            elif token in [DCLParser.K_USING]:
                localctx = DCLParser.JoinUsingConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(DCLParser.K_USING)
                self.state = 333
                self.match(DCLParser.OPEN_PAR)
                self.state = 334
                self.match(DCLParser.IDENT)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DCLParser.COMMA:
                    self.state = 335
                    self.match(DCLParser.COMMA)
                    self.state = 336
                    self.match(DCLParser.IDENT)
                    self.state = 341
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 342
                self.match(DCLParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultColumnRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_resultColumnRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StarResultContext(ResultColumnRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.ResultColumnRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(DCLParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStarResult" ):
                listener.enterStarResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStarResult" ):
                listener.exitStarResult(self)


    class ExpressionResultContext(ResultColumnRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.ResultColumnRuleContext
            super().__init__(parser)
            self.columnAlias = None # Token
            self.copyFrom(ctx)

        def booleanExprRule(self):
            return self.getTypedRuleContext(DCLParser.BooleanExprRuleContext,0)

        def IDENT(self):
            return self.getToken(DCLParser.IDENT, 0)
        def K_AS(self):
            return self.getToken(DCLParser.K_AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionResult" ):
                listener.enterExpressionResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionResult" ):
                listener.exitExpressionResult(self)



    def resultColumnRule(self):

        localctx = DCLParser.ResultColumnRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_resultColumnRule)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DCLParser.STAR]:
                localctx = DCLParser.StarResultContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(DCLParser.STAR)
                pass
            elif token in [DCLParser.OPEN_PAR, DCLParser.MINUS, DCLParser.K_NOT, DCLParser.K_NULL, DCLParser.IDENT, DCLParser.NUMERIC_LITERAL, DCLParser.STRING_LITERAL]:
                localctx = DCLParser.ExpressionResultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.booleanExprRule(0)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DCLParser.K_AS or _la==DCLParser.IDENT:
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==DCLParser.K_AS:
                        self.state = 347
                        self.match(DCLParser.K_AS)


                    self.state = 350
                    localctx.columnAlias = self.match(DCLParser.IDENT)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundOperatorRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DCLParser.RULE_compoundOperatorRule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntersectContext(CompoundOperatorRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompoundOperatorRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_INTERSECT(self):
            return self.getToken(DCLParser.K_INTERSECT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntersect" ):
                listener.enterIntersect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntersect" ):
                listener.exitIntersect(self)


    class UnionContext(CompoundOperatorRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompoundOperatorRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_UNION(self):
            return self.getToken(DCLParser.K_UNION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)


    class ExceptContext(CompoundOperatorRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompoundOperatorRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_EXCEPT(self):
            return self.getToken(DCLParser.K_EXCEPT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcept" ):
                listener.enterExcept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcept" ):
                listener.exitExcept(self)


    class UnionAllContext(CompoundOperatorRuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DCLParser.CompoundOperatorRuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_UNION(self):
            return self.getToken(DCLParser.K_UNION, 0)
        def K_ALL(self):
            return self.getToken(DCLParser.K_ALL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionAll" ):
                listener.enterUnionAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionAll" ):
                listener.exitUnionAll(self)



    def compoundOperatorRule(self):

        localctx = DCLParser.CompoundOperatorRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_compoundOperatorRule)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = DCLParser.UnionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(DCLParser.K_UNION)
                pass

            elif la_ == 2:
                localctx = DCLParser.UnionAllContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(DCLParser.K_UNION)
                self.state = 357
                self.match(DCLParser.K_ALL)
                pass

            elif la_ == 3:
                localctx = DCLParser.IntersectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.match(DCLParser.K_INTERSECT)
                pass

            elif la_ == 4:
                localctx = DCLParser.ExceptContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.match(DCLParser.K_EXCEPT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._orderingTermRule = None # OrderingTermRuleContext
            self.expr = list() # of OrderingTermRuleContexts

        def K_ORDER(self):
            return self.getToken(DCLParser.K_ORDER, 0)

        def K_BY(self):
            return self.getToken(DCLParser.K_BY, 0)

        def orderingTermRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.OrderingTermRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.OrderingTermRuleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.COMMA)
            else:
                return self.getToken(DCLParser.COMMA, i)

        def getRuleIndex(self):
            return DCLParser.RULE_orderByClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClauseRule" ):
                listener.enterOrderByClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClauseRule" ):
                listener.exitOrderByClauseRule(self)




    def orderByClauseRule(self):

        localctx = DCLParser.OrderByClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_orderByClauseRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(DCLParser.K_ORDER)
            self.state = 363
            self.match(DCLParser.K_BY)
            self.state = 364
            localctx._orderingTermRule = self.orderingTermRule()
            localctx.expr.append(localctx._orderingTermRule)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 365
                    self.match(DCLParser.COMMA)
                    self.state = 366
                    localctx._orderingTermRule = self.orderingTermRule()
                    localctx.expr.append(localctx._orderingTermRule) 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderingTermRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.column = None # Token
            self.order = None # Token

        def NUMERIC_LITERAL(self):
            return self.getToken(DCLParser.NUMERIC_LITERAL, 0)

        def K_ASC(self):
            return self.getToken(DCLParser.K_ASC, 0)

        def K_DESC(self):
            return self.getToken(DCLParser.K_DESC, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_orderingTermRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderingTermRule" ):
                listener.enterOrderingTermRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderingTermRule" ):
                listener.exitOrderingTermRule(self)




    def orderingTermRule(self):

        localctx = DCLParser.OrderingTermRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_orderingTermRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            localctx.column = self.match(DCLParser.NUMERIC_LITERAL)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.K_ASC or _la==DCLParser.K_DESC:
                self.state = 373
                localctx.order = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==DCLParser.K_ASC or _la==DCLParser.K_DESC):
                    localctx.order = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitClauseRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.limit = None # Token
            self.offset = None # Token

        def K_LIMIT(self):
            return self.getToken(DCLParser.K_LIMIT, 0)

        def NUMERIC_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.NUMERIC_LITERAL)
            else:
                return self.getToken(DCLParser.NUMERIC_LITERAL, i)

        def K_OFFSET(self):
            return self.getToken(DCLParser.K_OFFSET, 0)

        def COMMA(self):
            return self.getToken(DCLParser.COMMA, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_limitClauseRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClauseRule" ):
                listener.enterLimitClauseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClauseRule" ):
                listener.exitLimitClauseRule(self)




    def limitClauseRule(self):

        localctx = DCLParser.LimitClauseRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_limitClauseRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(DCLParser.K_LIMIT)
            self.state = 377
            localctx.limit = self.match(DCLParser.NUMERIC_LITERAL)
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 378
                _la = self._input.LA(1)
                if not(_la==DCLParser.COMMA or _la==DCLParser.K_OFFSET):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 379
                localctx.offset = self.match(DCLParser.NUMERIC_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DCLParser.IDENT)
            else:
                return self.getToken(DCLParser.IDENT, i)

        def OPEN_PAR(self):
            return self.getToken(DCLParser.OPEN_PAR, 0)

        def signedNumberRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCLParser.SignedNumberRuleContext)
            else:
                return self.getTypedRuleContext(DCLParser.SignedNumberRuleContext,i)


        def CLOSE_PAR(self):
            return self.getToken(DCLParser.CLOSE_PAR, 0)

        def COMMA(self):
            return self.getToken(DCLParser.COMMA, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_typeNameRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeNameRule" ):
                listener.enterTypeNameRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeNameRule" ):
                listener.exitTypeNameRule(self)




    def typeNameRule(self):

        localctx = DCLParser.TypeNameRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typeNameRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 382
                self.match(DCLParser.IDENT)
                self.state = 385 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DCLParser.IDENT):
                    break

            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 387
                self.match(DCLParser.OPEN_PAR)
                self.state = 388
                self.signedNumberRule()
                self.state = 389
                self.match(DCLParser.CLOSE_PAR)

            elif la_ == 2:
                self.state = 391
                self.match(DCLParser.OPEN_PAR)
                self.state = 392
                self.signedNumberRule()
                self.state = 393
                self.match(DCLParser.COMMA)
                self.state = 394
                self.signedNumberRule()
                self.state = 395
                self.match(DCLParser.CLOSE_PAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedNumberRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC_LITERAL(self):
            return self.getToken(DCLParser.NUMERIC_LITERAL, 0)

        def PLUS(self):
            return self.getToken(DCLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(DCLParser.MINUS, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_signedNumberRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedNumberRule" ):
                listener.enterSignedNumberRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedNumberRule" ):
                listener.exitSignedNumberRule(self)




    def signedNumberRule(self):

        localctx = DCLParser.SignedNumberRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_signedNumberRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DCLParser.PLUS or _la==DCLParser.MINUS:
                self.state = 399
                _la = self._input.LA(1)
                if not(_la==DCLParser.PLUS or _la==DCLParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 402
            self.match(DCLParser.NUMERIC_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ALL(self):
            return self.getToken(DCLParser.K_ALL, 0)

        def K_AND(self):
            return self.getToken(DCLParser.K_AND, 0)

        def K_AS(self):
            return self.getToken(DCLParser.K_AS, 0)

        def K_ASC(self):
            return self.getToken(DCLParser.K_ASC, 0)

        def K_BETWEEN(self):
            return self.getToken(DCLParser.K_BETWEEN, 0)

        def K_BY(self):
            return self.getToken(DCLParser.K_BY, 0)

        def K_CASE(self):
            return self.getToken(DCLParser.K_CASE, 0)

        def K_CAST(self):
            return self.getToken(DCLParser.K_CAST, 0)

        def K_CROSS(self):
            return self.getToken(DCLParser.K_CROSS, 0)

        def K_DESC(self):
            return self.getToken(DCLParser.K_DESC, 0)

        def K_DISTINCT(self):
            return self.getToken(DCLParser.K_DISTINCT, 0)

        def K_DROP(self):
            return self.getToken(DCLParser.K_DROP, 0)

        def K_ELSE(self):
            return self.getToken(DCLParser.K_ELSE, 0)

        def K_END(self):
            return self.getToken(DCLParser.K_END, 0)

        def K_ESCAPE(self):
            return self.getToken(DCLParser.K_ESCAPE, 0)

        def K_EXCEPT(self):
            return self.getToken(DCLParser.K_EXCEPT, 0)

        def K_FROM(self):
            return self.getToken(DCLParser.K_FROM, 0)

        def K_GLOB(self):
            return self.getToken(DCLParser.K_GLOB, 0)

        def K_GROUP(self):
            return self.getToken(DCLParser.K_GROUP, 0)

        def K_HAVING(self):
            return self.getToken(DCLParser.K_HAVING, 0)

        def K_IN(self):
            return self.getToken(DCLParser.K_IN, 0)

        def K_INNER(self):
            return self.getToken(DCLParser.K_INNER, 0)

        def K_INTERSECT(self):
            return self.getToken(DCLParser.K_INTERSECT, 0)

        def K_IS(self):
            return self.getToken(DCLParser.K_IS, 0)

        def K_ISNULL(self):
            return self.getToken(DCLParser.K_ISNULL, 0)

        def K_JOIN(self):
            return self.getToken(DCLParser.K_JOIN, 0)

        def K_LEFT(self):
            return self.getToken(DCLParser.K_LEFT, 0)

        def K_LIKE(self):
            return self.getToken(DCLParser.K_LIKE, 0)

        def K_LIMIT(self):
            return self.getToken(DCLParser.K_LIMIT, 0)

        def K_MATCH(self):
            return self.getToken(DCLParser.K_MATCH, 0)

        def K_NATURAL(self):
            return self.getToken(DCLParser.K_NATURAL, 0)

        def K_NOT(self):
            return self.getToken(DCLParser.K_NOT, 0)

        def K_NOTNULL(self):
            return self.getToken(DCLParser.K_NOTNULL, 0)

        def K_NULL(self):
            return self.getToken(DCLParser.K_NULL, 0)

        def K_OFFSET(self):
            return self.getToken(DCLParser.K_OFFSET, 0)

        def K_ON(self):
            return self.getToken(DCLParser.K_ON, 0)

        def K_OR(self):
            return self.getToken(DCLParser.K_OR, 0)

        def K_ORDER(self):
            return self.getToken(DCLParser.K_ORDER, 0)

        def K_OUTER(self):
            return self.getToken(DCLParser.K_OUTER, 0)

        def K_RECURSIVE(self):
            return self.getToken(DCLParser.K_RECURSIVE, 0)

        def K_REGEXP(self):
            return self.getToken(DCLParser.K_REGEXP, 0)

        def K_SELECT(self):
            return self.getToken(DCLParser.K_SELECT, 0)

        def K_THEN(self):
            return self.getToken(DCLParser.K_THEN, 0)

        def K_UNION(self):
            return self.getToken(DCLParser.K_UNION, 0)

        def K_UNIQUE(self):
            return self.getToken(DCLParser.K_UNIQUE, 0)

        def K_USING(self):
            return self.getToken(DCLParser.K_USING, 0)

        def K_VALUES(self):
            return self.getToken(DCLParser.K_VALUES, 0)

        def K_WHEN(self):
            return self.getToken(DCLParser.K_WHEN, 0)

        def K_WHERE(self):
            return self.getToken(DCLParser.K_WHERE, 0)

        def K_WITH(self):
            return self.getToken(DCLParser.K_WITH, 0)

        def K_YEAR(self):
            return self.getToken(DCLParser.K_YEAR, 0)

        def K_MONTH(self):
            return self.getToken(DCLParser.K_MONTH, 0)

        def K_DAY(self):
            return self.getToken(DCLParser.K_DAY, 0)

        def K_HOUR(self):
            return self.getToken(DCLParser.K_HOUR, 0)

        def K_MINUTE(self):
            return self.getToken(DCLParser.K_MINUTE, 0)

        def K_SECOND(self):
            return self.getToken(DCLParser.K_SECOND, 0)

        def getRuleIndex(self):
            return DCLParser.RULE_keywordRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordRule" ):
                listener.enterKeywordRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordRule" ):
                listener.exitKeywordRule(self)




    def keywordRule(self):

        localctx = DCLParser.KeywordRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_keywordRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            _la = self._input.LA(1)
            if not(((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & ((1 << (DCLParser.K_ALL - 30)) | (1 << (DCLParser.K_AND - 30)) | (1 << (DCLParser.K_AS - 30)) | (1 << (DCLParser.K_ASC - 30)) | (1 << (DCLParser.K_BETWEEN - 30)) | (1 << (DCLParser.K_BY - 30)) | (1 << (DCLParser.K_CASE - 30)) | (1 << (DCLParser.K_CAST - 30)) | (1 << (DCLParser.K_CROSS - 30)) | (1 << (DCLParser.K_DESC - 30)) | (1 << (DCLParser.K_DISTINCT - 30)) | (1 << (DCLParser.K_DROP - 30)) | (1 << (DCLParser.K_ELSE - 30)) | (1 << (DCLParser.K_END - 30)) | (1 << (DCLParser.K_ESCAPE - 30)) | (1 << (DCLParser.K_EXCEPT - 30)) | (1 << (DCLParser.K_FROM - 30)) | (1 << (DCLParser.K_GLOB - 30)) | (1 << (DCLParser.K_GROUP - 30)) | (1 << (DCLParser.K_HAVING - 30)) | (1 << (DCLParser.K_IN - 30)) | (1 << (DCLParser.K_INNER - 30)) | (1 << (DCLParser.K_INTERSECT - 30)) | (1 << (DCLParser.K_IS - 30)) | (1 << (DCLParser.K_ISNULL - 30)) | (1 << (DCLParser.K_JOIN - 30)) | (1 << (DCLParser.K_LEFT - 30)) | (1 << (DCLParser.K_LIKE - 30)) | (1 << (DCLParser.K_LIMIT - 30)) | (1 << (DCLParser.K_MATCH - 30)) | (1 << (DCLParser.K_NATURAL - 30)) | (1 << (DCLParser.K_NOT - 30)) | (1 << (DCLParser.K_NOTNULL - 30)) | (1 << (DCLParser.K_NULL - 30)) | (1 << (DCLParser.K_OFFSET - 30)) | (1 << (DCLParser.K_ON - 30)) | (1 << (DCLParser.K_OR - 30)) | (1 << (DCLParser.K_ORDER - 30)) | (1 << (DCLParser.K_OUTER - 30)) | (1 << (DCLParser.K_RECURSIVE - 30)) | (1 << (DCLParser.K_REGEXP - 30)) | (1 << (DCLParser.K_SELECT - 30)) | (1 << (DCLParser.K_THEN - 30)) | (1 << (DCLParser.K_UNION - 30)) | (1 << (DCLParser.K_UNIQUE - 30)) | (1 << (DCLParser.K_USING - 30)) | (1 << (DCLParser.K_VALUES - 30)) | (1 << (DCLParser.K_WHEN - 30)) | (1 << (DCLParser.K_WHERE - 30)) | (1 << (DCLParser.K_WITH - 30)) | (1 << (DCLParser.K_YEAR - 30)) | (1 << (DCLParser.K_MONTH - 30)) | (1 << (DCLParser.K_DAY - 30)) | (1 << (DCLParser.K_HOUR - 30)) | (1 << (DCLParser.K_MINUTE - 30)) | (1 << (DCLParser.K_SECOND - 30)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.booleanExprRule_sempred
        self._predicates[3] = self.baseExprRule_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def booleanExprRule_sempred(self, localctx:BooleanExprRuleContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def baseExprRule_sempred(self, localctx:BaseExprRuleContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         




