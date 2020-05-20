%{
  #include <stdio.h>
  extern void yyerror();
  extern int yylex();
  extern char* yytext;
  extern int yylineno;
%}

%define parse.lac full
%define parse.error verbose

%union{
	char* dataType;
	char charVal;
	int intVal;
	float floatVal;
	char* strVal;
}

%token ASPAS_S
%token IGUAL
%token P_VIRGULA
%token VIRGULA
%token ABRE_P
%token FECHA_P
%token DOIS_P
%token DEF
%token DEF_E
%token WHILE
%token WHILE_E
%token IF
%token ELIF
%token ELSE
%token IF_E
%token AND
%token OR
%token PRINT
%token TRUE
%token FALSE
%token IS
%token NOT
%token MENOR
%token MAIOR
%token MENOR_I
%token MAIOR_I
%token MAIS
%token MENOS
%token MULT
%token DIV
%token RESTO
%token DIV_INT
%token POW
%token <dataType> DATA_TYPE
%token <charVal> CHARACTER_VALUE
%token <intVal> INTEGER_VALUE
%token <floatVal> FLOAT_VALUE
%token <strVal> STRING_VALUE
%token <strVal> IDENTIFIER_VALUE

/* Nao terminais */
%type <strVal> BLOCO_N
%type <strVal> FUNC_DEF_N
%type <strVal> WHILE_N
%type <strVal> IF_N
%type <strVal> ELIF_N
%type <strVal> CONDITION_N
%type <strVal> FUNC_IDENTIFIER_VALUE
%type <strVal> ARGS_N
%type <strVal> ARGS2_N
%type <strVal> COND_OP_N
%type <strVal> EXPR_N
%type <strVal> TERM_N
%type <strVal> FACTOR_N
%type <strVal> RELEX_N

%%
BLOCO_N: FUNC_DEF_N
			| WHILE_N
			| IF_N
			| DATA_TYPE IDENTIFIER_VALUE IGUAL CONDITION_N P_VIRGULA
			| PRINT CONDITION_N P_VIRGULA
;

FUNC_DEF_N: DEF DATA_TYPE IDENTIFIER_VALUE ABRE_P ARGS_N FECHA_P DOIS_P BLOCO_N DEF_E P_VIRGULA;

WHILE_N: WHILE ABRE_P CONDITION_N FECHA_P DOIS_P BLOCO_N WHILE_E P_VIRGULA;

IF_N: IF ABRE_P CONDITION_N FECHA_P DOIS_P BLOCO_N IF_E P_VIRGULA
	| IF ABRE_P CONDITION_N FECHA_P DOIS_P BLOCO_N ELIF_N IF_E P_VIRGULA
;

ELIF_N: ELIF ABRE_P CONDITION_N FECHA_P DOIS_P BLOCO_N ELIF_N
		| ELIF ABRE_P CONDITION_N FECHA_P DOIS_P BLOCO_N ELSE DOIS_P BLOCO_N

FUNC_IDENTIFIER_VALUE: IDENTIFIER_VALUE ABRE_P ARGS2_N FECHA_P;

CONDITION_N: RELEX_N
			| RELEX_N AND CONDITION_N
			| RELEX_N OR CONDITION_N
;

RELEX_N: EXPR_N
		| EXPR_N COND_OP_N RELEX_N
;

EXPR_N: TERM_N
		| TERM_N MAIS EXPR_N
		| TERM_N MENOS EXPR_N
;

TERM_N: FACTOR_N
		| FACTOR_N MULT TERM_N
		| FACTOR_N DIV TERM_N
		| FACTOR_N RESTO TERM_N
		| FACTOR_N DIV_INT TERM_N
;

FACTOR_N: INTEGER_VALUE
			| FLOAT_VALUE
			| TRUE
			| FALSE
			| STRING_VALUE
			| CHARACTER_VALUE
			| MAIS FACTOR_N
			| MENOS FACTOR_N
			| ABRE_P CONDITION_N FECHA_P
			| IDENTIFIER_VALUE
			| FUNC_IDENTIFIER_VALUE
;

COND_OP_N: IS
			| NOT 
			| MAIOR 
			| MAIOR_I 
			| MENOR 
			| MENOR_I
;

ARGS_N: DATA_TYPE FUNC_IDENTIFIER_VALUE
		| DATA_TYPE IDENTIFIER_VALUE VIRGULA ARGS_N
;

ARGS2_N: CONDITION_N
		| DATA_TYPE IDENTIFIER_VALUE
		| CONDITION_N VIRGULA ARGS2_N
		| DATA_TYPE IDENTIFIER_VALUE VIRGULA ARGS2_N
;
%%

int main(){

  yyparse();
  printf("No Errors!!\n");
  return 0;
}

