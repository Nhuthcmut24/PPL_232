# Generated from c:/Users/Admin/Documents/HK232/PPL/Assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,0,0,
        1,3,1,1,0,0,0,0
    ]

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
                      "RSB", "LPT", "RPT", "COMMA", "COMMENT", "IDENTIFIERS", 
                      "NUMBER", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "WS", "NEW_LINE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

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
    IDENTIFIERS=45
    NUMBER=46
    STRINGLIT=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    WS=50
    NEW_LINE=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





