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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'number'", "'boolean'", 
                     "'string'", "'=='", "'...'", "'>='", "'>'", "'<='", 
                     "'<'", "'!='", "'<-'", "'='", "'or'", "'and'", "'not'", 
                     "'%'", "'+'", "'-'", "'*'", "'/'", "'true'", "'false'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'''", "'\\'" ]

    symbolicNames = [ "<INVALID>", "STRING", "NUM_TYPE", "BOOL_TYPE", "STRING_TYPE", 
                      "EQUAL_OPERATOR", "CONCAT_OPERATOR", "GE_OPERATOR", 
                      "G_OPERATOR", "LE_OPERATOR", "L_OPERATOR", "NE_OPERATOR", 
                      "ASSIGN1_OPERATOR", "ASSIGN2_OPERATOR", "OR_OPERATOR", 
                      "AND_OPERATOR", "NOT_OPERATOR", "MODULO_OPERATOR", 
                      "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                      "TRUE_BOOLEAN", "FALSE_BOOLEAN", "LB", "RB", "LSB", 
                      "RSB", "LPT", "RPT", "COMMA", "RETURN_KEY", "VAR_KEY", 
                      "DYNAMIC_KEY", "FUNC_KEY", "FOR_KEY", "UNTIL_KEY", 
                      "BY_KEY", "BREAK_KEY", "CONTINUE_KEY", "IF_KEY", "ELSE_KEY", 
                      "ELIF_KEY", "BEGIN_KEY", "END_KEY", "SINGLEQUOTE", 
                      "BACKSLASH", "IDENTIFIERS", "NUMBER", "COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    STRING=1
    NUM_TYPE=2
    BOOL_TYPE=3
    STRING_TYPE=4
    EQUAL_OPERATOR=5
    CONCAT_OPERATOR=6
    GE_OPERATOR=7
    G_OPERATOR=8
    LE_OPERATOR=9
    L_OPERATOR=10
    NE_OPERATOR=11
    ASSIGN1_OPERATOR=12
    ASSIGN2_OPERATOR=13
    OR_OPERATOR=14
    AND_OPERATOR=15
    NOT_OPERATOR=16
    MODULO_OPERATOR=17
    ADD_OPERATOR=18
    SUB_OPERATOR=19
    MUL_OPERATOR=20
    DIV_OPERATOR=21
    TRUE_BOOLEAN=22
    FALSE_BOOLEAN=23
    LB=24
    RB=25
    LSB=26
    RSB=27
    LPT=28
    RPT=29
    COMMA=30
    RETURN_KEY=31
    VAR_KEY=32
    DYNAMIC_KEY=33
    FUNC_KEY=34
    FOR_KEY=35
    UNTIL_KEY=36
    BY_KEY=37
    BREAK_KEY=38
    CONTINUE_KEY=39
    IF_KEY=40
    ELSE_KEY=41
    ELIF_KEY=42
    BEGIN_KEY=43
    END_KEY=44
    SINGLEQUOTE=45
    BACKSLASH=46
    IDENTIFIERS=47
    NUMBER=48
    COMMENT=49
    WS=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52
    ERROR_CHAR=53

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





