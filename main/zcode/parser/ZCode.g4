// My ID: 2212481
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decllist;

decllist: decl decllist | decl;

decl: vardecl | funcdecl;

vardecl: typdecl | varkeydecl | dynamicdecl;

typdecl: typ ID (ASSIGN1_OPERATOR expr)? NEW_LINE;

expr: expr1 CONCAT_OPERATOR expr1 | expr1;

expr1: expr2 relationaloperator expr2 | expr2;

expr2: expr2 (AND_OPERATOR | OR_OPERATOR) expr3 | expr3;

expr3: expr3 (ADD_OPERATOR | SUB_OPERATOR) expr4 | expr4;

expr4:
	expr4 (MUL_OPERATOR | DIV_OPERATOR | MODULO_OPERATOR) expr5
	| expr5;

expr5: expr6 NOT_OPERATOR expr5 | expr6;

expr6: SUB_OPERATOR expr6 | expr7;

expr7: expr7 indexoperator expr8 | expr8;

indexoperator: (ID | funccallstmt) LSB indexope RSB;

indexope: expr | expr COMMA indexope;

expr8: ID | funccallstmt;

relationaloperator:
	EQUAL_OPERATOR
	| ASSIGN2_OPERATOR
	| NE_OPERATOR
	| GE_OPERATOR
	| G_OPERATOR
	| LE_OPERATOR
	| L_OPERATOR;

logicoperator: AND_OPERATOR | OR_OPERATOR | NOT_OPERATOR;

arithmeticoperator:
	ADD_OPERATOR
	| SUB_OPERATOR
	| MODULO_OPERATOR
	| DIV_OPERATOR
	| MUL_OPERATOR;

varkeydecl: VAR_KEY ASSIGN1_OPERATOR expr NEW_LINE;

dynamicdecl: DYNAMIC_KEY ID (ASSIGN1_OPERATOR expr)? NEW_LINE;

typ: NUM_TYPE | BOOL_TYPE | STRING_TYPE;

arraydecl: typ ID LSB sizelist RSB NEW_LINE;

arrayvalue: arrayval | arrayvallist;

arrayval: LSB sizelist RSB;

arrayvallist: LSB listarrayval RSB;

listarrayval: arrayval COMMA listarrayval | arrayval;

sizelist: INTLIT COMMA sizelist | INTLIT;

statement:
	vardecl
	| assignstmt
	| ifstmt
	| forstmt
	| breakstmt
	| continuestmt
	| returnstmt
	| funccallstmt
	| blockstmt;

blockstmt: BEGIN_KEY NEW_LINE stmtlist END_KEY NEW_LINE;

stmtlist: statement stmtlist |;

funccallstmt: ID LB argumentlist RB NEW_LINE;

argumentlist: argumentprime |;

argumentprime: argument COMMA argumentprime | argument;

argument: literal;

literal: INTLIT | STRINGLIT | NUMBER | ID;

returnstmt: RETURN_KEY NEW_LINE | RETURN_KEY expr NEW_LINE;

continuestmt: CONTINUE_KEY NEW_LINE;

forstmt:
	FOR_KEY numbervariable UNTIL_KEY expr BY_KEY expr statement NEW_LINE;

numbervariable: ID;

breakstmt: BREAK_KEY NEW_LINE;

ifstmt:
	IF_KEY expr newlinelist statement eliflist (
		ELSE_KEY statement
	)? NEW_LINE;

eliflist: elifcomponent eliflist |;

elifcomponent: ELIF_KEY expr newlinelist statement NEW_LINE;

assignstmt: lhs ASSIGN1_OPERATOR expr;

newlinelist: NEW_LINE newlinelist |;

newlinelistnonull: NEW_LINE newlinelist | NEW_LINE;

lhs: ID | indexelement;

indexelement: ID LSB sizelist RSB;

funcdecl: FUNC_KEY ID paralist;

paralist: LB parameterlist RB;

parameterlist: paraprime |;

paraprime: para COMMA paraprime | para;

para: typ ID;

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

ID: [A-Za-z_][0-9A-Za-z_]*;

//LITERAL

NUMBER: (INTPART DECPART EXPPART? | INTPART DECPART? EXPPART?);
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: ('e' | 'E') ('+' | '-')? [0-9]+;

INTLIT: [0-9]+;

STRINGLIT:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* '"' {self.text = self.text[1:-1].replace('\'"','"')};

//ERROR

UNCLOSE_STRING:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* {raise UncloseString(self.text[1:])};

fragment LI_ESCAPE: ('\\' ['bftr\\]);

ILLEGAL_ESCAPE:
	'"' (~["\n\\] | LI_ESCAPE | [']["])* ILL_ESCAPE {raise IllegalEscape(self.text[1:])};

fragment ILL_ESCAPE: '\\' ~['btfr\\];

//NEWLINE & WS

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs, newlines

NEW_LINE: '\n'+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};