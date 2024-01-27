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
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'boolean'", "'string'", "'=='", 
                     "'...'", "'>='", "'>'", "'<='", "'<'", "'!='", "'<-'", 
                     "'='", "'or'", "'and'", "'not'", "'%'", "'+'", "'-'", 
                     "'*'", "'/'", "'true'", "'false'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "','", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "EQUAL_OPERATOR", "CONCAT_OPERATOR", "GE_OPERATOR", 
                      "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", "NE_OPERATOR", 
                      "ASSIGN1_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
                      "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", 
                      "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                      "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", "RB", "LSB", 
                      "RSB", "LPT", "RPT", "COMMA", "RETURN_KEY", "VAR_KEY", 
                      "DYNAMIC_KEY", "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", 
                      "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", 
                      "ELIF_KEY", "BEGIN_KEY", "END_KEY", "STRING", "IDENTIFIERS", 
                      "COMMENT", "NUMBER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "NEWLINE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    NUM_TYPE=1
    BOOL_TYPE=2
    STRING_TYPE=3
    EQUAL_OPERATOR=4
    CONCAT_OPERATOR=5
    GE_OPERATOR=6
    G_OPERATOR=7
    LE_OPERATOR=8
    L_OPERATOR=9
    NE_OPERATOR=10
    ASSIGN1_OPERATOR=11
    ASSIGN2_OPERATOR=12
    OR_OPERATOR=13
    AND_OPERATOR=14
    NOT_OPERATOR=15
    MODULO_OPERATOR=16
    ADD_OPERATOR=17
    SUB_OPERATOR=18
    MUL_OPERATOR=19
    DIV_OPERATOR=20
    TRUE_BOOLEAN=21
    FALSE_BOOLEAN=22
    LB=23
    RB=24
    LSB=25
    RSB=26
    LPT=27
    RPT=28
    COMMA=29
    RETURN_KEY=30
    VAR_KEY=31
    DYNAMIC_KEY=32
    FUNC_KEY=33
    FOR_KEY=34
    UNTIL_KEY=35
    BY_KEY=36
    BREAK_KEY=37
    CONTINUE_KEY=38
    IF_KEY=39
    ELSE_KEY=40
    ELIF_KEY=41
    BEGIN_KEY=42
    END_KEY=43
    STRING=44
    IDENTIFIERS=45
    COMMENT=46
    NUMBER=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    NEWLINE=51
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

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





