# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0193\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*")
        buf.write("\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\7-\u0122\n-\f-\16")
        buf.write("-\u0125\13-\3-\3-\3-\3.\3.\7.\u012c\n.\f.\16.\u012f\13")
        buf.write(".\3/\3/\3/\3/\7/\u0135\n/\f/\16/\u0138\13/\3/\3/\3\60")
        buf.write("\3\60\3\60\5\60\u013f\n\60\3\60\3\60\5\60\u0143\n\60\3")
        buf.write("\60\5\60\u0146\n\60\5\60\u0148\n\60\3\61\6\61\u014b\n")
        buf.write("\61\r\61\16\61\u014c\3\62\3\62\7\62\u0151\n\62\f\62\16")
        buf.write("\62\u0154\13\62\3\63\3\63\5\63\u0158\n\63\3\63\6\63\u015b")
        buf.write("\n\63\r\63\16\63\u015c\3\64\6\64\u0160\n\64\r\64\16\64")
        buf.write("\u0161\3\64\3\64\3\65\3\65\7\65\u0168\n\65\f\65\16\65")
        buf.write("\u016b\13\65\3\65\3\65\3\66\3\66\3\66\3\66\5\66\u0173")
        buf.write("\n\66\3\67\3\67\3\67\38\38\38\58\u017b\n8\39\39\79\u017f")
        buf.write("\n9\f9\169\u0182\139\39\39\79\u0186\n9\f9\169\u0189\13")
        buf.write("9\39\39\3:\3:\3:\3:\3;\3;\3;\2\2<\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\2c\2e\2g\62i\63k\2m\2o\2q\64s\65u\66\3\2\f\3\2$$\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\5\2\13\13\16\17\"\"\6\2\n\f\16\17$$^^\b\2^^ddh")
        buf.write("hppttvv\2\u019e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5~\3\2\2")
        buf.write("\2\7\u0086\3\2\2\2\t\u008d\3\2\2\2\13\u0090\3\2\2\2\r")
        buf.write("\u0094\3\2\2\2\17\u0097\3\2\2\2\21\u0099\3\2\2\2\23\u009c")
        buf.write("\3\2\2\2\25\u009e\3\2\2\2\27\u00a1\3\2\2\2\31\u00a4\3")
        buf.write("\2\2\2\33\u00a6\3\2\2\2\35\u00a9\3\2\2\2\37\u00ad\3\2")
        buf.write("\2\2!\u00b1\3\2\2\2#\u00b3\3\2\2\2%\u00b5\3\2\2\2\'\u00b7")
        buf.write("\3\2\2\2)\u00b9\3\2\2\2+\u00bb\3\2\2\2-\u00c0\3\2\2\2")
        buf.write("/\u00c6\3\2\2\2\61\u00c8\3\2\2\2\63\u00ca\3\2\2\2\65\u00cc")
        buf.write("\3\2\2\2\67\u00ce\3\2\2\29\u00d0\3\2\2\2;\u00d2\3\2\2")
        buf.write("\2=\u00d4\3\2\2\2?\u00db\3\2\2\2A\u00df\3\2\2\2C\u00e7")
        buf.write("\3\2\2\2E\u00ec\3\2\2\2G\u00f0\3\2\2\2I\u00f6\3\2\2\2")
        buf.write("K\u00f9\3\2\2\2M\u00ff\3\2\2\2O\u0108\3\2\2\2Q\u010b\3")
        buf.write("\2\2\2S\u0110\3\2\2\2U\u0115\3\2\2\2W\u011b\3\2\2\2Y\u011f")
        buf.write("\3\2\2\2[\u0129\3\2\2\2]\u0130\3\2\2\2_\u0147\3\2\2\2")
        buf.write("a\u014a\3\2\2\2c\u014e\3\2\2\2e\u0155\3\2\2\2g\u015f\3")
        buf.write("\2\2\2i\u0165\3\2\2\2k\u0172\3\2\2\2m\u0174\3\2\2\2o\u017a")
        buf.write("\3\2\2\2q\u017c\3\2\2\2s\u018c\3\2\2\2u\u0190\3\2\2\2")
        buf.write("wx\7p\2\2xy\7w\2\2yz\7o\2\2z{\7d\2\2{|\7g\2\2|}\7t\2\2")
        buf.write("}\4\3\2\2\2~\177\7d\2\2\177\u0080\7q\2\2\u0080\u0081\7")
        buf.write("q\2\2\u0081\u0082\7n\2\2\u0082\u0083\7g\2\2\u0083\u0084")
        buf.write("\7c\2\2\u0084\u0085\7p\2\2\u0085\6\3\2\2\2\u0086\u0087")
        buf.write("\7u\2\2\u0087\u0088\7v\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7k\2\2\u008a\u008b\7p\2\2\u008b\u008c\7i\2\2\u008c\b")
        buf.write("\3\2\2\2\u008d\u008e\7?\2\2\u008e\u008f\7?\2\2\u008f\n")
        buf.write("\3\2\2\2\u0090\u0091\7\60\2\2\u0091\u0092\7\60\2\2\u0092")
        buf.write("\u0093\7\60\2\2\u0093\f\3\2\2\2\u0094\u0095\7@\2\2\u0095")
        buf.write("\u0096\7?\2\2\u0096\16\3\2\2\2\u0097\u0098\7@\2\2\u0098")
        buf.write("\20\3\2\2\2\u0099\u009a\7>\2\2\u009a\u009b\7?\2\2\u009b")
        buf.write("\22\3\2\2\2\u009c\u009d\7>\2\2\u009d\24\3\2\2\2\u009e")
        buf.write("\u009f\7#\2\2\u009f\u00a0\7?\2\2\u00a0\26\3\2\2\2\u00a1")
        buf.write("\u00a2\7>\2\2\u00a2\u00a3\7/\2\2\u00a3\30\3\2\2\2\u00a4")
        buf.write("\u00a5\7?\2\2\u00a5\32\3\2\2\2\u00a6\u00a7\7q\2\2\u00a7")
        buf.write("\u00a8\7t\2\2\u00a8\34\3\2\2\2\u00a9\u00aa\7c\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7f\2\2\u00ac\36\3\2\2\2\u00ad")
        buf.write("\u00ae\7p\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write(" \3\2\2\2\u00b1\u00b2\7\'\2\2\u00b2\"\3\2\2\2\u00b3\u00b4")
        buf.write("\7-\2\2\u00b4$\3\2\2\2\u00b5\u00b6\7/\2\2\u00b6&\3\2\2")
        buf.write("\2\u00b7\u00b8\7,\2\2\u00b8(\3\2\2\2\u00b9\u00ba\7\61")
        buf.write("\2\2\u00ba*\3\2\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t")
        buf.write("\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7g\2\2\u00bf,\3\2")
        buf.write("\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7n\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7g\2\2\u00c5.\3")
        buf.write("\2\2\2\u00c6\u00c7\7*\2\2\u00c7\60\3\2\2\2\u00c8\u00c9")
        buf.write("\7+\2\2\u00c9\62\3\2\2\2\u00ca\u00cb\7]\2\2\u00cb\64\3")
        buf.write("\2\2\2\u00cc\u00cd\7_\2\2\u00cd\66\3\2\2\2\u00ce\u00cf")
        buf.write("\7}\2\2\u00cf8\3\2\2\2\u00d0\u00d1\7\177\2\2\u00d1:\3")
        buf.write("\2\2\2\u00d2\u00d3\7.\2\2\u00d3<\3\2\2\2\u00d4\u00d5\7")
        buf.write("t\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8")
        buf.write("\7w\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7p\2\2\u00da>\3")
        buf.write("\2\2\2\u00db\u00dc\7x\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de@\3\2\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1")
        buf.write("\7{\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7o\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7e\2\2\u00e6B\3")
        buf.write("\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7e\2\2\u00ebD\3\2\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7t\2\2\u00efF\3")
        buf.write("\2\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7n\2\2\u00f5H\3")
        buf.write("\2\2\2\u00f6\u00f7\7d\2\2\u00f7\u00f8\7{\2\2\u00f8J\3")
        buf.write("\2\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7m\2\2\u00feL\3")
        buf.write("\2\2\2\u00ff\u0100\7e\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7w\2\2\u0106\u0107\7g\2\2\u0107N\3")
        buf.write("\2\2\2\u0108\u0109\7k\2\2\u0109\u010a\7h\2\2\u010aP\3")
        buf.write("\2\2\2\u010b\u010c\7g\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7u\2\2\u010e\u010f\7g\2\2\u010fR\3\2\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111\u0112\7n\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7h\2\2\u0114T\3\2\2\2\u0115\u0116\7d\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\7i\2\2\u0118\u0119\7k\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011aV\3\2\2\2\u011b\u011c\7g\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7f\2\2\u011eX\3\2\2\2\u011f\u0123")
        buf.write("\t\2\2\2\u0120\u0122\5k\66\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127\t")
        buf.write("\2\2\2\u0127\u0128\b-\2\2\u0128Z\3\2\2\2\u0129\u012d\t")
        buf.write("\3\2\2\u012a\u012c\t\4\2\2\u012b\u012a\3\2\2\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\\\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7%\2\2\u0131")
        buf.write("\u0132\7%\2\2\u0132\u0136\3\2\2\2\u0133\u0135\n\5\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013a\b/\3\2\u013a^\3\2\2\2\u013b\u013c")
        buf.write("\5a\61\2\u013c\u013e\5c\62\2\u013d\u013f\5e\63\2\u013e")
        buf.write("\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0148\3\2\2\2")
        buf.write("\u0140\u0142\5a\61\2\u0141\u0143\5c\62\2\u0142\u0141\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0146")
        buf.write("\5e\63\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u013b\3\2\2\2\u0147\u0140\3\2\2\2")
        buf.write("\u0148`\3\2\2\2\u0149\u014b\t\6\2\2\u014a\u0149\3\2\2")
        buf.write("\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014db\3\2\2\2\u014e\u0152\7\60\2\2\u014f\u0151")
        buf.write("\t\6\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153d\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155\u0157\t\7\2\2\u0156\u0158\t\b\2\2")
        buf.write("\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\3")
        buf.write("\2\2\2\u0159\u015b\t\6\2\2\u015a\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("f\3\2\2\2\u015e\u0160\t\t\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0164\b\64\3\2\u0164h\3\2\2")
        buf.write("\2\u0165\u0169\7$\2\2\u0166\u0168\5k\66\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016c\u016d\b\65\4\2\u016dj\3\2\2\2\u016e\u0173\n\n\2")
        buf.write("\2\u016f\u0173\5m\67\2\u0170\u0171\7)\2\2\u0171\u0173")
        buf.write("\7$\2\2\u0172\u016e\3\2\2\2\u0172\u016f\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173l\3\2\2\2\u0174\u0175\7^\2\2\u0175")
        buf.write("\u0176\t\13\2\2\u0176n\3\2\2\2\u0177\u0178\7^\2\2\u0178")
        buf.write("\u017b\n\13\2\2\u0179\u017b\7^\2\2\u017a\u0177\3\2\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017bp\3\2\2\2\u017c\u0180\7$\2\2")
        buf.write("\u017d\u017f\5k\66\2\u017e\u017d\3\2\2\2\u017f\u0182\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0187\5o8\2\u0184\u0186")
        buf.write("\7$\2\2\u0185\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u018a\u018b\b9\5\2\u018br\3\2\2\2")
        buf.write("\u018c\u018d\7\f\2\2\u018d\u018e\3\2\2\2\u018e\u018f\b")
        buf.write(":\3\2\u018ft\3\2\2\2\u0190\u0191\13\2\2\2\u0191\u0192")
        buf.write("\b;\6\2\u0192v\3\2\2\2\24\2\u0123\u012d\u0136\u013e\u0142")
        buf.write("\u0145\u0147\u014c\u0152\u0157\u015c\u0161\u0169\u0172")
        buf.write("\u017a\u0180\u0187\7\3-\2\b\2\2\3\65\3\39\4\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM_TYPE = 1
    BOOL_TYPE = 2
    STRING_TYPE = 3
    EQUAL_OPERATOR = 4
    CONCAT_OPERATOR = 5
    GE_OPERATOR = 6
    G_OPERATOR = 7
    LE_OPERATOR = 8
    L_OPERATOR = 9
    NE_OPERATOR = 10
    ASSIGN1_OPERATOR = 11
    ASSIGN2_OPERATOR = 12
    OR_OPERATOR = 13
    AND_OPERATOR = 14
    NOT_OPERATOR = 15
    MODULO_OPERATOR = 16
    ADD_OPERATOR = 17
    SUB_OPERATOR = 18
    MUL_OPERATOR = 19
    DIV_OPERATOR = 20
    TRUE_BOOLEAN = 21
    FALSE_BOOLEAN = 22
    LB = 23
    RB = 24
    LSB = 25
    RSB = 26
    LPT = 27
    RPT = 28
    COMMA = 29
    RETURN_KEY = 30
    VAR_KEY = 31
    DYNAMIC_KEY = 32
    FUNC_KEY = 33
    FOR_KEY = 34
    UNTIL_KEY = 35
    BY_KEY = 36
    BREAK_KEY = 37
    CONTINUE_KEY = 38
    IF_KEY = 39
    ELSE_KEY = 40
    ELIF_KEY = 41
    BEGIN_KEY = 42
    END_KEY = 43
    STRING = 44
    IDENTIFIERS = 45
    COMMENT = 46
    NUMBER = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    NEWLINE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'boolean'", "'string'", "'=='", "'...'", "'>='", 
            "'>'", "'<='", "'<'", "'!='", "'<-'", "'='", "'or'", "'and'", 
            "'not'", "'%'", "'+'", "'-'", "'*'", "'/'", "'true'", "'false'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", "CONCAT_OPERATOR", 
            "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", "NE_OPERATOR", 
            "ASSIGN1_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", "AND_OPERATOR", 
            "NOT_OPERATOR", "MODULO_OPERATOR", "ADD_OPERATOR", "SUB_OPERATOR", 
            "MUL_OPERATOR", "DIV_OPERATOR", "TRUE_BOOLEAN", "FALSE_BOOLEAN", 
            "LB", "RB", "LSB", "RSB", "LPT", "RPT", "COMMA", "RETURN_KEY", 
            "VAR_KEY", "DYNAMIC_KEY", "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", 
            "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", 
            "ELIF_KEY", "BEGIN_KEY", "END_KEY", "STRING", "IDENTIFIERS", 
            "COMMENT", "NUMBER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "NEWLINE", "ERROR_CHAR" ]

    ruleNames = [ "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", 
                  "CONCAT_OPERATOR", "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", 
                  "L_OPERATOR", "NE_OPERATOR", "ASSIGN1_OPERATOR", "ASSIGN2_OPERATOR", 
                  "OR_OPERATOR", "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", 
                  "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                  "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", "RB", "LSB", "RSB", 
                  "LPT", "RPT", "COMMA", "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", 
                  "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", "BY_KEY", "BREAK_KEY", 
                  "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", "ELIF_KEY", "BEGIN_KEY", 
                  "END_KEY", "STRING", "IDENTIFIERS", "COMMENT", "NUMBER", 
                  "INTPART", "DECPART", "EXPPART", "WS", "UNCLOSE_STRING", 
                  "CHAR_OF_STRING", "ESCAPE", "ILL_ESCAPE", "ILLEGAL_ESCAPE", 
                  "NEWLINE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[43] = self.STRING_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1].replace('\'"','"')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


