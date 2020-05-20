/* https://github.com/ajhalthor/interpreter */
%{
    #include <string.h>
    #include <stdlib.h>
    #include "y.tab.h"
    void extern yyerror(char*);
    void InvalidToken();
%}

whitespace      [ \t\r\v\f]
linefeed        \n

%%
"void" | "int" | "char" | "float" | "bool"		{yylval.dataType = strdup(yytext); return DATA_TYPE;}
"'"												{return ASPAS_S;}
"="												{return IGUAL;}
";"												{return	P_VIRGULA;}
","												{return	VIRGULA;}
"("												{return ABRE_P;}
")"												{return FECHA_P;}
":"												{return DOIS_P;}
"eb"											{return DEF;}
"zeb"											{return DEF_E;}
"ible"											{return WHILE;}
"zible"											{return WHILE_E;}
"ib"											{return IF;}
"ebib"											{return ELIF;}
"eble"											{return ELSE;}
"zib"											{return IF_E;}
"obe"											{return AND;}
"obou"											{return OR;}
"zrint"                                         {return PRINT;}
"true"                                          {return TRUE;}
"false"                                         {return FALSE;}
"ob"											{return IS;}
"nob"											{return NOT;}
"<b"											{return MENOR;}
">b"											{return MAIOR;}
"<=b"											{return MENOR_I;}
">=b"											{return MAIOR_I;}
"+"												{return	MAIS;}
"-"												{return MENOS;}
"*"												{return MULT;}
"/"												{return DIV;}
"%"												{return RESTO;}
"//"											{return DIV_INT;}
"**"											{return POW;}
[\'][a-zA-Z][\']								{yylval.charVal = yytext[1]; return CHARACTER_VALUE;}
[\"][a-zA-Z][\"]								{yylval.charVal = yytext[1]; return CHARACTER_VALUE;}
[-+]?[0-9]+                                     {yylval.intVal = atoi(yytext); return INTEGER_VALUE;}
[-+]?[0-9]*\.?[0-9]+                            {yylval.floatVal = atof(yytext); return FLOAT_VALUE;}
[a-zA-Z][_a-zA-Z0-9]*							{yylval.strVal = strdup(yytext); return IDENTIFIER_VALUE;}
\"(\\.|[^"])*\"                                 {yylval.strVal = strdup(yytext); return STRING_VALUE;}


{linefeed}                                      {yylineno++;}
{whitespace}                                    ;
.                                               {InvalidToken();}
%%

int yywrap(void){
    return 1;
}

void yyerror(char *s) {
    fprintf(stderr, "\nERROR ON LINE %d : \n %s\n", yylineno, s);
    exit(0);
}

void InvalidToken(){
    printf("ERROR ON LINE %d : \n Invalid Token %s\n", yylineno,yytext);
    exit(0);
}
