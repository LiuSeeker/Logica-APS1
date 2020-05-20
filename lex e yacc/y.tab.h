/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ASPAS_S = 258,
    IGUAL = 259,
    P_VIRGULA = 260,
    VIRGULA = 261,
    ABRE_P = 262,
    FECHA_P = 263,
    DOIS_P = 264,
    DEF = 265,
    DEF_E = 266,
    WHILE = 267,
    WHILE_E = 268,
    IF = 269,
    ELIF = 270,
    ELSE = 271,
    IF_E = 272,
    AND = 273,
    OR = 274,
    PRINT = 275,
    TRUE = 276,
    FALSE = 277,
    IS = 278,
    NOT = 279,
    MENOR = 280,
    MAIOR = 281,
    MENOR_I = 282,
    MAIOR_I = 283,
    MAIS = 284,
    MENOS = 285,
    MULT = 286,
    DIV = 287,
    RESTO = 288,
    DIV_INT = 289,
    POW = 290,
    DATA_TYPE = 291,
    CHARACTER_VALUE = 292,
    INTEGER_VALUE = 293,
    FLOAT_VALUE = 294,
    STRING_VALUE = 295,
    IDENTIFIER_VALUE = 296
  };
#endif
/* Tokens.  */
#define ASPAS_S 258
#define IGUAL 259
#define P_VIRGULA 260
#define VIRGULA 261
#define ABRE_P 262
#define FECHA_P 263
#define DOIS_P 264
#define DEF 265
#define DEF_E 266
#define WHILE 267
#define WHILE_E 268
#define IF 269
#define ELIF 270
#define ELSE 271
#define IF_E 272
#define AND 273
#define OR 274
#define PRINT 275
#define TRUE 276
#define FALSE 277
#define IS 278
#define NOT 279
#define MENOR 280
#define MAIOR 281
#define MENOR_I 282
#define MAIOR_I 283
#define MAIS 284
#define MENOS 285
#define MULT 286
#define DIV 287
#define RESTO 288
#define DIV_INT 289
#define POW 290
#define DATA_TYPE 291
#define CHARACTER_VALUE 292
#define INTEGER_VALUE 293
#define FLOAT_VALUE 294
#define STRING_VALUE 295
#define IDENTIFIER_VALUE 296

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 12 "syntax.y" /* yacc.c:1909  */

	char* dataType;
	char charVal;
	int intVal;
	float floatVal;
	char* strVal;

#line 144 "y.tab.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
