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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u0194\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3-\3-\7-\u0124\n-\f-\16-\u0127")
        buf.write("\13-\3-\3-\3.\3.\7.\u012d\n.\f.\16.\u0130\13.\3/\3/\3")
        buf.write("/\5/\u0135\n/\3/\3/\5/\u0139\n/\3/\5/\u013c\n/\5/\u013e")
        buf.write("\n/\3\60\6\60\u0141\n\60\r\60\16\60\u0142\3\61\3\61\7")
        buf.write("\61\u0147\n\61\f\61\16\61\u014a\13\61\3\62\3\62\5\62\u014e")
        buf.write("\n\62\3\62\6\62\u0151\n\62\r\62\16\62\u0152\3\63\6\63")
        buf.write("\u0156\n\63\r\63\16\63\u0157\3\64\3\64\3\64\3\64\3\64")
        buf.write("\7\64\u015f\n\64\f\64\16\64\u0162\13\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\7\65\u016c\n\65\f\65\16\65\u016f")
        buf.write("\13\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u017b\n\67\f\67\16\67\u017e\13\67\3\67\3\67\3")
        buf.write("\67\38\38\38\39\69\u0187\n9\r9\169\u0188\39\39\3:\6:\u018e")
        buf.write("\n:\r:\16:\u018f\3;\3;\3;\2\2<\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a")
        buf.write("\2c\2e\61g\62i\63k\2m\64o\2q\65s\66u\67\3\2\r\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\5\2\f\f$$^^\3\2))\3\2$$\b\2))^^ddhhttvv\5\2\13\13")
        buf.write("\16\17\"\"\2\u01a4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2m\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2")
        buf.write("\2\5~\3\2\2\2\7\u0082\3\2\2\2\t\u008a\3\2\2\2\13\u008f")
        buf.write("\3\2\2\2\r\u0093\3\2\2\2\17\u0099\3\2\2\2\21\u009c\3\2")
        buf.write("\2\2\23\u00a2\3\2\2\2\25\u00ab\3\2\2\2\27\u00ae\3\2\2")
        buf.write("\2\31\u00b3\3\2\2\2\33\u00b8\3\2\2\2\35\u00be\3\2\2\2")
        buf.write("\37\u00c2\3\2\2\2!\u00c9\3\2\2\2#\u00d1\3\2\2\2%\u00d8")
        buf.write("\3\2\2\2\'\u00db\3\2\2\2)\u00df\3\2\2\2+\u00e2\3\2\2\2")
        buf.write("-\u00e5\3\2\2\2/\u00e7\3\2\2\2\61\u00ea\3\2\2\2\63\u00ec")
        buf.write("\3\2\2\2\65\u00ef\3\2\2\2\67\u00f1\3\2\2\29\u00f4\3\2")
        buf.write("\2\2;\u00f8\3\2\2\2=\u00fc\3\2\2\2?\u00fe\3\2\2\2A\u0100")
        buf.write("\3\2\2\2C\u0102\3\2\2\2E\u0104\3\2\2\2G\u0106\3\2\2\2")
        buf.write("I\u010b\3\2\2\2K\u0111\3\2\2\2M\u0113\3\2\2\2O\u0115\3")
        buf.write("\2\2\2Q\u0117\3\2\2\2S\u0119\3\2\2\2U\u011b\3\2\2\2W\u011d")
        buf.write("\3\2\2\2Y\u011f\3\2\2\2[\u012a\3\2\2\2]\u013d\3\2\2\2")
        buf.write("_\u0140\3\2\2\2a\u0144\3\2\2\2c\u014b\3\2\2\2e\u0155\3")
        buf.write("\2\2\2g\u0159\3\2\2\2i\u0166\3\2\2\2k\u0172\3\2\2\2m\u0175")
        buf.write("\3\2\2\2o\u0182\3\2\2\2q\u0186\3\2\2\2s\u018d\3\2\2\2")
        buf.write("u\u0191\3\2\2\2wx\7t\2\2xy\7g\2\2yz\7v\2\2z{\7w\2\2{|")
        buf.write("\7t\2\2|}\7p\2\2}\4\3\2\2\2~\177\7x\2\2\177\u0080\7c\2")
        buf.write("\2\u0080\u0081\7t\2\2\u0081\6\3\2\2\2\u0082\u0083\7f\2")
        buf.write("\2\u0083\u0084\7{\2\2\u0084\u0085\7p\2\2\u0085\u0086\7")
        buf.write("c\2\2\u0086\u0087\7o\2\2\u0087\u0088\7k\2\2\u0088\u0089")
        buf.write("\7e\2\2\u0089\b\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c")
        buf.write("\7w\2\2\u008c\u008d\7p\2\2\u008d\u008e\7e\2\2\u008e\n")
        buf.write("\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091\7q\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\f\3\2\2\2\u0093\u0094\7w\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\u0096\7v\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7n\2\2\u0098\16\3\2\2\2\u0099\u009a\7d\2\2\u009a\u009b")
        buf.write("\7{\2\2\u009b\20\3\2\2\2\u009c\u009d\7d\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7m\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7e\2\2\u00a3\u00a4")
        buf.write("\7q\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\24\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7h\2\2\u00ad\26\3\2\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7g\2\2\u00b2\30")
        buf.write("\3\2\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7h\2\2\u00b7\32\3\2\2\2\u00b8\u00b9")
        buf.write("\7d\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7i\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7f\2\2\u00c1\36")
        buf.write("\3\2\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5")
        buf.write("\7o\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7d\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7p\2\2\u00d0\"")
        buf.write("\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7")
        buf.write("\7i\2\2\u00d7$\3\2\2\2\u00d8\u00d9\7?\2\2\u00d9\u00da")
        buf.write("\7?\2\2\u00da&\3\2\2\2\u00db\u00dc\7\60\2\2\u00dc\u00dd")
        buf.write("\7\60\2\2\u00dd\u00de\7\60\2\2\u00de(\3\2\2\2\u00df\u00e0")
        buf.write("\7>\2\2\u00e0\u00e1\7/\2\2\u00e1*\3\2\2\2\u00e2\u00e3")
        buf.write("\7@\2\2\u00e3\u00e4\7?\2\2\u00e4,\3\2\2\2\u00e5\u00e6")
        buf.write("\7@\2\2\u00e6.\3\2\2\2\u00e7\u00e8\7>\2\2\u00e8\u00e9")
        buf.write("\7?\2\2\u00e9\60\3\2\2\2\u00ea\u00eb\7>\2\2\u00eb\62\3")
        buf.write("\2\2\2\u00ec\u00ed\7#\2\2\u00ed\u00ee\7?\2\2\u00ee\64")
        buf.write("\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0\66\3\2\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7t\2\2\u00f38\3\2\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7f\2\2\u00f7:\3")
        buf.write("\2\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb<\3\2\2\2\u00fc\u00fd\7\'\2\2\u00fd>\3\2")
        buf.write("\2\2\u00fe\u00ff\7-\2\2\u00ff@\3\2\2\2\u0100\u0101\7/")
        buf.write("\2\2\u0101B\3\2\2\2\u0102\u0103\7,\2\2\u0103D\3\2\2\2")
        buf.write("\u0104\u0105\7\61\2\2\u0105F\3\2\2\2\u0106\u0107\7v\2")
        buf.write("\2\u0107\u0108\7t\2\2\u0108\u0109\7w\2\2\u0109\u010a\7")
        buf.write("g\2\2\u010aH\3\2\2\2\u010b\u010c\7h\2\2\u010c\u010d\7")
        buf.write("c\2\2\u010d\u010e\7n\2\2\u010e\u010f\7u\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110J\3\2\2\2\u0111\u0112\7*\2\2\u0112L\3\2\2")
        buf.write("\2\u0113\u0114\7+\2\2\u0114N\3\2\2\2\u0115\u0116\7]\2")
        buf.write("\2\u0116P\3\2\2\2\u0117\u0118\7_\2\2\u0118R\3\2\2\2\u0119")
        buf.write("\u011a\7}\2\2\u011aT\3\2\2\2\u011b\u011c\7\177\2\2\u011c")
        buf.write("V\3\2\2\2\u011d\u011e\7.\2\2\u011eX\3\2\2\2\u011f\u0120")
        buf.write("\7%\2\2\u0120\u0121\7%\2\2\u0121\u0125\3\2\2\2\u0122\u0124")
        buf.write("\n\2\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0125\3\2\2\2\u0128\u0129\b-\2\2\u0129Z\3\2\2\2")
        buf.write("\u012a\u012e\t\3\2\2\u012b\u012d\t\4\2\2\u012c\u012b\3")
        buf.write("\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\\\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132")
        buf.write("\5_\60\2\u0132\u0134\5a\61\2\u0133\u0135\5c\62\2\u0134")
        buf.write("\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u013e\3\2\2\2")
        buf.write("\u0136\u0138\5_\60\2\u0137\u0139\5a\61\2\u0138\u0137\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u013c")
        buf.write("\5c\62\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\3\2\2\2\u013d\u0131\3\2\2\2\u013d\u0136\3\2\2\2")
        buf.write("\u013e^\3\2\2\2\u013f\u0141\t\5\2\2\u0140\u013f\3\2\2")
        buf.write("\2\u0141\u0142\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143`\3\2\2\2\u0144\u0148\7\60\2\2\u0145\u0147")
        buf.write("\t\5\2\2\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149b\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014d\t\6\2\2\u014c\u014e\t\7\2\2")
        buf.write("\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3")
        buf.write("\2\2\2\u014f\u0151\t\5\2\2\u0150\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("d\3\2\2\2\u0154\u0156\t\5\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158f\3\2\2\2\u0159\u0160\7$\2\2\u015a\u015f\n\b\2\2")
        buf.write("\u015b\u015f\5k\66\2\u015c\u015d\t\t\2\2\u015d\u015f\t")
        buf.write("\n\2\2\u015e\u015a\3\2\2\2\u015e\u015b\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0164\7$\2\2\u0164\u0165\b\64\3\2\u0165h\3\2\2")
        buf.write("\2\u0166\u016d\7$\2\2\u0167\u016c\n\b\2\2\u0168\u016c")
        buf.write("\5k\66\2\u0169\u016a\t\t\2\2\u016a\u016c\t\n\2\2\u016b")
        buf.write("\u0167\3\2\2\2\u016b\u0168\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171")
        buf.write("\b\65\4\2\u0171j\3\2\2\2\u0172\u0173\7^\2\2\u0173\u0174")
        buf.write("\t\13\2\2\u0174l\3\2\2\2\u0175\u017c\7$\2\2\u0176\u017b")
        buf.write("\n\b\2\2\u0177\u017b\5k\66\2\u0178\u0179\t\t\2\2\u0179")
        buf.write("\u017b\t\n\2\2\u017a\u0176\3\2\2\2\u017a\u0177\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017f\u0180\5o8\2\u0180\u0181\b\67\5\2\u0181")
        buf.write("n\3\2\2\2\u0182\u0183\7^\2\2\u0183\u0184\n\13\2\2\u0184")
        buf.write("p\3\2\2\2\u0185\u0187\t\f\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018b\b9\2\2\u018br\3\2\2\2")
        buf.write("\u018c\u018e\7\f\2\2\u018d\u018c\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190t")
        buf.write("\3\2\2\2\u0191\u0192\13\2\2\2\u0192\u0193\b;\6\2\u0193")
        buf.write("v\3\2\2\2\26\2\u0125\u012e\u0134\u0138\u013b\u013d\u0142")
        buf.write("\u0148\u014d\u0152\u0157\u015e\u0160\u016b\u016d\u017a")
        buf.write("\u017c\u0188\u018f\7\b\2\2\3\64\2\3\65\3\3\67\4\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN_KEY = 1
    VAR_KEY = 2
    DYNAMIC_KEY = 3
    FUNC_KEY = 4
    FOR_KEY = 5
    UNTIL_KEY = 6
    BY_KEY = 7
    BREAK_KEY = 8
    CONTINUE_KEY = 9
    IF_KEY = 10
    ELSE_KEY = 11
    ELIF_KEY = 12
    BEGIN_KEY = 13
    END_KEY = 14
    NUM_TYPE = 15
    BOOL_TYPE = 16
    STRING_TYPE = 17
    EQUAL_OPERATOR = 18
    CONCAT_OPERATOR = 19
    ASSIGN1_OPERATOR = 20
    GE_OPERATOR = 21
    G_OPERATOR = 22
    LE_OPERATOR = 23
    L_OPERATOR = 24
    NE_OPERATOR = 25
    ASSIGN2_OPERATOR = 26
    OR_OPERATOR = 27
    AND_OPERATOR = 28
    NOT_OPERATOR = 29
    MODULO_OPERATOR = 30
    ADD_OPERATOR = 31
    SUB_OPERATOR = 32
    MUL_OPERATOR = 33
    DIV_OPERATOR = 34
    TRUE_BOOLEAN = 35
    FALSE_BOOLEAN = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    LPT = 41
    RPT = 42
    COMMA = 43
    COMMENT = 44
    ID = 45
    NUMBER = 46
    INTLIT = 47
    STRINGLIT = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    WS = 51
    NEW_LINE = 52
    ERROR_CHAR = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'number'", "'boolean'", "'string'", "'=='", 
            "'...'", "'<-'", "'>='", "'>'", "'<='", "'<'", "'!='", "'='", 
            "'or'", "'and'", "'not'", "'%'", "'+'", "'-'", "'*'", "'/'", 
            "'true'", "'false'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", "FUNC_KEY", "FOR_KEY", 
            "UNTIL_KEY", "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", "IF_KEY", 
            "ELSE_KEY", "ELIF_KEY", "BEGIN_KEY", "END_KEY", "NUM_TYPE", 
            "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", "CONCAT_OPERATOR", 
            "ASSIGN1_OPERATOR", "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", 
            "L_OPERATOR", "NE_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
            "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", "ADD_OPERATOR", 
            "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "TRUE_BOOLEAN", 
            "FALSE_BOOLEAN", "LB", "RB", "LSB", "RSB", "LPT", "RPT", "COMMA", 
            "COMMENT", "ID", "NUMBER", "INTLIT", "STRINGLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "NEW_LINE", "ERROR_CHAR" ]

    ruleNames = [ "RETURN_KEY", "VAR_KEY", "DYNAMIC_KEY", "FUNC_KEY", "FOR_KEY", 
                  "UNTIL_KEY", "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", "IF_KEY", 
                  "ELSE_KEY", "ELIF_KEY", "BEGIN_KEY", "END_KEY", "NUM_TYPE", 
                  "BOOL_TYPE", "STRING_TYPE", "EQUAL_OPERATOR", "CONCAT_OPERATOR", 
                  "ASSIGN1_OPERATOR", "GE_OPERATOR", "G_OPERATOR", "LE_OPERATOR", 
                  "L_OPERATOR", "NE_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
                  "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", "ADD_OPERATOR", 
                  "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "TRUE_BOOLEAN", 
                  "FALSE_BOOLEAN", "LB", "RB", "LSB", "RSB", "LPT", "RPT", 
                  "COMMA", "COMMENT", "ID", "NUMBER", "INTPART", "DECPART", 
                  "EXPPART", "INTLIT", "STRINGLIT", "UNCLOSE_STRING", "LI_ESCAPE", 
                  "ILLEGAL_ESCAPE", "ILL_ESCAPE", "WS", "NEW_LINE", "ERROR_CHAR" ]

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
            actions[50] = self.STRINGLIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
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
     


