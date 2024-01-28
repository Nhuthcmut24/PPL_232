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
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*")
        buf.write("\3+\3+\3,\3,\3-\3-\3-\3-\7-\u0122\n-\f-\16-\u0125\13-")
        buf.write("\3-\3-\3.\3.\7.\u012b\n.\f.\16.\u012e\13.\3/\3/\3/\5/")
        buf.write("\u0133\n/\3/\3/\5/\u0137\n/\3/\5/\u013a\n/\5/\u013c\n")
        buf.write("/\3\60\6\60\u013f\n\60\r\60\16\60\u0140\3\61\3\61\7\61")
        buf.write("\u0145\n\61\f\61\16\61\u0148\13\61\3\62\3\62\5\62\u014c")
        buf.write("\n\62\3\62\6\62\u014f\n\62\r\62\16\62\u0150\3\63\3\63")
        buf.write("\3\63\3\63\3\63\7\63\u0158\n\63\f\63\16\63\u015b\13\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\7\64\u0165\n")
        buf.write("\64\f\64\16\64\u0168\13\64\3\64\3\64\3\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\7\66\u0174\n\66\f\66\16\66\u0177")
        buf.write("\13\66\3\66\3\66\3\66\3\67\3\67\3\67\38\68\u0180\n8\r")
        buf.write("8\168\u0181\38\38\39\69\u0187\n9\r9\169\u0188\39\39\3")
        buf.write(":\3:\3:\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\2c\2e\61g\62i\2k\63")
        buf.write("m\2o\64q\65s\66\3\2\r\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\3\2))\3\2")
        buf.write("$$\b\2))^^ddhhttvv\5\2\13\13\16\17\"\"\2\u019e\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2k\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\3u\3\2\2\2\5|\3\2\2\2\7\u0080\3\2\2\2\t\u0088")
        buf.write("\3\2\2\2\13\u008d\3\2\2\2\r\u0091\3\2\2\2\17\u0097\3\2")
        buf.write("\2\2\21\u009a\3\2\2\2\23\u00a0\3\2\2\2\25\u00a9\3\2\2")
        buf.write("\2\27\u00ac\3\2\2\2\31\u00b1\3\2\2\2\33\u00b6\3\2\2\2")
        buf.write("\35\u00bc\3\2\2\2\37\u00c0\3\2\2\2!\u00c7\3\2\2\2#\u00cf")
        buf.write("\3\2\2\2%\u00d6\3\2\2\2\'\u00d9\3\2\2\2)\u00dd\3\2\2\2")
        buf.write("+\u00e0\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3\2\2\2\61\u00e8")
        buf.write("\3\2\2\2\63\u00ea\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3")
        buf.write("\2\2\29\u00f2\3\2\2\2;\u00f6\3\2\2\2=\u00fa\3\2\2\2?\u00fc")
        buf.write("\3\2\2\2A\u00fe\3\2\2\2C\u0100\3\2\2\2E\u0102\3\2\2\2")
        buf.write("G\u0104\3\2\2\2I\u0109\3\2\2\2K\u010f\3\2\2\2M\u0111\3")
        buf.write("\2\2\2O\u0113\3\2\2\2Q\u0115\3\2\2\2S\u0117\3\2\2\2U\u0119")
        buf.write("\3\2\2\2W\u011b\3\2\2\2Y\u011d\3\2\2\2[\u0128\3\2\2\2")
        buf.write("]\u013b\3\2\2\2_\u013e\3\2\2\2a\u0142\3\2\2\2c\u0149\3")
        buf.write("\2\2\2e\u0152\3\2\2\2g\u015f\3\2\2\2i\u016b\3\2\2\2k\u016e")
        buf.write("\3\2\2\2m\u017b\3\2\2\2o\u017f\3\2\2\2q\u0186\3\2\2\2")
        buf.write("s\u018c\3\2\2\2uv\7t\2\2vw\7g\2\2wx\7v\2\2xy\7w\2\2yz")
        buf.write("\7t\2\2z{\7p\2\2{\4\3\2\2\2|}\7x\2\2}~\7c\2\2~\177\7t")
        buf.write("\2\2\177\6\3\2\2\2\u0080\u0081\7f\2\2\u0081\u0082\7{\2")
        buf.write("\2\u0082\u0083\7p\2\2\u0083\u0084\7c\2\2\u0084\u0085\7")
        buf.write("o\2\2\u0085\u0086\7k\2\2\u0086\u0087\7e\2\2\u0087\b\3")
        buf.write("\2\2\2\u0088\u0089\7h\2\2\u0089\u008a\7w\2\2\u008a\u008b")
        buf.write("\7p\2\2\u008b\u008c\7e\2\2\u008c\n\3\2\2\2\u008d\u008e")
        buf.write("\7h\2\2\u008e\u008f\7q\2\2\u008f\u0090\7t\2\2\u0090\f")
        buf.write("\3\2\2\2\u0091\u0092\7w\2\2\u0092\u0093\7p\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7k\2\2\u0095\u0096\7n\2\2\u0096\16")
        buf.write("\3\2\2\2\u0097\u0098\7d\2\2\u0098\u0099\7{\2\2\u0099\20")
        buf.write("\3\2\2\2\u009a\u009b\7d\2\2\u009b\u009c\7t\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\u009e\7c\2\2\u009e\u009f\7m\2\2\u009f\22")
        buf.write("\3\2\2\2\u00a0\u00a1\7e\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8\7g\2\2\u00a8\24")
        buf.write("\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7h\2\2\u00ab\26")
        buf.write("\3\2\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af")
        buf.write("\7u\2\2\u00af\u00b0\7g\2\2\u00b0\30\3\2\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7h\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7i\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\34\3\2\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7f\2\2\u00bf\36\3\2\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7o\2\2\u00c3\u00c4")
        buf.write("\7d\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6 \3")
        buf.write("\2\2\2\u00c7\u00c8\7d\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7q\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\"\3\2\2\2\u00cf\u00d0")
        buf.write("\7u\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7i\2\2\u00d5$\3")
        buf.write("\2\2\2\u00d6\u00d7\7?\2\2\u00d7\u00d8\7?\2\2\u00d8&\3")
        buf.write("\2\2\2\u00d9\u00da\7\60\2\2\u00da\u00db\7\60\2\2\u00db")
        buf.write("\u00dc\7\60\2\2\u00dc(\3\2\2\2\u00dd\u00de\7>\2\2\u00de")
        buf.write("\u00df\7/\2\2\u00df*\3\2\2\2\u00e0\u00e1\7@\2\2\u00e1")
        buf.write("\u00e2\7?\2\2\u00e2,\3\2\2\2\u00e3\u00e4\7@\2\2\u00e4")
        buf.write(".\3\2\2\2\u00e5\u00e6\7>\2\2\u00e6\u00e7\7?\2\2\u00e7")
        buf.write("\60\3\2\2\2\u00e8\u00e9\7>\2\2\u00e9\62\3\2\2\2\u00ea")
        buf.write("\u00eb\7#\2\2\u00eb\u00ec\7?\2\2\u00ec\64\3\2\2\2\u00ed")
        buf.write("\u00ee\7?\2\2\u00ee\66\3\2\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7t\2\2\u00f18\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7f\2\2\u00f5:\3\2\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7v\2\2\u00f9")
        buf.write("<\3\2\2\2\u00fa\u00fb\7\'\2\2\u00fb>\3\2\2\2\u00fc\u00fd")
        buf.write("\7-\2\2\u00fd@\3\2\2\2\u00fe\u00ff\7/\2\2\u00ffB\3\2\2")
        buf.write("\2\u0100\u0101\7,\2\2\u0101D\3\2\2\2\u0102\u0103\7\61")
        buf.write("\2\2\u0103F\3\2\2\2\u0104\u0105\7v\2\2\u0105\u0106\7t")
        buf.write("\2\2\u0106\u0107\7w\2\2\u0107\u0108\7g\2\2\u0108H\3\2")
        buf.write("\2\2\u0109\u010a\7h\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010eJ\3")
        buf.write("\2\2\2\u010f\u0110\7*\2\2\u0110L\3\2\2\2\u0111\u0112\7")
        buf.write("+\2\2\u0112N\3\2\2\2\u0113\u0114\7]\2\2\u0114P\3\2\2\2")
        buf.write("\u0115\u0116\7_\2\2\u0116R\3\2\2\2\u0117\u0118\7}\2\2")
        buf.write("\u0118T\3\2\2\2\u0119\u011a\7\177\2\2\u011aV\3\2\2\2\u011b")
        buf.write("\u011c\7.\2\2\u011cX\3\2\2\2\u011d\u011e\7%\2\2\u011e")
        buf.write("\u011f\7%\2\2\u011f\u0123\3\2\2\2\u0120\u0122\n\2\2\2")
        buf.write("\u0121\u0120\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\b-\2\2\u0127Z\3\2\2\2\u0128\u012c")
        buf.write("\t\3\2\2\u0129\u012b\t\4\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\\\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\5_\60")
        buf.write("\2\u0130\u0132\5a\61\2\u0131\u0133\5c\62\2\u0132\u0131")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u013c\3\2\2\2\u0134")
        buf.write("\u0136\5_\60\2\u0135\u0137\5a\61\2\u0136\u0135\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u013a\5")
        buf.write("c\62\2\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u012f\3\2\2\2\u013b\u0134\3\2\2\2\u013c")
        buf.write("^\3\2\2\2\u013d\u013f\t\5\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141`\3\2\2\2\u0142\u0146\7\60\2\2\u0143\u0145\t\5\2")
        buf.write("\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147b\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014b\t\6\2\2\u014a\u014c\t\7\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3\2\2\2")
        buf.write("\u014d\u014f\t\5\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151d")
        buf.write("\3\2\2\2\u0152\u0159\7$\2\2\u0153\u0158\n\b\2\2\u0154")
        buf.write("\u0158\5i\65\2\u0155\u0156\t\t\2\2\u0156\u0158\t\n\2\2")
        buf.write("\u0157\u0153\3\2\2\2\u0157\u0154\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c")
        buf.write("\u015d\7$\2\2\u015d\u015e\b\63\3\2\u015ef\3\2\2\2\u015f")
        buf.write("\u0166\7$\2\2\u0160\u0165\n\b\2\2\u0161\u0165\5i\65\2")
        buf.write("\u0162\u0163\t\t\2\2\u0163\u0165\t\n\2\2\u0164\u0160\3")
        buf.write("\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a\b\64\4")
        buf.write("\2\u016ah\3\2\2\2\u016b\u016c\7^\2\2\u016c\u016d\t\13")
        buf.write("\2\2\u016dj\3\2\2\2\u016e\u0175\7$\2\2\u016f\u0174\n\b")
        buf.write("\2\2\u0170\u0174\5i\65\2\u0171\u0172\t\t\2\2\u0172\u0174")
        buf.write("\t\n\2\2\u0173\u016f\3\2\2\2\u0173\u0170\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0178\u0179\5m\67\2\u0179\u017a\b\66\5\2\u017a")
        buf.write("l\3\2\2\2\u017b\u017c\7^\2\2\u017c\u017d\n\13\2\2\u017d")
        buf.write("n\3\2\2\2\u017e\u0180\t\f\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\b8\2\2\u0184p\3\2\2\2")
        buf.write("\u0185\u0187\7\f\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u018b\b9\2\2\u018br\3\2\2\2\u018c\u018d")
        buf.write("\13\2\2\2\u018d\u018e\b:\6\2\u018et\3\2\2\2\25\2\u0123")
        buf.write("\u012c\u0132\u0136\u0139\u013b\u0140\u0146\u014b\u0150")
        buf.write("\u0157\u0159\u0164\u0166\u0173\u0175\u0181\u0188\7\b\2")
        buf.write("\2\3\63\2\3\64\3\3\66\4\3:\5")
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
    IDENTIFIERS = 45
    NUMBER = 46
    STRINGLIT = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    WS = 50
    NEW_LINE = 51
    ERROR_CHAR = 52

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
            "COMMENT", "IDENTIFIERS", "NUMBER", "STRINGLIT", "UNCLOSE_STRING", 
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
                  "COMMA", "COMMENT", "IDENTIFIERS", "NUMBER", "INTPART", 
                  "DECPART", "EXPPART", "STRINGLIT", "UNCLOSE_STRING", "LI_ESCAPE", 
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
            actions[49] = self.STRINGLIT_action 
            actions[50] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_CHAR_action 
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
     


