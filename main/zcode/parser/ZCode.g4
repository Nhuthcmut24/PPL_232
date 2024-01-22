grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: ;

STRING: '"'(~["]|[']["])*'"' {self.text = self.text[1:-1]};

NUM_TYPE: 'number';

BOOL_TYPE: 'boolean';

STRING_TYPE: 'string';

EQUAL_OPERATOR: '==';

CONCAT_OPERATOR: '...';

GE_OPERATOR: '>=';

G_OPERATOR: '>';

LE_OPERATOR: '<=';

L_OPERATOR: '<';

NE_OPERATOR: '!=';

ASSIGN1_OPERATOR: '<-';

ASSIGN2_OPERATOR: '=';

OR_OPERATOR: 'or';

AND_OPERATOR: 'and';

NOT_OPERATOR: 'not';

MODULO_OPERATOR: '%';

ADD_OPERATOR: '+';

SUB_OPERATOR: '-';

MUL_OPERATOR: '*';

DIV_OPERATOR: '/';

TRUE_BOOLEAN: 'true';

FALSE_BOOLEAN: 'false';

LB: '(';

RB: ')';

LSB: '[';

RSB: ']';

LPT: '{';

RPT: '}';

COMMA: ',';

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

SINGLEQUOTE: '\'' {self.text = self.text.replace('\\','')};

BACKSLASH: '\\' {self.text = self.text[0]};

IDENTIFIERS: [A-Za-z_][0-9A-Za-z_]*;

NUMBER: (INTPART DECPART EXPPART?|INTPART DECPART? EXPPART?);
fragment INTPART: ([0]|[1-9][0-9]*);
fragment DECPART: '.'[0-9]*;
fragment EXPPART: ('e'|'E')('+'|'-')?[0-9]+;

COMMENT: '##' ~[\r\n]* ->skip;

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: FORMAL INFORMAL* {raise UncloseString(self.text[1:-1])};

fragment FORMAL: '"';

fragment INFORMAL: ~["];

ILLEGAL_ESCAPE: [\] ~[tnrbf] {raise IllegalEscape(self.text)};

ERROR_CHAR: . {raise ErrorToken(self.text)};