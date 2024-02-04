# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01e7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\177\n\3\3\4\3\4")
        buf.write("\5\4\u0083\n\4\3\5\3\5\3\5\5\5\u0088\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0095\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00a1\n\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ab\n\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u00b2\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00bb")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c6")
        buf.write("\n\13\3\f\3\f\5\f\u00ca\n\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d9\n\17\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00df\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00ea\n\21\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00f0\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u0100\n")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u011c\n\31\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0122\n\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3!\3!\5!\u013b\n!\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u0142\n\"\3#\3#\3#\3#\3#\3#\7#\u014a\n#\f#\16#\u014d")
        buf.write("\13#\3$\3$\3$\3$\3$\3$\7$\u0155\n$\f$\16$\u0158\13$\3")
        buf.write("%\3%\3%\3%\3%\3%\7%\u0160\n%\f%\16%\u0163\13%\3&\3&\3")
        buf.write("&\5&\u0168\n&\3\'\3\'\3\'\5\'\u016d\n\'\3(\3(\3(\3(\3")
        buf.write("(\7(\u0174\n(\f(\16(\u0177\13(\3)\3)\3)\3)\3)\3)\5)\u017f")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\5+\u0187\n+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\5,\u0192\n,\3-\3-\5-\u0196\n-\3.\3.\3.\3.\3.\5")
        buf.write(".\u019d\n.\3/\3/\3\60\3\60\3\60\3\60\5\60\u01a5\n\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\63\5\63\u01ae\n\63\3\64")
        buf.write("\3\64\3\64\5\64\u01b3\n\64\3\65\3\65\3\65\5\65\u01b8\n")
        buf.write("\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u01c4\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u01cb\n")
        buf.write("\67\38\38\38\38\39\39\59\u01d3\n9\3:\3:\3:\3:\3:\5:\u01da")
        buf.write("\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u01e5\n;\3;\2\6DFHN")
        buf.write("<\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt\2\n\4\2\24\24\27")
        buf.write("\34\3\2\35\37\3\2 $\3\2\21\23\3\2\35\36\3\2!\"\4\2  #")
        buf.write("$\3\2%&\2\u01e4\2v\3\2\2\2\4~\3\2\2\2\6\u0082\3\2\2\2")
        buf.write("\b\u0087\3\2\2\2\n\u0094\3\2\2\2\f\u0096\3\2\2\2\16\u009c")
        buf.write("\3\2\2\2\20\u00b1\3\2\2\2\22\u00b3\3\2\2\2\24\u00be\3")
        buf.write("\2\2\2\26\u00c9\3\2\2\2\30\u00cb\3\2\2\2\32\u00cf\3\2")
        buf.write("\2\2\34\u00d8\3\2\2\2\36\u00de\3\2\2\2 \u00e9\3\2\2\2")
        buf.write("\"\u00ef\3\2\2\2$\u00f1\3\2\2\2&\u00f7\3\2\2\2(\u00fd")
        buf.write("\3\2\2\2*\u0103\3\2\2\2,\u0106\3\2\2\2.\u010f\3\2\2\2")
        buf.write("\60\u0112\3\2\2\2\62\u0121\3\2\2\2\64\u0123\3\2\2\2\66")
        buf.write("\u0128\3\2\2\28\u012d\3\2\2\2:\u012f\3\2\2\2<\u0131\3")
        buf.write("\2\2\2>\u0133\3\2\2\2@\u013a\3\2\2\2B\u0141\3\2\2\2D\u0143")
        buf.write("\3\2\2\2F\u014e\3\2\2\2H\u0159\3\2\2\2J\u0167\3\2\2\2")
        buf.write("L\u016c\3\2\2\2N\u016e\3\2\2\2P\u017e\3\2\2\2R\u0180\3")
        buf.write("\2\2\2T\u0186\3\2\2\2V\u0191\3\2\2\2X\u0195\3\2\2\2Z\u019c")
        buf.write("\3\2\2\2\\\u019e\3\2\2\2^\u01a4\3\2\2\2`\u01a6\3\2\2\2")
        buf.write("b\u01a8\3\2\2\2d\u01ad\3\2\2\2f\u01b2\3\2\2\2h\u01b7\3")
        buf.write("\2\2\2j\u01c3\3\2\2\2l\u01ca\3\2\2\2n\u01cc\3\2\2\2p\u01d2")
        buf.write("\3\2\2\2r\u01d9\3\2\2\2t\u01e4\3\2\2\2vw\5d\63\2wx\5\4")
        buf.write("\3\2xy\7\2\2\3y\3\3\2\2\2z{\5\6\4\2{|\5\4\3\2|\177\3\2")
        buf.write("\2\2}\177\5\6\4\2~z\3\2\2\2~}\3\2\2\2\177\5\3\2\2\2\u0080")
        buf.write("\u0083\5\b\5\2\u0081\u0083\5\20\t\2\u0082\u0080\3\2\2")
        buf.write("\2\u0082\u0081\3\2\2\2\u0083\7\3\2\2\2\u0084\u0088\5\n")
        buf.write("\6\2\u0085\u0088\5\f\7\2\u0086\u0088\5\16\b\2\u0087\u0084")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\t\3\2\2\2\u0089\u008a\5> \2\u008a\u008b\7/\2\2\u008b")
        buf.write("\u008c\7\26\2\2\u008c\u008d\5@!\2\u008d\u008e\5f\64\2")
        buf.write("\u008e\u0095\3\2\2\2\u008f\u0090\5> \2\u0090\u0091\7/")
        buf.write("\2\2\u0091\u0092\5f\64\2\u0092\u0095\3\2\2\2\u0093\u0095")
        buf.write("\5\22\n\2\u0094\u0089\3\2\2\2\u0094\u008f\3\2\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095\13\3\2\2\2\u0096\u0097\7\4\2\2\u0097")
        buf.write("\u0098\7/\2\2\u0098\u0099\7\26\2\2\u0099\u009a\5@!\2\u009a")
        buf.write("\u009b\5f\64\2\u009b\r\3\2\2\2\u009c\u009d\7\5\2\2\u009d")
        buf.write("\u00a0\7/\2\2\u009e\u009f\7\26\2\2\u009f\u00a1\5@!\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\5f\64\2\u00a3\17\3\2\2\2\u00a4\u00a5\7\6")
        buf.write("\2\2\u00a5\u00a6\7/\2\2\u00a6\u00a7\5n8\2\u00a7\u00aa")
        buf.write("\5d\63\2\u00a8\u00ab\5(\25\2\u00a9\u00ab\5$\23\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00b2\3\2\2\2")
        buf.write("\u00ac\u00ad\7\6\2\2\u00ad\u00ae\7/\2\2\u00ae\u00af\5")
        buf.write("n8\2\u00af\u00b0\5f\64\2\u00b0\u00b2\3\2\2\2\u00b1\u00a4")
        buf.write("\3\2\2\2\u00b1\u00ac\3\2\2\2\u00b2\21\3\2\2\2\u00b3\u00b4")
        buf.write("\5> \2\u00b4\u00b5\7/\2\2\u00b5\u00b6\7)\2\2\u00b6\u00b7")
        buf.write("\5\36\20\2\u00b7\u00ba\7*\2\2\u00b8\u00b9\7\26\2\2\u00b9")
        buf.write("\u00bb\5\26\f\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\5f\64\2\u00bd\23\3")
        buf.write("\2\2\2\u00be\u00bf\5> \2\u00bf\u00c0\7/\2\2\u00c0\u00c1")
        buf.write("\7)\2\2\u00c1\u00c2\5\36\20\2\u00c2\u00c5\7*\2\2\u00c3")
        buf.write("\u00c4\7\26\2\2\u00c4\u00c6\5\26\f\2\u00c5\u00c3\3\2\2")
        buf.write("\2\u00c5\u00c6\3\2\2\2\u00c6\25\3\2\2\2\u00c7\u00ca\5")
        buf.write("\30\r\2\u00c8\u00ca\5\32\16\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\27\3\2\2\2\u00cb\u00cc\7)\2\2\u00cc")
        buf.write("\u00cd\5l\67\2\u00cd\u00ce\7*\2\2\u00ce\31\3\2\2\2\u00cf")
        buf.write("\u00d0\7)\2\2\u00d0\u00d1\5\34\17\2\u00d1\u00d2\7*\2\2")
        buf.write("\u00d2\33\3\2\2\2\u00d3\u00d4\5\30\r\2\u00d4\u00d5\7-")
        buf.write("\2\2\u00d5\u00d6\5\34\17\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9")
        buf.write("\5\30\r\2\u00d8\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\35\3\2\2\2\u00da\u00db\7\60\2\2\u00db\u00dc\7-\2\2\u00dc")
        buf.write("\u00df\5\36\20\2\u00dd\u00df\7\60\2\2\u00de\u00da\3\2")
        buf.write("\2\2\u00de\u00dd\3\2\2\2\u00df\37\3\2\2\2\u00e0\u00ea")
        buf.write("\5\b\5\2\u00e1\u00ea\5\66\34\2\u00e2\u00ea\5\60\31\2\u00e3")
        buf.write("\u00ea\5,\27\2\u00e4\u00ea\5.\30\2\u00e5\u00ea\5*\26\2")
        buf.write("\u00e6\u00ea\5(\25\2\u00e7\u00ea\5&\24\2\u00e8\u00ea\5")
        buf.write("$\23\2\u00e9\u00e0\3\2\2\2\u00e9\u00e1\3\2\2\2\u00e9\u00e2")
        buf.write("\3\2\2\2\u00e9\u00e3\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9")
        buf.write("\u00e5\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00ea!\3\2\2\2\u00eb\u00ec\5 \21")
        buf.write("\2\u00ec\u00ed\5\"\22\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0")
        buf.write("\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("#\3\2\2\2\u00f1\u00f2\7\17\2\2\u00f2\u00f3\5f\64\2\u00f3")
        buf.write("\u00f4\5\"\22\2\u00f4\u00f5\7\20\2\2\u00f5\u00f6\5f\64")
        buf.write("\2\u00f6%\3\2\2\2\u00f7\u00f8\7/\2\2\u00f8\u00f9\7\'\2")
        buf.write("\2\u00f9\u00fa\5X-\2\u00fa\u00fb\7(\2\2\u00fb\u00fc\5")
        buf.write("d\63\2\u00fc\'\3\2\2\2\u00fd\u00ff\7\3\2\2\u00fe\u0100")
        buf.write("\5@!\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u0102\5f\64\2\u0102)\3\2\2\2\u0103\u0104")
        buf.write("\7\13\2\2\u0104\u0105\5f\64\2\u0105+\3\2\2\2\u0106\u0107")
        buf.write("\7\7\2\2\u0107\u0108\5b\62\2\u0108\u0109\7\b\2\2\u0109")
        buf.write("\u010a\5@!\2\u010a\u010b\7\t\2\2\u010b\u010c\5@!\2\u010c")
        buf.write("\u010d\5d\63\2\u010d\u010e\5 \21\2\u010e-\3\2\2\2\u010f")
        buf.write("\u0110\7\n\2\2\u0110\u0111\5f\64\2\u0111/\3\2\2\2\u0112")
        buf.write("\u0113\7\f\2\2\u0113\u0114\7\'\2\2\u0114\u0115\5@!\2\u0115")
        buf.write("\u0116\7(\2\2\u0116\u0117\5d\63\2\u0117\u0118\5 \21\2")
        buf.write("\u0118\u011b\5\62\32\2\u0119\u011a\7\r\2\2\u011a\u011c")
        buf.write("\5 \21\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\61\3\2\2\2\u011d\u011e\5\64\33\2\u011e\u011f\5\62\32")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u011d")
        buf.write("\3\2\2\2\u0121\u0120\3\2\2\2\u0122\63\3\2\2\2\u0123\u0124")
        buf.write("\7\16\2\2\u0124\u0125\5@!\2\u0125\u0126\5d\63\2\u0126")
        buf.write("\u0127\5 \21\2\u0127\65\3\2\2\2\u0128\u0129\5h\65\2\u0129")
        buf.write("\u012a\7\26\2\2\u012a\u012b\5@!\2\u012b\u012c\5f\64\2")
        buf.write("\u012c\67\3\2\2\2\u012d\u012e\t\2\2\2\u012e9\3\2\2\2\u012f")
        buf.write("\u0130\t\3\2\2\u0130;\3\2\2\2\u0131\u0132\t\4\2\2\u0132")
        buf.write("=\3\2\2\2\u0133\u0134\t\5\2\2\u0134?\3\2\2\2\u0135\u0136")
        buf.write("\5B\"\2\u0136\u0137\7\25\2\2\u0137\u0138\5B\"\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u013b\5B\"\2\u013a\u0135\3\2\2\2")
        buf.write("\u013a\u0139\3\2\2\2\u013bA\3\2\2\2\u013c\u013d\5D#\2")
        buf.write("\u013d\u013e\58\35\2\u013e\u013f\5D#\2\u013f\u0142\3\2")
        buf.write("\2\2\u0140\u0142\5D#\2\u0141\u013c\3\2\2\2\u0141\u0140")
        buf.write("\3\2\2\2\u0142C\3\2\2\2\u0143\u0144\b#\1\2\u0144\u0145")
        buf.write("\5F$\2\u0145\u014b\3\2\2\2\u0146\u0147\f\4\2\2\u0147\u0148")
        buf.write("\t\6\2\2\u0148\u014a\5F$\2\u0149\u0146\3\2\2\2\u014a\u014d")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("E\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\b$\1\2\u014f")
        buf.write("\u0150\5H%\2\u0150\u0156\3\2\2\2\u0151\u0152\f\4\2\2\u0152")
        buf.write("\u0153\t\7\2\2\u0153\u0155\5H%\2\u0154\u0151\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157G\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\b%\1\2")
        buf.write("\u015a\u015b\5J&\2\u015b\u0161\3\2\2\2\u015c\u015d\f\4")
        buf.write("\2\2\u015d\u015e\t\b\2\2\u015e\u0160\5J&\2\u015f\u015c")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162I\3\2\2\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0165\7\37\2\2\u0165\u0168\5J&\2\u0166\u0168\5L\'\2\u0167")
        buf.write("\u0164\3\2\2\2\u0167\u0166\3\2\2\2\u0168K\3\2\2\2\u0169")
        buf.write("\u016a\7\"\2\2\u016a\u016d\5L\'\2\u016b\u016d\5N(\2\u016c")
        buf.write("\u0169\3\2\2\2\u016c\u016b\3\2\2\2\u016dM\3\2\2\2\u016e")
        buf.write("\u016f\b(\1\2\u016f\u0170\5P)\2\u0170\u0175\3\2\2\2\u0171")
        buf.write("\u0172\f\4\2\2\u0172\u0174\5T+\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176O\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017f\7/\2\2")
        buf.write("\u0179\u017f\5&\24\2\u017a\u017f\5^\60\2\u017b\u017f\5")
        buf.write("\26\f\2\u017c\u017f\5T+\2\u017d\u017f\5R*\2\u017e\u0178")
        buf.write("\3\2\2\2\u017e\u0179\3\2\2\2\u017e\u017a\3\2\2\2\u017e")
        buf.write("\u017b\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2")
        buf.write("\u017fQ\3\2\2\2\u0180\u0181\7\'\2\2\u0181\u0182\5@!\2")
        buf.write("\u0182\u0183\7(\2\2\u0183S\3\2\2\2\u0184\u0187\7/\2\2")
        buf.write("\u0185\u0187\5&\24\2\u0186\u0184\3\2\2\2\u0186\u0185\3")
        buf.write("\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7)\2\2\u0189\u018a")
        buf.write("\5V,\2\u018a\u018b\7*\2\2\u018bU\3\2\2\2\u018c\u0192\5")
        buf.write("@!\2\u018d\u018e\5@!\2\u018e\u018f\7-\2\2\u018f\u0190")
        buf.write("\5V,\2\u0190\u0192\3\2\2\2\u0191\u018c\3\2\2\2\u0191\u018d")
        buf.write("\3\2\2\2\u0192W\3\2\2\2\u0193\u0196\5Z.\2\u0194\u0196")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("Y\3\2\2\2\u0197\u0198\5\\/\2\u0198\u0199\7-\2\2\u0199")
        buf.write("\u019a\5Z.\2\u019a\u019d\3\2\2\2\u019b\u019d\5\\/\2\u019c")
        buf.write("\u0197\3\2\2\2\u019c\u019b\3\2\2\2\u019d[\3\2\2\2\u019e")
        buf.write("\u019f\5@!\2\u019f]\3\2\2\2\u01a0\u01a5\7\61\2\2\u01a1")
        buf.write("\u01a5\7\60\2\2\u01a2\u01a5\7/\2\2\u01a3\u01a5\5`\61\2")
        buf.write("\u01a4\u01a0\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a3\3\2\2\2\u01a5_\3\2\2\2\u01a6\u01a7")
        buf.write("\t\t\2\2\u01a7a\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9c\3\2")
        buf.write("\2\2\u01aa\u01ab\7\64\2\2\u01ab\u01ae\5d\63\2\u01ac\u01ae")
        buf.write("\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("e\3\2\2\2\u01af\u01b0\7\64\2\2\u01b0\u01b3\5f\64\2\u01b1")
        buf.write("\u01b3\7\64\2\2\u01b2\u01af\3\2\2\2\u01b2\u01b1\3\2\2")
        buf.write("\2\u01b3g\3\2\2\2\u01b4\u01b8\7/\2\2\u01b5\u01b8\5j\66")
        buf.write("\2\u01b6\u01b8\5T+\2\u01b7\u01b4\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b7\u01b6\3\2\2\2\u01b8i\3\2\2\2\u01b9\u01ba")
        buf.write("\7/\2\2\u01ba\u01bb\7)\2\2\u01bb\u01bc\5l\67\2\u01bc\u01bd")
        buf.write("\7*\2\2\u01bd\u01c4\3\2\2\2\u01be\u01bf\7/\2\2\u01bf\u01c0")
        buf.write("\7)\2\2\u01c0\u01c1\5j\66\2\u01c1\u01c2\7*\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01b9\3\2\2\2\u01c3\u01be\3\2\2\2\u01c4")
        buf.write("k\3\2\2\2\u01c5\u01c6\5@!\2\u01c6\u01c7\7-\2\2\u01c7\u01c8")
        buf.write("\5l\67\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb\5@!\2\u01ca\u01c5")
        buf.write("\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cbm\3\2\2\2\u01cc\u01cd")
        buf.write("\7\'\2\2\u01cd\u01ce\5p9\2\u01ce\u01cf\7(\2\2\u01cfo\3")
        buf.write("\2\2\2\u01d0\u01d3\5r:\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3q\3\2\2\2\u01d4\u01d5")
        buf.write("\5t;\2\u01d5\u01d6\7-\2\2\u01d6\u01d7\5r:\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01da\5t;\2\u01d9\u01d4\3\2\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01das\3\2\2\2\u01db\u01dc\5> \2\u01dc\u01dd")
        buf.write("\7/\2\2\u01dd\u01e5\3\2\2\2\u01de\u01df\5> \2\u01df\u01e0")
        buf.write("\7/\2\2\u01e0\u01e1\7)\2\2\u01e1\u01e2\7*\2\2\u01e2\u01e5")
        buf.write("\3\2\2\2\u01e3\u01e5\5\24\13\2\u01e4\u01db\3\2\2\2\u01e4")
        buf.write("\u01de\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5u\3\2\2\2)~\u0082")
        buf.write("\u0087\u0094\u00a0\u00aa\u00b1\u00ba\u00c5\u00c9\u00d8")
        buf.write("\u00de\u00e9\u00ef\u00ff\u011b\u0121\u013a\u0141\u014b")
        buf.write("\u0156\u0161\u0167\u016c\u0175\u017e\u0186\u0191\u0195")
        buf.write("\u019c\u01a4\u01ad\u01b2\u01b7\u01c3\u01ca\u01d2\u01d9")
        buf.write("\u01e4")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'number'", 
                     "'boolean'", "'string'", "'=='", "'...'", "'<-'", "'>='", 
                     "'>'", "'<='", "'<'", "'!='", "'='", "'or'", "'and'", 
                     "'not'", "'%'", "'+'", "'-'", "'*'", "'/'", "'true'", 
                     "'false'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", 
                      "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", "BY_KEY", "BREAK_KEY", 
                      "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", "ELIF_KEY", 
                      "BEGIN_KEY", "END_KEY", "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "EQUAL_OPERATOR", "CONCAT_OPERATOR", "ASSIGN1_OPERATOR", 
                      "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", 
                      "NE_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
                      "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", 
                      "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                      "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", "RB", "LSB", 
                      "RSB", "LPT", "RPT", "COMMA", "COMMENT", "ID", "NUMBER", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "NEW_LINE", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_typdecl = 4
    RULE_varkeydecl = 5
    RULE_dynamicdecl = 6
    RULE_funcdecl = 7
    RULE_arraydecl = 8
    RULE_arrayparameter = 9
    RULE_arrayvalue = 10
    RULE_arrayval = 11
    RULE_arrayvallist = 12
    RULE_listarrayval = 13
    RULE_sizelist = 14
    RULE_statement = 15
    RULE_stmtlist = 16
    RULE_blockstmt = 17
    RULE_funccallstmt = 18
    RULE_returnstmt = 19
    RULE_continuestmt = 20
    RULE_forstmt = 21
    RULE_breakstmt = 22
    RULE_ifstmt = 23
    RULE_eliflist = 24
    RULE_elifcomponent = 25
    RULE_assignstmt = 26
    RULE_relationaloperator = 27
    RULE_logicoperator = 28
    RULE_arithmeticoperator = 29
    RULE_typ = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_expr3 = 34
    RULE_expr4 = 35
    RULE_expr5 = 36
    RULE_expr6 = 37
    RULE_expr7 = 38
    RULE_expr8 = 39
    RULE_subexpr = 40
    RULE_indexoperator = 41
    RULE_indexope = 42
    RULE_argumentlist = 43
    RULE_argumentprime = 44
    RULE_argument = 45
    RULE_literal = 46
    RULE_booleanvalue = 47
    RULE_numbervariable = 48
    RULE_newlinelist = 49
    RULE_newlinelistnonull = 50
    RULE_lhs = 51
    RULE_indexexpr = 52
    RULE_index = 53
    RULE_paralist = 54
    RULE_parameterlist = 55
    RULE_paraprime = 56
    RULE_para = 57

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "typdecl", 
                   "varkeydecl", "dynamicdecl", "funcdecl", "arraydecl", 
                   "arrayparameter", "arrayvalue", "arrayval", "arrayvallist", 
                   "listarrayval", "sizelist", "statement", "stmtlist", 
                   "blockstmt", "funccallstmt", "returnstmt", "continuestmt", 
                   "forstmt", "breakstmt", "ifstmt", "eliflist", "elifcomponent", 
                   "assignstmt", "relationaloperator", "logicoperator", 
                   "arithmeticoperator", "typ", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "subexpr", "indexoperator", "indexope", "argumentlist", 
                   "argumentprime", "argument", "literal", "booleanvalue", 
                   "numbervariable", "newlinelist", "newlinelistnonull", 
                   "lhs", "indexexpr", "index", "paralist", "parameterlist", 
                   "paraprime", "para" ]

    EOF = Token.EOF
    RETURN_KEY=1
    VAR_KEY=2
    DYNAMIC_KEY=3
    FUNC_KEY=4
    FOR_KEY=5
    UNTIL_KEY=6
    BY_KEY=7
    BREAK_KEY=8
    CONTINUE_KEY=9
    IF_KEY=10
    ELSE_KEY=11
    ELIF_KEY=12
    BEGIN_KEY=13
    END_KEY=14
    NUM_TYPE=15
    BOOL_TYPE=16
    STRING_TYPE=17
    EQUAL_OPERATOR=18
    CONCAT_OPERATOR=19
    ASSIGN1_OPERATOR=20
    GE_OPERATOR=21
    G_OPERATOR=22
    LE_OPERATOR=23
    L_OPERATOR=24
    NE_OPERATOR=25
    ASSIGN2_OPERATOR=26
    OR_OPERATOR=27
    AND_OPERATOR=28
    NOT_OPERATOR=29
    MODULO_OPERATOR=30
    ADD_OPERATOR=31
    SUB_OPERATOR=32
    MUL_OPERATOR=33
    DIV_OPERATOR=34
    TRUE_BOOLEAN=35
    FALSE_BOOLEAN=36
    LB=37
    RB=38
    LSB=39
    RSB=40
    LPT=41
    RPT=42
    COMMA=43
    COMMENT=44
    ID=45
    NUMBER=46
    STRINGLIT=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    NEW_LINE=50
    WS=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.newlinelist()
            self.state = 117
            self.decllist()
            self.state = 118
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.decl()
                self.state = 121
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.funcdecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypdeclContext,0)


        def varkeydecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarkeydeclContext,0)


        def dynamicdecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.varkeydecl()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.dynamicdecl()
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


    class TypdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypdecl" ):
                return visitor.visitTypdecl(self)
            else:
                return visitor.visitChildren(self)




    def typdecl(self):

        localctx = ZCodeParser.TypdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typdecl)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.typ()
                self.state = 136
                self.match(ZCodeParser.ID)
                self.state = 137
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 138
                self.expr()
                self.state = 139
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.typ()
                self.state = 142
                self.match(ZCodeParser.ID)
                self.state = 143
                self.newlinelistnonull()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarkeydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KEY(self):
            return self.getToken(ZCodeParser.VAR_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varkeydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarkeydecl" ):
                return visitor.visitVarkeydecl(self)
            else:
                return visitor.visitChildren(self)




    def varkeydecl(self):

        localctx = ZCodeParser.VarkeydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varkeydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.VAR_KEY)
            self.state = 149
            self.match(ZCodeParser.ID)
            self.state = 150
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 151
            self.expr()
            self.state = 152
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC_KEY(self):
            return self.getToken(ZCodeParser.DYNAMIC_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamicdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamicdecl" ):
                return visitor.visitDynamicdecl(self)
            else:
                return visitor.visitChildren(self)




    def dynamicdecl(self):

        localctx = ZCodeParser.DynamicdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dynamicdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.DYNAMIC_KEY)
            self.state = 155
            self.match(ZCodeParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 156
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 157
                self.expr()


            self.state = 160
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEY(self):
            return self.getToken(ZCodeParser.FUNC_KEY, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def paralist(self):
            return self.getTypedRuleContext(ZCodeParser.ParalistContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 163
                self.match(ZCodeParser.ID)
                self.state = 164
                self.paralist()
                self.state = 165
                self.newlinelist()
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN_KEY]:
                    self.state = 166
                    self.returnstmt()
                    pass
                elif token in [ZCodeParser.BEGIN_KEY]:
                    self.state = 167
                    self.blockstmt()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 171
                self.match(ZCodeParser.ID)
                self.state = 172
                self.paralist()
                self.state = 173
                self.newlinelistnonull()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.typ()
            self.state = 178
            self.match(ZCodeParser.ID)
            self.state = 179
            self.match(ZCodeParser.LSB)
            self.state = 180
            self.sizelist()
            self.state = 181
            self.match(ZCodeParser.RSB)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 182
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 183
                self.arrayvalue()


            self.state = 186
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayparameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayparameter" ):
                return visitor.visitArrayparameter(self)
            else:
                return visitor.visitChildren(self)




    def arrayparameter(self):

        localctx = ZCodeParser.ArrayparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayparameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.typ()
            self.state = 189
            self.match(ZCodeParser.ID)
            self.state = 190
            self.match(ZCodeParser.LSB)
            self.state = 191
            self.sizelist()
            self.state = 192
            self.match(ZCodeParser.RSB)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 193
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 194
                self.arrayvalue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalContext,0)


        def arrayvallist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvallistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvalue" ):
                return visitor.visitArrayvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayvalue)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.arrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.arrayvallist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayval" ):
                return visitor.visitArrayval(self)
            else:
                return visitor.visitChildren(self)




    def arrayval(self):

        localctx = ZCodeParser.ArrayvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ZCodeParser.LSB)
            self.state = 202
            self.index()
            self.state = 203
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def listarrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ListarrayvalContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvallist" ):
                return visitor.visitArrayvallist(self)
            else:
                return visitor.visitChildren(self)




    def arrayvallist(self):

        localctx = ZCodeParser.ArrayvallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayvallist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.LSB)
            self.state = 206
            self.listarrayval()
            self.state = 207
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListarrayvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def listarrayval(self):
            return self.getTypedRuleContext(ZCodeParser.ListarrayvalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listarrayval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListarrayval" ):
                return visitor.visitListarrayval(self)
            else:
                return visitor.visitChildren(self)




    def listarrayval(self):

        localctx = ZCodeParser.ListarrayvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listarrayval)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.arrayval()
                self.state = 210
                self.match(ZCodeParser.COMMA)
                self.state = 211
                self.listarrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.arrayval()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizelist" ):
                return visitor.visitSizelist(self)
            else:
                return visitor.visitChildren(self)




    def sizelist(self):

        localctx = ZCodeParser.SizelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sizelist)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(ZCodeParser.NUMBER)
                self.state = 217
                self.match(ZCodeParser.COMMA)
                self.state = 218
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 227
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 228
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 229
                self.funccallstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 230
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmtlist)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN_KEY, ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.FOR_KEY, ZCodeParser.BREAK_KEY, ZCodeParser.CONTINUE_KEY, ZCodeParser.IF_KEY, ZCodeParser.BEGIN_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.statement()
                self.state = 234
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END_KEY]:
                self.enterOuterAlt(localctx, 2)

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


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KEY(self):
            return self.getToken(ZCodeParser.BEGIN_KEY, 0)

        def newlinelistnonull(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistnonullContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,i)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END_KEY(self):
            return self.getToken(ZCodeParser.END_KEY, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.BEGIN_KEY)
            self.state = 240
            self.newlinelistnonull()
            self.state = 241
            self.stmtlist()
            self.state = 242
            self.match(ZCodeParser.END_KEY)
            self.state = 243
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccallstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccallstmt" ):
                return visitor.visitFunccallstmt(self)
            else:
                return visitor.visitChildren(self)




    def funccallstmt(self):

        localctx = ZCodeParser.FunccallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funccallstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.ID)
            self.state = 246
            self.match(ZCodeParser.LB)
            self.state = 247
            self.argumentlist()
            self.state = 248
            self.match(ZCodeParser.RB)
            self.state = 249
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEY(self):
            return self.getToken(ZCodeParser.RETURN_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ZCodeParser.RETURN_KEY)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT_OPERATOR) | (1 << ZCodeParser.SUB_OPERATOR) | (1 << ZCodeParser.TRUE_BOOLEAN) | (1 << ZCodeParser.FALSE_BOOLEAN) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 252
                self.expr()


            self.state = 255
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_KEY(self):
            return self.getToken(ZCodeParser.CONTINUE_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.CONTINUE_KEY)
            self.state = 258
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KEY(self):
            return self.getToken(ZCodeParser.FOR_KEY, 0)

        def numbervariable(self):
            return self.getTypedRuleContext(ZCodeParser.NumbervariableContext,0)


        def UNTIL_KEY(self):
            return self.getToken(ZCodeParser.UNTIL_KEY, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY_KEY(self):
            return self.getToken(ZCodeParser.BY_KEY, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ZCodeParser.FOR_KEY)
            self.state = 261
            self.numbervariable()
            self.state = 262
            self.match(ZCodeParser.UNTIL_KEY)
            self.state = 263
            self.expr()
            self.state = 264
            self.match(ZCodeParser.BY_KEY)
            self.state = 265
            self.expr()
            self.state = 266
            self.newlinelist()
            self.state = 267
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_KEY(self):
            return self.getToken(ZCodeParser.BREAK_KEY, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.BREAK_KEY)
            self.state = 270
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEY(self):
            return self.getToken(ZCodeParser.IF_KEY, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def ELSE_KEY(self):
            return self.getToken(ZCodeParser.ELSE_KEY, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.IF_KEY)
            self.state = 273
            self.match(ZCodeParser.LB)
            self.state = 274
            self.expr()
            self.state = 275
            self.match(ZCodeParser.RB)
            self.state = 276
            self.newlinelist()
            self.state = 277
            self.statement()
            self.state = 278
            self.eliflist()
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 279
                self.match(ZCodeParser.ELSE_KEY)
                self.state = 280
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifcomponent(self):
            return self.getTypedRuleContext(ZCodeParser.ElifcomponentContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_eliflist)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.elifcomponent()
                self.state = 284
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifcomponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF_KEY(self):
            return self.getToken(ZCodeParser.ELIF_KEY, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifcomponent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifcomponent" ):
                return visitor.visitElifcomponent(self)
            else:
                return visitor.visitChildren(self)




    def elifcomponent(self):

        localctx = ZCodeParser.ElifcomponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elifcomponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.ELIF_KEY)
            self.state = 290
            self.expr()
            self.state = 291
            self.newlinelist()
            self.state = 292
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.lhs()
            self.state = 295
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 296
            self.expr()
            self.state = 297
            self.newlinelistnonull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationaloperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_OPERATOR(self):
            return self.getToken(ZCodeParser.EQUAL_OPERATOR, 0)

        def ASSIGN2_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN2_OPERATOR, 0)

        def NE_OPERATOR(self):
            return self.getToken(ZCodeParser.NE_OPERATOR, 0)

        def GE_OPERATOR(self):
            return self.getToken(ZCodeParser.GE_OPERATOR, 0)

        def G_OPERATOR(self):
            return self.getToken(ZCodeParser.G_OPERATOR, 0)

        def LE_OPERATOR(self):
            return self.getToken(ZCodeParser.LE_OPERATOR, 0)

        def L_OPERATOR(self):
            return self.getToken(ZCodeParser.L_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relationaloperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationaloperator" ):
                return visitor.visitRelationaloperator(self)
            else:
                return visitor.visitChildren(self)




    def relationaloperator(self):

        localctx = ZCodeParser.RelationaloperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_relationaloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OPERATOR) | (1 << ZCodeParser.GE_OPERATOR) | (1 << ZCodeParser.G_OPERATOR) | (1 << ZCodeParser.LE_OPERATOR) | (1 << ZCodeParser.L_OPERATOR) | (1 << ZCodeParser.NE_OPERATOR) | (1 << ZCodeParser.ASSIGN2_OPERATOR))) != 0)):
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


    class LogicoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OPERATOR(self):
            return self.getToken(ZCodeParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(ZCodeParser.OR_OPERATOR, 0)

        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicoperator" ):
                return visitor.visitLogicoperator(self)
            else:
                return visitor.visitChildren(self)




    def logicoperator(self):

        localctx = ZCodeParser.LogicoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_logicoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OR_OPERATOR) | (1 << ZCodeParser.AND_OPERATOR) | (1 << ZCodeParser.NOT_OPERATOR))) != 0)):
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


    class ArithmeticoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_OPERATOR(self):
            return self.getToken(ZCodeParser.ADD_OPERATOR, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def MODULO_OPERATOR(self):
            return self.getToken(ZCodeParser.MODULO_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(ZCodeParser.DIV_OPERATOR, 0)

        def MUL_OPERATOR(self):
            return self.getToken(ZCodeParser.MUL_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arithmeticoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticoperator" ):
                return visitor.visitArithmeticoperator(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticoperator(self):

        localctx = ZCodeParser.ArithmeticoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arithmeticoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MODULO_OPERATOR) | (1 << ZCodeParser.ADD_OPERATOR) | (1 << ZCodeParser.SUB_OPERATOR) | (1 << ZCodeParser.MUL_OPERATOR) | (1 << ZCodeParser.DIV_OPERATOR))) != 0)):
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_TYPE(self):
            return self.getToken(ZCodeParser.NUM_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(ZCodeParser.BOOL_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ZCodeParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_TYPE) | (1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.STRING_TYPE))) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT_OPERATOR(self):
            return self.getToken(ZCodeParser.CONCAT_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.expr1()
                self.state = 308
                self.match(ZCodeParser.CONCAT_OPERATOR)
                self.state = 309
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def relationaloperator(self):
            return self.getTypedRuleContext(ZCodeParser.RelationaloperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr1)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.expr2(0)
                self.state = 315
                self.relationaloperator()
                self.state = 316
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND_OPERATOR(self):
            return self.getToken(ZCodeParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(ZCodeParser.OR_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.OR_OPERATOR or _la==ZCodeParser.AND_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.expr3(0) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD_OPERATOR(self):
            return self.getToken(ZCodeParser.ADD_OPERATOR, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 336
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OPERATOR or _la==ZCodeParser.SUB_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 337
                    self.expr4(0) 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL_OPERATOR(self):
            return self.getToken(ZCodeParser.MUL_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(ZCodeParser.DIV_OPERATOR, 0)

        def MODULO_OPERATOR(self):
            return self.getToken(ZCodeParser.MODULO_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 347
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MODULO_OPERATOR) | (1 << ZCodeParser.MUL_OPERATOR) | (1 << ZCodeParser.DIV_OPERATOR))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348
                    self.expr5() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 355
                self.expr5()
                pass
            elif token in [ZCodeParser.SUB_OPERATOR, ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr6)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 360
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.expr7(0)
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.indexoperator() 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr8)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.funccallstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.arrayvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 378
                self.indexoperator()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 379
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ZCodeParser.LB)
            self.state = 383
            self.expr()
            self.state = 384
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def indexope(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexoperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexoperator" ):
                return visitor.visitIndexoperator(self)
            else:
                return visitor.visitChildren(self)




    def indexoperator(self):

        localctx = ZCodeParser.IndexoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indexoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 386
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 387
                self.funccallstmt()
                pass


            self.state = 390
            self.match(ZCodeParser.LSB)
            self.state = 391
            self.indexope()
            self.state = 392
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indexope(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexope

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexope" ):
                return visitor.visitIndexope(self)
            else:
                return visitor.visitChildren(self)




    def indexope(self):

        localctx = ZCodeParser.IndexopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_indexope)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.expr()
                self.state = 396
                self.match(ZCodeParser.COMMA)
                self.state = 397
                self.indexope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argumentlist)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR, ZCodeParser.SUB_OPERATOR, ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.argumentprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgumentprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argumentprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentprime" ):
                return visitor.visitArgumentprime(self)
            else:
                return visitor.visitChildren(self)




    def argumentprime(self):

        localctx = ZCodeParser.ArgumentprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_argumentprime)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.argument()
                self.state = 406
                self.match(ZCodeParser.COMMA)
                self.state = 407
                self.argumentprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def booleanvalue(self):
            return self.getTypedRuleContext(ZCodeParser.BooleanvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.match(ZCodeParser.ID)
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 417
                self.booleanvalue()
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


    class BooleanvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE_BOOLEAN(self):
            return self.getToken(ZCodeParser.TRUE_BOOLEAN, 0)

        def FALSE_BOOLEAN(self):
            return self.getToken(ZCodeParser.FALSE_BOOLEAN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_booleanvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanvalue" ):
                return visitor.visitBooleanvalue(self)
            else:
                return visitor.visitChildren(self)




    def booleanvalue(self):

        localctx = ZCodeParser.BooleanvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_booleanvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE_BOOLEAN or _la==ZCodeParser.FALSE_BOOLEAN):
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


    class NumbervariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numbervariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumbervariable" ):
                return visitor.visitNumbervariable(self)
            else:
                return visitor.visitChildren(self)




    def numbervariable(self):

        localctx = ZCodeParser.NumbervariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_numbervariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_newlinelist)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(ZCodeParser.NEW_LINE)
                self.state = 425
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistnonullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelistnonull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelistnonull" ):
                return visitor.visitNewlinelistnonull(self)
            else:
                return visitor.visitChildren(self)




    def newlinelistnonull(self):

        localctx = ZCodeParser.NewlinelistnonullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_newlinelistnonull)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ZCodeParser.NEW_LINE)
                self.state = 430
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(ZCodeParser.NEW_LINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexexpr(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexprContext,0)


        def indexoperator(self):
            return self.getTypedRuleContext(ZCodeParser.IndexoperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_lhs)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.indexexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.indexoperator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def indexexpr(self):
            return self.getTypedRuleContext(ZCodeParser.IndexexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexpr" ):
                return visitor.visitIndexexpr(self)
            else:
                return visitor.visitChildren(self)




    def indexexpr(self):

        localctx = ZCodeParser.IndexexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_indexexpr)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(ZCodeParser.ID)
                self.state = 440
                self.match(ZCodeParser.LSB)
                self.state = 441
                self.index()
                self.state = 442
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(ZCodeParser.ID)
                self.state = 445
                self.match(ZCodeParser.LSB)
                self.state = 446
                self.indexexpr()
                self.state = 447
                self.match(ZCodeParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = ZCodeParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.expr()
                self.state = 452
                self.match(ZCodeParser.COMMA)
                self.state = 453
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = ZCodeParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_paralist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(ZCodeParser.LB)
            self.state = 459
            self.parameterlist()
            self.state = 460
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParaprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = ZCodeParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_parameterlist)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.paraprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ParaprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(ZCodeParser.ParaContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paraprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParaprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paraprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaprime" ):
                return visitor.visitParaprime(self)
            else:
                return visitor.visitChildren(self)




    def paraprime(self):

        localctx = ZCodeParser.ParaprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_paraprime)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.para()
                self.state = 467
                self.match(ZCodeParser.COMMA)
                self.state = 468
                self.paraprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def arrayparameter(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayparameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ZCodeParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_para)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.typ()
                self.state = 474
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.typ()
                self.state = 477
                self.match(ZCodeParser.ID)
                self.state = 478
                self.match(ZCodeParser.LSB)
                self.state = 479
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 481
                self.arrayparameter()
                pass


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
        self._predicates[33] = self.expr2_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[35] = self.expr4_sempred
        self._predicates[38] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




