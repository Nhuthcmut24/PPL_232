// My ID: 2212481
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

//KEY WORD

RETURN_KEY: 'return';

VAR_KEY: 'var';

DYNAMIC_KEY: 'dynamic';

FUNC_KEY: 'func';

FOR_KEY: 'for';

UNTIL_KEY: 'until';

BY_KEY: 'by';

BREAK_KEY: 'break';

CONTINUE_KEY: 'continue';

IF_KEY: 'if';

ELSE_KEY: 'else';

ELIF_KEY: 'elif';

BEGIN_KEY: 'begin';

END_KEY: 'end';

// TYPE

NUM_TYPE: 'number';

BOOL_TYPE: 'boolean';

STRING_TYPE: 'string';

//OPERATOR

EQUAL_OPERATOR: '==';

CONCAT_OPERATOR: '...';

ASSIGN1_OPERATOR: '<-';

GE_OPERATOR: '>=';

G_OPERATOR: '>';

LE_OPERATOR: '<=';

L_OPERATOR: '<';

NE_OPERATOR: '!=';

ASSIGN2_OPERATOR: '=';

OR_OPERATOR: 'or';

AND_OPERATOR: 'and';

NOT_OPERATOR: 'not';

MODULO_OPERATOR: '%';

ADD_OPERATOR: '+';

SUB_OPERATOR: '-';

MUL_OPERATOR: '*';

DIV_OPERATOR: '/';

//BOOLEAN

TRUE_BOOLEAN: 'true';

FALSE_BOOLEAN: 'false';

//SEPARATOR

LB: '(';

RB: ')';

LSB: '[';

RSB: ']';

LPT: '{';

RPT: '}';

COMMA: ',';

//COMMENT

COMMENT: '##' ~[\r\n]* -> skip;

//IDENTIFIER

IDENTIFIERS: [A-Za-z_][0-9A-Za-z_]*;

//LITERAL

NUMBER: (INTPART DECPART EXPPART? | INTPART DECPART? EXPPART?);
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: ('e' | 'E') ('+' | '-')? [0-9]+;

STRINGLIT:
	'"' (~["\n\\]|LI_ESCAPE|[']["])* '"' {self.text = self.text[1:-1].replace('\'"','"')};

//ERROR

UNCLOSE_STRING: '"' (~["\n\\]|LI_ESCAPE|[']["])*   {raise UncloseString(self.text[1:])};

fragment LI_ESCAPE: ('\\' ['bftr\\]) ;

ILLEGAL_ESCAPE:
	'"' (~["\n\\]|LI_ESCAPE|[']["])*  ILL_ESCAPE {raise IllegalEscape(self.text[1:])};

fragment ILL_ESCAPE: '\\' ~['btfr\\];

//NEWLINE & WS
WS: [ \t\r\f]+ -> skip; // skip spaces, tabs, newlines

NEW_LINE: '\n'+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};