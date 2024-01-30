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
        buf.write("\u01ca\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\4\3\4\5\4|\n\4\3\5\3\5\3\5\5\5\u0081")
        buf.write("\n\5\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u0098")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a2\n\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00a9\n\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00b2\n\n\3\n\3\n\3\13\3\13\5\13\u00b8\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\5\17\u00cd\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00d8")
        buf.write("\n\20\3\21\3\21\3\21\3\21\5\21\u00de\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\5\24\u00ee\n\24\3\24\3\24\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u010a")
        buf.write("\n\30\3\31\3\31\3\31\3\31\5\31\u0110\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u0129\n \3")
        buf.write("!\3!\3!\3!\3!\5!\u0130\n!\3\"\3\"\3\"\3\"\3\"\3\"\7\"")
        buf.write("\u0138\n\"\f\"\16\"\u013b\13\"\3#\3#\3#\3#\3#\3#\7#\u0143")
        buf.write("\n#\f#\16#\u0146\13#\3$\3$\3$\3$\3$\3$\7$\u014e\n$\f$")
        buf.write("\16$\u0151\13$\3%\3%\3%\3%\3%\5%\u0158\n%\3&\3&\3&\5&")
        buf.write("\u015d\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0166\n\'\f")
        buf.write("\'\16\'\u0169\13\'\3(\3(\5(\u016d\n(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\5)\u0178\n)\3*\3*\3*\3*\5*\u017e\n*\3+\3+\5")
        buf.write("+\u0182\n+\3,\3,\3,\3,\3,\5,\u0189\n,\3-\3-\3.\3.\3.\3")
        buf.write(".\5.\u0191\n.\3/\3/\3\60\3\60\3\61\3\61\3\61\5\61\u019a")
        buf.write("\n\61\3\62\3\62\3\62\5\62\u019f\n\62\3\63\3\63\5\63\u01a3")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01af\n\64\3\65\3\65\3\65\3\65\3\66\3\66\5\66\u01b7")
        buf.write("\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u01be\n\67\38\38\3")
        buf.write("8\38\38\38\38\38\58\u01c8\n8\38\2\6BDFL9\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjln\2\n\4\2\24\24\27\34\3\2\35\37\3")
        buf.write("\2 $\3\2\21\23\3\2\35\36\3\2!\"\4\2  #$\3\2%&\2\u01c4")
        buf.write("\2p\3\2\2\2\4w\3\2\2\2\6{\3\2\2\2\b\u0080\3\2\2\2\n\u008b")
        buf.write("\3\2\2\2\f\u008d\3\2\2\2\16\u0093\3\2\2\2\20\u00a8\3\2")
        buf.write("\2\2\22\u00aa\3\2\2\2\24\u00b7\3\2\2\2\26\u00b9\3\2\2")
        buf.write("\2\30\u00bd\3\2\2\2\32\u00c6\3\2\2\2\34\u00cc\3\2\2\2")
        buf.write("\36\u00d7\3\2\2\2 \u00dd\3\2\2\2\"\u00df\3\2\2\2$\u00e5")
        buf.write("\3\2\2\2&\u00eb\3\2\2\2(\u00f1\3\2\2\2*\u00f4\3\2\2\2")
        buf.write(",\u00fd\3\2\2\2.\u0100\3\2\2\2\60\u010f\3\2\2\2\62\u0111")
        buf.write("\3\2\2\2\64\u0116\3\2\2\2\66\u011b\3\2\2\28\u011d\3\2")
        buf.write("\2\2:\u011f\3\2\2\2<\u0121\3\2\2\2>\u0128\3\2\2\2@\u012f")
        buf.write("\3\2\2\2B\u0131\3\2\2\2D\u013c\3\2\2\2F\u0147\3\2\2\2")
        buf.write("H\u0157\3\2\2\2J\u015c\3\2\2\2L\u015e\3\2\2\2N\u016c\3")
        buf.write("\2\2\2P\u0177\3\2\2\2R\u017d\3\2\2\2T\u0181\3\2\2\2V\u0188")
        buf.write("\3\2\2\2X\u018a\3\2\2\2Z\u0190\3\2\2\2\\\u0192\3\2\2\2")
        buf.write("^\u0194\3\2\2\2`\u0199\3\2\2\2b\u019e\3\2\2\2d\u01a2\3")
        buf.write("\2\2\2f\u01ae\3\2\2\2h\u01b0\3\2\2\2j\u01b6\3\2\2\2l\u01bd")
        buf.write("\3\2\2\2n\u01c7\3\2\2\2pq\5\4\3\2qr\7\2\2\3r\3\3\2\2\2")
        buf.write("st\5\6\4\2tu\5\4\3\2ux\3\2\2\2vx\5\6\4\2ws\3\2\2\2wv\3")
        buf.write("\2\2\2x\5\3\2\2\2y|\5\b\5\2z|\5\20\t\2{y\3\2\2\2{z\3\2")
        buf.write("\2\2|\7\3\2\2\2}\u0081\5\n\6\2~\u0081\5\f\7\2\177\u0081")
        buf.write("\5\16\b\2\u0080}\3\2\2\2\u0080~\3\2\2\2\u0080\177\3\2")
        buf.write("\2\2\u0081\t\3\2\2\2\u0082\u0083\5<\37\2\u0083\u0086\7")
        buf.write("/\2\2\u0084\u0085\7\26\2\2\u0085\u0087\5> \2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\5b\62\2\u0089\u008c\3\2\2\2\u008a\u008c\5\22\n")
        buf.write("\2\u008b\u0082\3\2\2\2\u008b\u008a\3\2\2\2\u008c\13\3")
        buf.write("\2\2\2\u008d\u008e\7\4\2\2\u008e\u008f\7/\2\2\u008f\u0090")
        buf.write("\7\26\2\2\u0090\u0091\5> \2\u0091\u0092\5b\62\2\u0092")
        buf.write("\r\3\2\2\2\u0093\u0094\7\5\2\2\u0094\u0097\7/\2\2\u0095")
        buf.write("\u0096\7\26\2\2\u0096\u0098\5> \2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\5")
        buf.write("b\62\2\u009a\17\3\2\2\2\u009b\u009c\7\6\2\2\u009c\u009d")
        buf.write("\7/\2\2\u009d\u009e\5h\65\2\u009e\u00a1\5`\61\2\u009f")
        buf.write("\u00a2\5&\24\2\u00a0\u00a2\5\"\22\2\u00a1\u009f\3\2\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a2\u00a9\3\2\2\2\u00a3\u00a4")
        buf.write("\7\6\2\2\u00a4\u00a5\7/\2\2\u00a5\u00a6\5h\65\2\u00a6")
        buf.write("\u00a7\5b\62\2\u00a7\u00a9\3\2\2\2\u00a8\u009b\3\2\2\2")
        buf.write("\u00a8\u00a3\3\2\2\2\u00a9\21\3\2\2\2\u00aa\u00ab\5<\37")
        buf.write("\2\u00ab\u00ac\7/\2\2\u00ac\u00ad\7)\2\2\u00ad\u00ae\5")
        buf.write("\34\17\2\u00ae\u00b1\7*\2\2\u00af\u00b0\7\26\2\2\u00b0")
        buf.write("\u00b2\5\24\13\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2")
        buf.write("\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\5b\62\2\u00b4\23\3")
        buf.write("\2\2\2\u00b5\u00b8\5\26\f\2\u00b6\u00b8\5\30\r\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\25\3\2\2\2\u00b9")
        buf.write("\u00ba\7)\2\2\u00ba\u00bb\5\34\17\2\u00bb\u00bc\7*\2\2")
        buf.write("\u00bc\27\3\2\2\2\u00bd\u00be\7)\2\2\u00be\u00bf\5\32")
        buf.write("\16\2\u00bf\u00c0\7*\2\2\u00c0\31\3\2\2\2\u00c1\u00c2")
        buf.write("\5\26\f\2\u00c2\u00c3\7-\2\2\u00c3\u00c4\5\32\16\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5\26\f\2\u00c6\u00c1\3\2\2")
        buf.write("\2\u00c6\u00c5\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c9\7")
        buf.write("\60\2\2\u00c9\u00ca\7-\2\2\u00ca\u00cd\5\34\17\2\u00cb")
        buf.write("\u00cd\7\60\2\2\u00cc\u00c8\3\2\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cd\35\3\2\2\2\u00ce\u00d8\5\b\5\2\u00cf\u00d8\5")
        buf.write("\64\33\2\u00d0\u00d8\5.\30\2\u00d1\u00d8\5*\26\2\u00d2")
        buf.write("\u00d8\5,\27\2\u00d3\u00d8\5(\25\2\u00d4\u00d8\5&\24\2")
        buf.write("\u00d5\u00d8\5$\23\2\u00d6\u00d8\5\"\22\2\u00d7\u00ce")
        buf.write("\3\2\2\2\u00d7\u00cf\3\2\2\2\u00d7\u00d0\3\2\2\2\u00d7")
        buf.write("\u00d1\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d3\3\2\2\2")
        buf.write("\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3")
        buf.write("\2\2\2\u00d8\37\3\2\2\2\u00d9\u00da\5\36\20\2\u00da\u00db")
        buf.write("\5 \21\2\u00db\u00de\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de!\3\2\2\2\u00df")
        buf.write("\u00e0\7\17\2\2\u00e0\u00e1\5b\62\2\u00e1\u00e2\5 \21")
        buf.write("\2\u00e2\u00e3\7\20\2\2\u00e3\u00e4\5b\62\2\u00e4#\3\2")
        buf.write("\2\2\u00e5\u00e6\7/\2\2\u00e6\u00e7\7\'\2\2\u00e7\u00e8")
        buf.write("\5T+\2\u00e8\u00e9\7(\2\2\u00e9\u00ea\5`\61\2\u00ea%\3")
        buf.write("\2\2\2\u00eb\u00ed\7\3\2\2\u00ec\u00ee\5> \2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f0\5b\62\2\u00f0\'\3\2\2\2\u00f1\u00f2\7\13\2\2\u00f2")
        buf.write("\u00f3\5b\62\2\u00f3)\3\2\2\2\u00f4\u00f5\7\7\2\2\u00f5")
        buf.write("\u00f6\5^\60\2\u00f6\u00f7\7\b\2\2\u00f7\u00f8\5> \2\u00f8")
        buf.write("\u00f9\7\t\2\2\u00f9\u00fa\5> \2\u00fa\u00fb\5`\61\2\u00fb")
        buf.write("\u00fc\5\36\20\2\u00fc+\3\2\2\2\u00fd\u00fe\7\n\2\2\u00fe")
        buf.write("\u00ff\5b\62\2\u00ff-\3\2\2\2\u0100\u0101\7\f\2\2\u0101")
        buf.write("\u0102\7\'\2\2\u0102\u0103\5> \2\u0103\u0104\7(\2\2\u0104")
        buf.write("\u0105\5`\61\2\u0105\u0106\5\36\20\2\u0106\u0109\5\60")
        buf.write("\31\2\u0107\u0108\7\r\2\2\u0108\u010a\5\36\20\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a/\3\2\2\2\u010b")
        buf.write("\u010c\5\62\32\2\u010c\u010d\5\60\31\2\u010d\u0110\3\2")
        buf.write("\2\2\u010e\u0110\3\2\2\2\u010f\u010b\3\2\2\2\u010f\u010e")
        buf.write("\3\2\2\2\u0110\61\3\2\2\2\u0111\u0112\7\16\2\2\u0112\u0113")
        buf.write("\5> \2\u0113\u0114\5`\61\2\u0114\u0115\5\36\20\2\u0115")
        buf.write("\63\3\2\2\2\u0116\u0117\5d\63\2\u0117\u0118\7\26\2\2\u0118")
        buf.write("\u0119\5> \2\u0119\u011a\5b\62\2\u011a\65\3\2\2\2\u011b")
        buf.write("\u011c\t\2\2\2\u011c\67\3\2\2\2\u011d\u011e\t\3\2\2\u011e")
        buf.write("9\3\2\2\2\u011f\u0120\t\4\2\2\u0120;\3\2\2\2\u0121\u0122")
        buf.write("\t\5\2\2\u0122=\3\2\2\2\u0123\u0124\5@!\2\u0124\u0125")
        buf.write("\7\25\2\2\u0125\u0126\5@!\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0129\5@!\2\u0128\u0123\3\2\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("?\3\2\2\2\u012a\u012b\5B\"\2\u012b\u012c\5\66\34\2\u012c")
        buf.write("\u012d\5B\"\2\u012d\u0130\3\2\2\2\u012e\u0130\5B\"\2\u012f")
        buf.write("\u012a\3\2\2\2\u012f\u012e\3\2\2\2\u0130A\3\2\2\2\u0131")
        buf.write("\u0132\b\"\1\2\u0132\u0133\5D#\2\u0133\u0139\3\2\2\2\u0134")
        buf.write("\u0135\f\4\2\2\u0135\u0136\t\6\2\2\u0136\u0138\5D#\2\u0137")
        buf.write("\u0134\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013aC\3\2\2\2\u013b\u0139\3\2\2")
        buf.write("\2\u013c\u013d\b#\1\2\u013d\u013e\5F$\2\u013e\u0144\3")
        buf.write("\2\2\2\u013f\u0140\f\4\2\2\u0140\u0141\t\7\2\2\u0141\u0143")
        buf.write("\5F$\2\u0142\u013f\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145E\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0147\u0148\b$\1\2\u0148\u0149\5H%\2\u0149\u014f")
        buf.write("\3\2\2\2\u014a\u014b\f\4\2\2\u014b\u014c\t\b\2\2\u014c")
        buf.write("\u014e\5H%\2\u014d\u014a\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150G\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152\u0153\5J&\2\u0153\u0154\7\37\2\2")
        buf.write("\u0154\u0155\5H%\2\u0155\u0158\3\2\2\2\u0156\u0158\5J")
        buf.write("&\2\u0157\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u0158I\3\2")
        buf.write("\2\2\u0159\u015a\7\"\2\2\u015a\u015d\5J&\2\u015b\u015d")
        buf.write("\5L\'\2\u015c\u0159\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("K\3\2\2\2\u015e\u015f\b\'\1\2\u015f\u0160\5R*\2\u0160")
        buf.write("\u0167\3\2\2\2\u0161\u0162\f\4\2\2\u0162\u0163\5N(\2\u0163")
        buf.write("\u0164\5R*\2\u0164\u0166\3\2\2\2\u0165\u0161\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168M\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016d\7/\2\2")
        buf.write("\u016b\u016d\5$\23\2\u016c\u016a\3\2\2\2\u016c\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7)\2\2\u016f\u0170")
        buf.write("\5P)\2\u0170\u0171\7*\2\2\u0171O\3\2\2\2\u0172\u0178\5")
        buf.write("> \2\u0173\u0174\5> \2\u0174\u0175\7-\2\2\u0175\u0176")
        buf.write("\5P)\2\u0176\u0178\3\2\2\2\u0177\u0172\3\2\2\2\u0177\u0173")
        buf.write("\3\2\2\2\u0178Q\3\2\2\2\u0179\u017e\7/\2\2\u017a\u017e")
        buf.write("\5$\23\2\u017b\u017e\5Z.\2\u017c\u017e\5\24\13\2\u017d")
        buf.write("\u0179\3\2\2\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017c\3\2\2\2\u017eS\3\2\2\2\u017f\u0182\5V,\2")
        buf.write("\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3")
        buf.write("\2\2\2\u0182U\3\2\2\2\u0183\u0184\5X-\2\u0184\u0185\7")
        buf.write("-\2\2\u0185\u0186\5V,\2\u0186\u0189\3\2\2\2\u0187\u0189")
        buf.write("\5X-\2\u0188\u0183\3\2\2\2\u0188\u0187\3\2\2\2\u0189W")
        buf.write("\3\2\2\2\u018a\u018b\5Z.\2\u018bY\3\2\2\2\u018c\u0191")
        buf.write("\7\61\2\2\u018d\u0191\7\60\2\2\u018e\u0191\7/\2\2\u018f")
        buf.write("\u0191\5\\/\2\u0190\u018c\3\2\2\2\u0190\u018d\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191[\3\2\2")
        buf.write("\2\u0192\u0193\t\t\2\2\u0193]\3\2\2\2\u0194\u0195\7/\2")
        buf.write("\2\u0195_\3\2\2\2\u0196\u0197\7\64\2\2\u0197\u019a\5`")
        buf.write("\61\2\u0198\u019a\3\2\2\2\u0199\u0196\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019aa\3\2\2\2\u019b\u019c\7\64\2\2\u019c\u019f")
        buf.write("\5b\62\2\u019d\u019f\7\64\2\2\u019e\u019b\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019fc\3\2\2\2\u01a0\u01a3\7/\2\2\u01a1")
        buf.write("\u01a3\5f\64\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3e\3\2\2\2\u01a4\u01a5\7/\2\2\u01a5\u01a6\7)\2\2")
        buf.write("\u01a6\u01a7\5\34\17\2\u01a7\u01a8\7*\2\2\u01a8\u01af")
        buf.write("\3\2\2\2\u01a9\u01aa\7/\2\2\u01aa\u01ab\7)\2\2\u01ab\u01ac")
        buf.write("\5f\64\2\u01ac\u01ad\7*\2\2\u01ad\u01af\3\2\2\2\u01ae")
        buf.write("\u01a4\3\2\2\2\u01ae\u01a9\3\2\2\2\u01afg\3\2\2\2\u01b0")
        buf.write("\u01b1\7\'\2\2\u01b1\u01b2\5j\66\2\u01b2\u01b3\7(\2\2")
        buf.write("\u01b3i\3\2\2\2\u01b4\u01b7\5l\67\2\u01b5\u01b7\3\2\2")
        buf.write("\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7k\3\2")
        buf.write("\2\2\u01b8\u01b9\5n8\2\u01b9\u01ba\7-\2\2\u01ba\u01bb")
        buf.write("\5l\67\2\u01bb\u01be\3\2\2\2\u01bc\u01be\5n8\2\u01bd\u01b8")
        buf.write("\3\2\2\2\u01bd\u01bc\3\2\2\2\u01bem\3\2\2\2\u01bf\u01c0")
        buf.write("\5<\37\2\u01c0\u01c1\7/\2\2\u01c1\u01c8\3\2\2\2\u01c2")
        buf.write("\u01c3\5<\37\2\u01c3\u01c4\7/\2\2\u01c4\u01c5\7)\2\2\u01c5")
        buf.write("\u01c6\7*\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01bf\3\2\2\2")
        buf.write("\u01c7\u01c2\3\2\2\2\u01c8o\3\2\2\2(w{\u0080\u0086\u008b")
        buf.write("\u0097\u00a1\u00a8\u00b1\u00b7\u00c6\u00cc\u00d7\u00dd")
        buf.write("\u00ed\u0109\u010f\u0128\u012f\u0139\u0144\u014f\u0157")
        buf.write("\u015c\u0167\u016c\u0177\u017d\u0181\u0188\u0190\u0199")
        buf.write("\u019e\u01a2\u01ae\u01b6\u01bd\u01c7")
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
                     "','" ]

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
    RULE_arrayvalue = 9
    RULE_arrayval = 10
    RULE_arrayvallist = 11
    RULE_listarrayval = 12
    RULE_sizelist = 13
    RULE_statement = 14
    RULE_stmtlist = 15
    RULE_blockstmt = 16
    RULE_funccallstmt = 17
    RULE_returnstmt = 18
    RULE_continuestmt = 19
    RULE_forstmt = 20
    RULE_breakstmt = 21
    RULE_ifstmt = 22
    RULE_eliflist = 23
    RULE_elifcomponent = 24
    RULE_assignstmt = 25
    RULE_relationaloperator = 26
    RULE_logicoperator = 27
    RULE_arithmeticoperator = 28
    RULE_typ = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_expr7 = 37
    RULE_indexoperator = 38
    RULE_indexope = 39
    RULE_expr8 = 40
    RULE_argumentlist = 41
    RULE_argumentprime = 42
    RULE_argument = 43
    RULE_literal = 44
    RULE_booleanvalue = 45
    RULE_numbervariable = 46
    RULE_newlinelist = 47
    RULE_newlinelistnonull = 48
    RULE_lhs = 49
    RULE_indexexpr = 50
    RULE_paralist = 51
    RULE_parameterlist = 52
    RULE_paraprime = 53
    RULE_para = 54

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "typdecl", 
                   "varkeydecl", "dynamicdecl", "funcdecl", "arraydecl", 
                   "arrayvalue", "arrayval", "arrayvallist", "listarrayval", 
                   "sizelist", "statement", "stmtlist", "blockstmt", "funccallstmt", 
                   "returnstmt", "continuestmt", "forstmt", "breakstmt", 
                   "ifstmt", "eliflist", "elifcomponent", "assignstmt", 
                   "relationaloperator", "logicoperator", "arithmeticoperator", 
                   "typ", "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "indexoperator", "indexope", "expr8", 
                   "argumentlist", "argumentprime", "argument", "literal", 
                   "booleanvalue", "numbervariable", "newlinelist", "newlinelistnonull", 
                   "lhs", "indexexpr", "paralist", "parameterlist", "paraprime", 
                   "para" ]

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
            self.state = 110
            self.decllist()
            self.state = 111
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.decl()
                self.state = 114
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.varkeydecl()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
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

        def newlinelistnonull(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistnonullContext,0)


        def ASSIGN1_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN1_OPERATOR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.typ()
                self.state = 129
                self.match(ZCodeParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN1_OPERATOR:
                    self.state = 130
                    self.match(ZCodeParser.ASSIGN1_OPERATOR)
                    self.state = 131
                    self.expr()


                self.state = 134
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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
            self.state = 139
            self.match(ZCodeParser.VAR_KEY)
            self.state = 140
            self.match(ZCodeParser.ID)
            self.state = 141
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 142
            self.expr()
            self.state = 143
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
            self.state = 145
            self.match(ZCodeParser.DYNAMIC_KEY)
            self.state = 146
            self.match(ZCodeParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 147
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 148
                self.expr()


            self.state = 151
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 154
                self.match(ZCodeParser.ID)
                self.state = 155
                self.paralist()
                self.state = 156
                self.newlinelist()
                self.state = 159
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN_KEY]:
                    self.state = 157
                    self.returnstmt()
                    pass
                elif token in [ZCodeParser.BEGIN_KEY]:
                    self.state = 158
                    self.blockstmt()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(ZCodeParser.FUNC_KEY)
                self.state = 162
                self.match(ZCodeParser.ID)
                self.state = 163
                self.paralist()
                self.state = 164
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
            self.state = 168
            self.typ()
            self.state = 169
            self.match(ZCodeParser.ID)
            self.state = 170
            self.match(ZCodeParser.LSB)
            self.state = 171
            self.sizelist()
            self.state = 172
            self.match(ZCodeParser.RSB)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN1_OPERATOR:
                self.state = 173
                self.match(ZCodeParser.ASSIGN1_OPERATOR)
                self.state = 174
                self.arrayvalue()


            self.state = 177
            self.newlinelistnonull()
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
        self.enterRule(localctx, 18, self.RULE_arrayvalue)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.arrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


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
        self.enterRule(localctx, 20, self.RULE_arrayval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ZCodeParser.LSB)
            self.state = 184
            self.sizelist()
            self.state = 185
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
        self.enterRule(localctx, 22, self.RULE_arrayvallist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.LSB)
            self.state = 188
            self.listarrayval()
            self.state = 189
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
        self.enterRule(localctx, 24, self.RULE_listarrayval)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.arrayval()
                self.state = 192
                self.match(ZCodeParser.COMMA)
                self.state = 193
                self.listarrayval()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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
        self.enterRule(localctx, 26, self.RULE_sizelist)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(ZCodeParser.NUMBER)
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 209
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 210
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 211
                self.funccallstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 212
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
        self.enterRule(localctx, 30, self.RULE_stmtlist)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN_KEY, ZCodeParser.VAR_KEY, ZCodeParser.DYNAMIC_KEY, ZCodeParser.FOR_KEY, ZCodeParser.BREAK_KEY, ZCodeParser.CONTINUE_KEY, ZCodeParser.IF_KEY, ZCodeParser.BEGIN_KEY, ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.statement()
                self.state = 216
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
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ZCodeParser.BEGIN_KEY)
            self.state = 222
            self.newlinelistnonull()
            self.state = 223
            self.stmtlist()
            self.state = 224
            self.match(ZCodeParser.END_KEY)
            self.state = 225
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
        self.enterRule(localctx, 34, self.RULE_funccallstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(ZCodeParser.ID)
            self.state = 228
            self.match(ZCodeParser.LB)
            self.state = 229
            self.argumentlist()
            self.state = 230
            self.match(ZCodeParser.RB)
            self.state = 231
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
        self.enterRule(localctx, 36, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZCodeParser.RETURN_KEY)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SUB_OPERATOR) | (1 << ZCodeParser.TRUE_BOOLEAN) | (1 << ZCodeParser.FALSE_BOOLEAN) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 234
                self.expr()


            self.state = 237
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
        self.enterRule(localctx, 38, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.CONTINUE_KEY)
            self.state = 240
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
        self.enterRule(localctx, 40, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ZCodeParser.FOR_KEY)
            self.state = 243
            self.numbervariable()
            self.state = 244
            self.match(ZCodeParser.UNTIL_KEY)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(ZCodeParser.BY_KEY)
            self.state = 247
            self.expr()
            self.state = 248
            self.newlinelist()
            self.state = 249
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
        self.enterRule(localctx, 42, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ZCodeParser.BREAK_KEY)
            self.state = 252
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
        self.enterRule(localctx, 44, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ZCodeParser.IF_KEY)
            self.state = 255
            self.match(ZCodeParser.LB)
            self.state = 256
            self.expr()
            self.state = 257
            self.match(ZCodeParser.RB)
            self.state = 258
            self.newlinelist()
            self.state = 259
            self.statement()
            self.state = 260
            self.eliflist()
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(ZCodeParser.ELSE_KEY)
                self.state = 262
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
        self.enterRule(localctx, 46, self.RULE_eliflist)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.elifcomponent()
                self.state = 266
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
        self.enterRule(localctx, 48, self.RULE_elifcomponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(ZCodeParser.ELIF_KEY)
            self.state = 272
            self.expr()
            self.state = 273
            self.newlinelist()
            self.state = 274
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
        self.enterRule(localctx, 50, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.lhs()
            self.state = 277
            self.match(ZCodeParser.ASSIGN1_OPERATOR)
            self.state = 278
            self.expr()
            self.state = 279
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
        self.enterRule(localctx, 52, self.RULE_relationaloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
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
        self.enterRule(localctx, 54, self.RULE_logicoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
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
        self.enterRule(localctx, 56, self.RULE_arithmeticoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
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
        self.enterRule(localctx, 58, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.expr1()
                self.state = 290
                self.match(ZCodeParser.CONCAT_OPERATOR)
                self.state = 291
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
        self.enterRule(localctx, 62, self.RULE_expr1)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.expr2(0)
                self.state = 297
                self.relationaloperator()
                self.state = 298
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.OR_OPERATOR or _la==ZCodeParser.AND_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    self.expr3(0) 
                self.state = 313
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OPERATOR or _la==ZCodeParser.SUB_OPERATOR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.expr4(0) 
                self.state = 324
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MODULO_OPERATOR) | (1 << ZCodeParser.MUL_OPERATOR) | (1 << ZCodeParser.DIV_OPERATOR))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 330
                    self.expr5() 
                self.state = 335
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

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr5)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.expr6()
                self.state = 337
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 338
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.expr6()
                pass


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
        self.enterRule(localctx, 72, self.RULE_expr6)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 344
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.LSB, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 351
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 352
                    self.indexoperator()
                    self.state = 353
                    self.expr8() 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 76, self.RULE_indexoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 360
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 361
                self.funccallstmt()
                pass


            self.state = 364
            self.match(ZCodeParser.LSB)
            self.state = 365
            self.indexope()
            self.state = 366
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
        self.enterRule(localctx, 78, self.RULE_indexope)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.expr()
                self.state = 370
                self.match(ZCodeParser.COMMA)
                self.state = 371
                self.indexope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr8)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.funccallstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.arrayvalue()
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
        self.enterRule(localctx, 82, self.RULE_argumentlist)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN, ZCodeParser.ID, ZCodeParser.NUMBER, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
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
        self.enterRule(localctx, 84, self.RULE_argumentprime)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.argument()
                self.state = 386
                self.match(ZCodeParser.COMMA)
                self.state = 387
                self.argumentprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.literal()
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
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.match(ZCodeParser.ID)
                pass
            elif token in [ZCodeParser.TRUE_BOOLEAN, ZCodeParser.FALSE_BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
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
        self.enterRule(localctx, 90, self.RULE_booleanvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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
        self.enterRule(localctx, 92, self.RULE_numbervariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        self.enterRule(localctx, 94, self.RULE_newlinelist)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(ZCodeParser.NEW_LINE)
                self.state = 405
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
        self.enterRule(localctx, 96, self.RULE_newlinelistnonull)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(ZCodeParser.NEW_LINE)
                self.state = 410
                self.newlinelistnonull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.indexexpr()
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

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


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
        self.enterRule(localctx, 100, self.RULE_indexexpr)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(ZCodeParser.ID)
                self.state = 419
                self.match(ZCodeParser.LSB)
                self.state = 420
                self.sizelist()
                self.state = 421
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(ZCodeParser.ID)
                self.state = 424
                self.match(ZCodeParser.LSB)
                self.state = 425
                self.indexexpr()
                self.state = 426
                self.match(ZCodeParser.RSB)
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
        self.enterRule(localctx, 102, self.RULE_paralist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(ZCodeParser.LB)
            self.state = 431
            self.parameterlist()
            self.state = 432
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
        self.enterRule(localctx, 104, self.RULE_parameterlist)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
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
        self.enterRule(localctx, 106, self.RULE_paraprime)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.para()
                self.state = 439
                self.match(ZCodeParser.COMMA)
                self.state = 440
                self.paraprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ZCodeParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_para)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.typ()
                self.state = 446
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.typ()
                self.state = 449
                self.match(ZCodeParser.ID)
                self.state = 450
                self.match(ZCodeParser.LSB)
                self.state = 451
                self.match(ZCodeParser.RSB)
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
        self._predicates[32] = self.expr2_sempred
        self._predicates[33] = self.expr3_sempred
        self._predicates[34] = self.expr4_sempred
        self._predicates[37] = self.expr7_sempred
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
         




