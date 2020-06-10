import sys
import re
from collections import defaultdict

class Token:
    def __init__(self, t, value):
        self.type = t
        self.value = value

class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None
        self.line_n = 1
        self.line = ""
        self.selectNext()

    def selectNext(self):
        if self.position < len(self.origin):
            while self.origin[self.position] == " " or self.origin[self.position] is "\n":
                if self.origin[self.position] is "\n":
                    self.line_n += 1
                    self.line = ""
                self.position += 1
                if self.position >= len(self.origin):
                    self.actual = Token("EOF", "")
                    return

            if self.origin[self.position].isdigit():
                i = self.position
                self.position += 1
                if self.position < len(self.origin): # N eficiente
                    while self.origin[self.position].isdigit():
                        self.position += 1
                        if self.position >= len(self.origin):
                            break
                    if self.origin[self.position] == ".":
                        self.position += 1
                        while self.origin[self.position].isdigit():
                            self.position += 1
                            if self.position >= len(self.origin):
                                break
                        self.actual = Token("FLOAT_VAL", float(self.origin[i:self.position]))
                    else:
                        self.actual = Token("INT_VAL", int(self.origin[i:self.position]))
                else:
                    self.actual = Token("INT_VAL", int(self.origin[i:self.position]))
                return
            elif self.origin[self.position] == "+":
                self.actual = Token("PLUS", "+")
                self.position += 1
                return
            elif self.origin[self.position] == "-":
                self.actual = Token("MINUS", "-")
                self.position += 1
                return
            elif self.origin[self.position] == "*":
                self.actual = Token("MULT", "*")
                self.position += 1
                if self.origin[self.position] == "*":
                    self.actual = Token("POW", "**")
                    self.position += 1
                return
            elif self.origin[self.position] == "%":
                self.actual = Token("RESTO", "%")
                self.position += 1
                return
            elif self.origin[self.position] == "/":
                self.actual = Token("DIV", "/")
                self.position += 1
                if self.origin[self.position] == "/":
                    self.actual = Token("DIV_INT", "//")
                    self.position += 1
                return
            elif self.origin[self.position] == "(":
                self.actual = Token("ABRE_PAR", "(")
                self.position += 1
                return
            elif self.origin[self.position] == ")":
                self.actual = Token("FECHA_PAR", ")")
                self.position += 1
                return
            # elif self.origin[self.position] == "{":
            #     self.actual = Token("OCHA", "{")
            #     self.position += 1
            #     return
            # elif self.origin[self.position] == "}":
            #     self.actual = Token("CCHA", "}")
            #     self.position += 1
            #     return
            elif self.origin[self.position] == ";":
                self.actual = Token("P_VIRGULA", ";")
                self.position += 1
                return
            elif self.origin[self.position] == ":":
                self.actual = Token("DOIS_P", ":")
                self.position += 1
                return
            elif self.origin[self.position] == ",":
                self.actual = Token("VIRGULA", ",")
                self.position += 1
                return
            # elif self.origin[self.position] == ".":
            #     self.actual = Token("PONT", ".")
            #     self.position += 1
            #     return
            elif self.origin[self.position] == "=":
                self.actual = Token("IGUAL", "=")
                self.position += 1
                if self.origin[self.position] == "=":
                    self.actual = Token("D_IGUAL", "==")
                    self.position += 1
                return
            elif self.origin[self.position] == ">":
                self.actual = Token("MAIOR", ">")
                self.position += 1
                return
            elif self.origin[self.position] == "<":
                self.actual = Token("MENOR", "<")
                self.position += 1
                return
            elif self.origin[self.position] == "!":
                self.actual = Token("NOT", "!")
                self.position += 1
                return
            # elif self.origin[self.position] == "?":
            #     i = self.position
            #     self.position += 1
            #     if self.position < len(self.origin):
            #         if self.origin[self.position] == ">":
            #             self.actual = Token("CPRO", self.origin[i:self.position])
            #             self.position += 1
            #     return
            # elif self.origin[self.position] == "$":
            #     i = self.position
            #     self.position += 1
            #     if self.origin[self.position].isalpha():
            #         self.position += 1
            #         if self.position < len(self.origin): # N eficiente
            #             while self.origin[self.position].isdigit() or self.origin[self.position].isalpha() or self.origin[self.position] == "_":
            #                 self.position += 1
            #                 if self.position >= len(self.origin):
            #                     break
            #     self.actual = Token("IDEN", self.origin[i:self.position])
            #     return
            elif self.origin[self.position].isalpha():
                i = self.position
                self.position += 1
                if self.position < len(self.origin): # N eficiente
                    while self.origin[self.position].isalpha():
                        self.position += 1
                        if self.position >= len(self.origin):
                            break
                if self.origin[i:self.position].lower() == "zrint":
                    self.actual = Token("PRINT", "print")
                    return
                elif self.origin[i:self.position].lower() == "obou":
                    self.actual = Token("OR", "or")
                    return
                elif self.origin[i:self.position].lower() == "obe":
                    self.actual = Token("AND", "and")
                    return
                elif self.origin[i:self.position].lower() == "ible":
                    self.actual = Token("WHILE", "while")
                    return
                elif self.origin[i:self.position].lower() == "zible":
                    self.actual = Token("WHILE_E", "while_e")
                    return
                elif self.origin[i:self.position].lower() == "ib":
                    self.actual = Token("IF", "if")
                    return
                elif self.origin[i:self.position].lower() == "ebib":
                    self.actual = Token("ELIF", "elif")
                    return
                elif self.origin[i:self.position].lower() == "eble":
                    self.actual = Token("ELSE", "else")
                    return
                elif self.origin[i:self.position].lower() == "zib":
                    self.actual = Token("IF_E", "if_e")
                    return
                # elif self.origin[i:self.position].lower() == "readline":
                #     self.actual = Token("READ", self.origin[i:self.position].lower())
                #     return
                elif self.origin[i:self.position].lower() == "true":
                    self.actual = Token("TRUE", True)
                    return
                elif self.origin[i:self.position].lower() == "false":
                    self.actual = Token("FALSE", False)
                    return
                elif self.origin[i:self.position].lower() == "eb":
                    self.actual = Token("DEF", "def")
                    return
                elif self.origin[i:self.position].lower() == "zeb":
                    self.actual = Token("DEF_E", "def_e")
                    return
                elif self.origin[i:self.position].lower() == "zeturn":
                    self.actual = Token("RETURN", "return")
                    return
                elif self.origin[i:self.position].lower() == "zinput":
                    self.actual = Token("INPUT", "input")
                    return
                else:
                    while self.origin[self.position].isdigit() or self.origin[self.position].isalpha() or self.origin[self.position] == "_":
                        self.position += 1
                        if self.position >= len(self.origin):
                            break
                    if self.origin[self.position] == "(":
                        self.actual = Token("IDEN", self.origin[i:self.position])
                    else:
                        self.actual = Token("IDEN", self.origin[i:self.position])
            elif self.origin[self.position] == '"':
                i = self.position
                self.position += 1
                if self.position < len(self.origin):
                    while self.origin[self.position] != '"':
                        self.position += 1
                        if self.position >= len(self.origin):
                            break
                    self.actual = Token("STRING_VAL", self.origin[i+1:self.position])
                    self.position += 1
                else:
                    self.actual = Token("STRING_VAL", self.origin[i+1:self.position])
                return
            
            else:
                raise SyntaxError("Caractere nao permitido {}".format(self.origin[self.position]))
            
        else:
            self.actual = Token("EOF", "")


class Parser:
    tokens = None

    # @staticmethod
    # def parseProgram():
    #     if Parser.tokens.actual.type == "OPRO":
    #         ret = Comm()
    #         Parser.tokens.selectNext()
    #         while Parser.tokens.actual.type != "CPRO":
    #             if Parser.tokens.actual.type == "EOF":
    #                 raise SyntaxError("Line {}: Fechamento ?> esperado".format(Parser.tokens.line_n))
    #             ret_t = Parser.parseCommand()
    #             if ret_t is not None:
    #                 ret.children.append(ret_t)
    #         Parser.tokens.selectNext()
    #     else:
    #         raise SyntaxError("Line {}: Abertura de <?php esperado".format(Parser.tokens.line_n))
        
    #     return ret

    # @staticmethod
    # def parseBlock():
    #     if Parser.tokens.actual.type == "OCHA":
    #         ret = Comm()
    #         Parser.tokens.selectNext()
    #         while Parser.tokens.actual.type != "CCHA":
    #             if Parser.tokens.actual.type == "EOF":
    #                 raise SyntaxError("Line {}: Fechamento de chaves esperado".format(Parser.tokens.line_n))
    #             ret_t = Parser.parseCommand()
    #             if ret_t is not None:
    #                 ret.children.append(ret_t)
    #         Parser.tokens.selectNext()
    #     else:
    #         raise SyntaxError("Line {}: Abertura de chaves esperado".format(Parser.tokens.line_n))

    #     return ret

    @staticmethod
    def parseProgram():
        ret = Comm()
        while Parser.tokens.actual.type != "EOF":
            ret_t = Parser.parseCommand()
            if ret_t != None:
                ret.children.append(ret_t)

        if len(ret.children) == 0:
            ret.children.append(NoOp())
        return ret
    
    @staticmethod
    def parseCommand():
        ret = None
        # IDENTIFIER ...
        if Parser.tokens.actual.type == "IDEN":
            ret = Iden(Parser.tokens.actual.value)
            ret2 = FuncCall(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            # ... = RELEX;
            if Parser.tokens.actual.type == "IGUAL":
                ret = Assign(ret)
                Parser.tokens.selectNext()
                ret.children.append(Parser.parseRelationExpression())
                if Parser.tokens.actual.type == "P_VIRGULA":
                    Parser.tokens.selectNext()
                else:
                    raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            # ... (ARGS);
            elif Parser.tokens.actual.type == "ABRE_PAR":
                ret = ret2
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                else:
                    ret.children.append(Parser.parseRelationExpression())
                    while Parser.tokens.actual.type == "VIRGULA":
                        Parser.tokens.selectNext()
                        ret.children.append(Parser.parseRelationExpression())
                    if Parser.tokens.actual.type == "FECHA_PAR":
                        Parser.tokens.selectNext()
                    else:
                        raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                if Parser.tokens.actual.type == "P_VIRGULA":
                    Parser.tokens.selectNext()
                else:
                    raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Assignment ('=') esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))        
        # zrint RELEX;
        elif Parser.tokens.actual.type == "PRINT":
            ret = PRINT()
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseRelationExpression())
            if Parser.tokens.actual.type == "P_VIRGULA":
                Parser.tokens.selectNext()
            else:
                raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # zeturn RELEX;
        elif Parser.tokens.actual.type == "RETURN":
            ret = Return(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseRelationExpression())
            if Parser.tokens.actual.type == "P_VIRGULA":
                Parser.tokens.selectNext()
            else:
                raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # eb IDENTIFIER (ARGS2): COMMAND zeb;
        elif Parser.tokens.actual.type == "DEF":
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "IDEN":
                ret = FuncDef(Parser.tokens.actual.value)
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "ABRE_PAR":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "FECHA_PAR":
                        Parser.tokens.selectNext()
                    else:
                        if Parser.tokens.actual.type == "IDEN":
                            ret.children.append(Iden(Parser.tokens.actual.value))
                            Parser.tokens.selectNext()
                        else:
                            raise SyntaxError("Line {}: Identifier esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        while Parser.tokens.actual.type == "VIRGULA":
                            Parser.tokens.selectNext()
                            if Parser.tokens.actual.type == "IDEN":
                                ret.children.append(Iden(Parser.tokens.actual.value))
                                Parser.tokens.selectNext()
                            else:
                                raise SyntaxError("Line {}: Identifier esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        if Parser.tokens.actual.type == "FECHA_PAR":
                            Parser.tokens.selectNext()
                        else:
                            raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                    if Parser.tokens.actual.type == "DOIS_P":
                        Parser.tokens.selectNext()
                        ret_t = Comm()
                        while Parser.tokens.actual.type != "DEF_E":
                            if Parser.tokens.actual.type == "EOF":
                                raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                            ret_t.children.append(Parser.parseCommand())
                        ret.children.append(ret_t)
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.type == "P_VIRGULA":
                            Parser.tokens.selectNext()
                        else:
                            raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                    else:
                        raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                else:
                    raise SyntaxError("Line {}: Abertura de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Identifier esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # ible (RELEX) : COMMAND zible;
        elif Parser.tokens.actual.type == "WHILE":
            ret = While()
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "ABRE_PAR":
                Parser.tokens.selectNext()
                ret.children.append(Parser.parseRelationExpression())
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "DOIS_P":
                        Parser.tokens.selectNext()
                        ret_t = Comm()
                        ret_t.children.append(Parser.parseCommand())
                        while Parser.tokens.actual.type != "WHILE_E":
                            if Parser.tokens.actual.type == "EOF":
                                raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                            ret_t.children.append(Parser.parseCommand())
                        ret.children.append(ret_t)
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.type == "P_VIRGULA":
                            Parser.tokens.selectNext()
                        else:
                            raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                    else:
                        raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                else:
                    raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Abertura de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # ib (RELEX) : COMMAND
        elif Parser.tokens.actual.type == "IF":
            ret = If()
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "ABRE_PAR":
                Parser.tokens.selectNext()
                ret.children.append(Parser.parseRelationExpression())
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "DOIS_P":
                        Parser.tokens.selectNext()
                        ret_t = Comm()
                        ret_t.children.append(Parser.parseCommand())
                        while Parser.tokens.actual.type != "IF_E" and Parser.tokens.actual.type != "ELIF"  and Parser.tokens.actual.type != "ELSE":
                            if Parser.tokens.actual.type == "EOF":
                                raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                            ret_t.children.append(Parser.parseCommand())
                        ret.children.append(ret_t)
                        if Parser.tokens.actual.type == "ELIF":
                            Parser.tokens.selectNext()
                            ret.children.append(Parser.parseElif())
                            if Parser.tokens.actual.type == "IF_E":
                                Parser.tokens.selectNext()
                                if Parser.tokens.actual.type == "P_VIRGULA":
                                    Parser.tokens.selectNext()
                                else:
                                    raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                            else:
                                raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        elif Parser.tokens.actual.type == "ELSE":
                            Parser.tokens.selectNext()
                            if Parser.tokens.actual.type == "DOIS_P":
                                Parser.tokens.selectNext()
                                ret_t = Comm()
                                ret_t.children.append(Parser.parseCommand())
                                while Parser.tokens.actual.type != "IF_E":
                                    if Parser.tokens.actual.type == "EOF":
                                        raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                                    ret_t.children.append(Parser.parseCommand())
                                ret.children.append(ret_t)
                                if Parser.tokens.actual.type == "IF_E":
                                    Parser.tokens.selectNext()
                                    if Parser.tokens.actual.type == "P_VIRGULA":
                                        Parser.tokens.selectNext()
                                    else:
                                        raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                            else:
                                raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        elif Parser.tokens.actual.type == "IF_E":
                            Parser.tokens.selectNext()
                            if Parser.tokens.actual.type == "P_VIRGULA":
                                Parser.tokens.selectNext()
                            else:
                                raise SyntaxError("Line {}: Ponto e virgula esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        else:
                            raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                    else:
                        raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                else:
                    raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Abertura de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        else:
            if Parser.tokens.actual.type == "P_VIRGULA":
                raise SyntaxError("Line {}: Ponto e virgula desnecessario".format(Parser.tokens.line_n))
            raise SyntaxError("Line {}".format(Parser.tokens.line_n))

        return ret

    @staticmethod
    def parseElif():
        ret = If()
        if Parser.tokens.actual.type == "ABRE_PAR":
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseRelationExpression())
            if Parser.tokens.actual.type == "FECHA_PAR":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "DOIS_P":
                    Parser.tokens.selectNext()
                    ret_t = Comm()
                    ret_t.children.append(Parser.parseCommand())
                    while Parser.tokens.actual.type != "IF_E" and Parser.tokens.actual.type != "ELSE" and Parser.tokens.actual.type != "ELIF":
                        if Parser.tokens.actual.type == "EOF":
                            raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                        ret_t.children.append(Parser.parseCommand())
                    ret.children.append(ret_t)
                    if Parser.tokens.actual.type == "ELIF":
                        Parser.tokens.selectNext()
                        ret.children.append(Parser.parseElif())
                    if Parser.tokens.actual.type == "ELSE":
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.type == "DOIS_P":
                            Parser.tokens.selectNext()
                            ret_t = Comm()
                            ret_t.children.append(Parser.parseCommand())
                            while Parser.tokens.actual.type != "IF_E":
                                if Parser.tokens.actual.type == "EOF":
                                    raise SyntaxError("Line {}: Fechamento de funcao esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                                ret_t.children.append(Parser.parseCommand())
                            ret.children.append(ret_t)
                        else:
                            raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
                else:
                    raise SyntaxError("Line {}: Dois pontos esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value)) 
        else:
            raise SyntaxError("Line {}: Abertura de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        return ret

    @staticmethod
    def parseRelationExpression():
        ret = Parser.parseExpression()
        while Parser.tokens.actual.type == "D_IGUAL" or Parser.tokens.actual.type == "MAIOR" or Parser.tokens.actual.type == "MENOR":
            ret = BinOp(Parser.tokens.actual.value, ret)
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseExpression())
        
        return ret

    @staticmethod
    def parseExpression():
        ret = Parser.parseTerm()
        while Parser.tokens.actual.type == "PLUS" or Parser.tokens.actual.type == "MINUS" or Parser.tokens.actual.type == "OR":
            ret = BinOp(Parser.tokens.actual.value, ret)
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseTerm())
        return ret
    
    @staticmethod
    def parseTerm():        
        ret = Parser.parseFactor()
        while Parser.tokens.actual.type == "MULT" or Parser.tokens.actual.type == "DIV" or Parser.tokens.actual.type == "AND" or Parser.tokens.actual.type == "RESTO" or Parser.tokens.actual.type == "DIV_INT" or Parser.tokens.actual.type == "POW":
            tmp_ret = BinOp(Parser.tokens.actual.value, ret)
            Parser.tokens.selectNext()
            tmp_ret.children.append(Parser.parseFactor())
            ret = tmp_ret
        
        return ret

    @staticmethod
    def parseFactor():
        # INT
        if Parser.tokens.actual.type == "INT_VAL":
            ret = IntVal(int(Parser.tokens.actual.value))
            Parser.tokens.selectNext()
        # ("+" | "-" | "!"), FACTOR
        elif Parser.tokens.actual.type == "PLUS" or Parser.tokens.actual.type == "MINUS" or Parser.tokens.actual.type == "NOT":
            ret = UnOp(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            ret.children.append(Parser.parseFactor())
        # "(", RELEX, ")"
        elif Parser.tokens.actual.type == "ABRE_PAR":
            Parser.tokens.selectNext()
            ret = Parser.parseRelationExpression()
            if Parser.tokens.actual.type != "FECHA_PAR":
                raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            Parser.tokens.selectNext()
        # IDENTIFIER
        elif Parser.tokens.actual.type == "IDEN":
            ret = Iden(Parser.tokens.actual.value)
            ret2 = FuncCall(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "ABRE_PAR":
                ret = ret2
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                else:
                    ret.children.append(Parser.parseRelationExpression())
                    while Parser.tokens.actual.type == "VIRGULA":
                        Parser.tokens.selectNext()
                        ret.children.append(Parser.parseRelationExpression())
                    if Parser.tokens.actual.type == "FECHA_PAR":
                        Parser.tokens.selectNext()
                    else:
                        raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # IDENTIFIER, "(", ARGS, ")"
        elif Parser.tokens.actual.type == "IDEF":
            ret = FuncCall(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "ABRE_PAR":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                else:
                    ret.children.append(Parser.parseRelationExpression())
                    while Parser.tokens.actual.type == "VIRGULA":
                        Parser.tokens.selectNext()
                        ret.children.append(Parser.parseRelationExpression())
                    if Parser.tokens.actual.type == "FECHA_PAR":
                        Parser.tokens.selectNext()
                    else:
                        raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # "zinput", "(", ")"
        elif Parser.tokens.actual.type == "INPUT":
            ret_t = Readline()
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "ABRE_PAR":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "FECHA_PAR":
                    Parser.tokens.selectNext()
                    ret = ret_t
                else:
                    raise SyntaxError("Line {}: Fechamento de parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
            else:
                raise SyntaxError("Line {}: Parenteses esperado. Recebeu {}: '{}'".format(Parser.tokens.line_n, Parser.tokens.actual.type, Parser.tokens.actual.value))
        # STRING
        elif Parser.tokens.actual.type == "STRING_VAL":
            ret = StringVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
        # "true" | "false"
        elif Parser.tokens.actual.type == "TRUE" or Parser.tokens.actual.type == "FALSE":
            ret = BoolVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
        # FLOAT
        elif Parser.tokens.actual.type == "FLOAT_VAL":
            ret = FloatVal(float(Parser.tokens.actual.value))
            Parser.tokens.selectNext()

        else:
            raise SyntaxError("Line {}".format(Parser.tokens.line_n))
        
        return ret


    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        ast = Parser.parseProgram()
        if Parser.tokens.actual.type != "EOF":
            raise SyntaxError("Line {}: Tratar isso {}".format(Parser.tokens.line_n, Parser.tokens.actual.value))
        return ast

class PrePro:
    @staticmethod
    def filter(string):
        ## https://stackoverflow.com/questions/2319019/using-regex-to-remove-comments-from-source-files
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
        #string = re.sub(re.compile("\\n",re.DOTALL), " ", string)
        return string

class Node:
    def __init__(self):
        self.value = None
        self.children = []
    
    def evaluate(self, st):
        raise NotImplementedError('subclasses must override evaluate()!')

class BinOp(Node):
    def __init__(self, value, c1):
        self.value = value
        self.children = [c1]

    def evaluate(self, st):
        c1 = self.children[0].evaluate(st)
        c2 = self.children[1].evaluate(st)
        c1_int = c1
        c2_int = c2
        if c1["val_type"] == "bool":
            if c1["value"] == True:
                c1_int = {"value": 1, "val_type": "int", "id_type": "iden"}
            else:
                c1_int = {"value": 0, "val_type": "int", "id_type": "iden"}
        if c2["val_type"] == "bool":
            if c2["value"] == True:
                c2_int = {"value": 1, "val_type": "int", "id_type": "iden"}
            else:
                c2_int = {"value": 0, "val_type": "int", "id_type": "iden"}
        c1_bool = c1
        c2_bool = c2
        if c1["val_type"] == "int":
            if c1["value"] == 0:
                c1_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                c1_bool = {"value": True, "val_type": "bool", "id_type": "iden"}
        if c2["val_type"] == "int":
            if c2["value"] == 0:
                c2_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                c2_bool = {"value": True, "val_type": "bool", "id_type": "iden"}

        # aritmeticos
        if self.value == "+":
            if c1["val_type"] == "string" and c2["val_type"] == "string":
                return {"value": c1["value"] + c2["value"], "val_type": "string", "id_type": "iden"}
            elif c1["val_type"] == "string" or c2["val_type"] == "string":
                return {"value": str(c1["value"]) + str(c2["value"]), "val_type": "string", "id_type": "iden"}
            return {"value": c1_int["value"] + c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "-":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '-' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] - c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "*":
            if (c1["val_type"] == "int" and c2["val_type"] == "string") or (c1["val_type"] == "string" and c2["val_type"] == "int"):
                return {"value": c1["value"] * c2["value"], "val_type": "string", "id_type": "iden"}
            elif (c1["val_type"] == "string" or c2["val_type"] == "string"):
                raise TypeError("Nao e possivel '*' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] * c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "/":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '/' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] / c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "//":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '/' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] // c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "%":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '/' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] % c2_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "**":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '/' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] ** c2_int["value"], "val_type": "int", "id_type": "iden"}

        # booleanos
        elif self.value == ">":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '>' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] > c2_int["value"], "val_type": "bool", "id_type": "iden"}
        elif self.value == "<":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel '<' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_int["value"] < c2_int["value"], "val_type": "bool", "id_type": "iden"}
        elif self.value == "==":
            #print(self.children[0].value, self.children[1].children[0].value, self.children[1].children[1].value)
            #print(c1, c2)
            if (c1["val_type"] == "int" and c2["val_type"] == "bool") or (c1["val_type"] == "bool" and c2["val_type"] == "int"):
                return {"value": c1_bool["value"] == c2_bool["value"], "val_type": "bool", "id_type": "iden"}
            return {"value": c1["value"] == c2["value"], "val_type": "bool", "id_type": "iden"}
        elif self.value == "and":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel 'and' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_bool["value"] and c2_bool["value"], "val_type": "bool", "id_type": "iden"}
        elif self.value == "or":
            if c1["val_type"] == "string" or c2["val_type"] == "string":
                raise TypeError("Nao e possivel 'or' entre '{}' e '{}'".format(c1["val_type"], c2["val_type"]))
            return {"value": c1_bool["value"] or c2_bool["value"], "val_type": "bool", "id_type": "iden"}
        # strings
        # elif self.value == ".":
        #     return ("string", str(c1["value"]) + str(c2["value"]))
        else:
            raise TypeError("BinOp Fail ({})".format(self.value))

class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, st):
        c1 = self.children[0].evaluate(st)
        c1_bool = c1
        if c1["val_type"] == "int":
            if c1["value"] == 0:
                c1_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                c1_bool = {"value": True, "val_type": "bool", "id_type": "iden"}
        c1_int = c1
        if c1["val_type"] == "bool":
            if c1["value"] == True:
                c1_int = {"value": 1, "val_type": "int", "id_type": "iden"}
            else:
                c1_int = {"value": 0, "val_type": "int", "id_type": "iden"}
        if c1["val_type"] == "string":
            raise TypeError("Nao e possivel '{}' com '{}'".format(self.value, c1["val_type"]))
        if self.value == "+":
            return c1_int
        elif self.value == "-":
            return {"value": -c1_int["value"], "val_type": "int", "id_type": "iden"}
        elif self.value == "!":
            return {"value": not c1_bool["value"], "val_type": "bool", "id_type": "iden"}
        else:
            raise TypeError("UnOp Fail ({})".format(self.value))

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return {"value": self.value, "val_type": "int", "id_type": "iden"}

class FloatVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return {"value": self.value, "val_type": "float", "id_type": "iden"}

class BoolVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return {"value": self.value, "val_type": "bool", "id_type": "iden"}

class StringVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return {"value": self.value, "val_type": "string", "id_type": "iden"}

class NoOp(Node):
    def evaluate(self, st):
        pass

class Comm(Node):
    def evaluate(self, st):
        for c in self.children:
            c.evaluate(st)
            if "return" in st.symbols.keys():
                break

class Assign(Node):
    def __init__(self, c1):
        self.children = [c1]

    def evaluate(self, st):
        val = self.children[1].evaluate(st)
        if val == None:
            print("Warning: '{}' is None".format(self.children[0].value))
        st.setSymbol(self.children[0].value, val)

class Iden(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return st.getSymbol(self.value)

class PRINT(Node):
    def evaluate(self, st):
        c1 = self.children[0].evaluate(st)
        if c1["val_type"] == "int":
            print(int(c1["value"]))
        else:
            print(c1["value"])
        
class Readline(Node):
    def evaluate(self, st):
        inp = input()
        ret = None
        try:
            inp = int(inp)
            ret = {"value": inp, "val_type": "int", "id_type": "iden"}
        except ValueError:
            if inp.lower() == "true":
                ret = {"value": True, "val_type": "bool", "id_type": "iden"}
            elif inp.lower() == "false":
                ret = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                ret = {"value": inp, "val_type": "string", "id_type": "iden"}
        return ret

class While(Node):    
    def evaluate(self, st):
        c1 = self.children[0].evaluate(st)
        c1_bool = c1
        if c1["val_type"] == "int":
            if c1["value"] == 0:
                c1_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                c1_bool = {"value": True, "val_type": "bool", "id_type": "iden"}
        elif c1["val_type"] == "string":
            raise TypeError("'While' nao pode receber 'str'")
        while c1_bool["value"]:
            self.children[1].evaluate(st)
            c1 = self.children[0].evaluate(st)
            c1_bool = c1
            if c1["val_type"] == "int":
                if c1["value"] == 0:
                    c1_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
                else:
                    c1_bool = {"value": True, "val_type": "bool", "id_type": "iden"}
            elif c1["val_type"] == "string":
                raise TypeError("'While' nao pode receber 'str'")

class If(Node):    
    def evaluate(self, st):
        c1 = self.children[0].evaluate(st)
        c1_bool = c1
        if c1["val_type"] == "int":
            if c1["value"] == 0:
                c1_bool = {"value": False, "val_type": "bool", "id_type": "iden"}
            else:
                c1_bool = {"value": True, "val_type": "bool", "id_type": "iden"}
        elif c1["val_type"] == "string":
            raise TypeError("'If' nao pode receber 'str'")
        if c1_bool["value"]:
            self.children[1].evaluate(st)
        else:
            if len(self.children) > 2:
                self.children[2].evaluate(st)

class FuncDef(Node):
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, st):
        st.setSymbol(self.value, {"value": self, "type": "func"})

class FuncCall(Node):
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, st):
        func = st.getSymbol(self.value)["value"]
        if len(func.children)-1 != len(self.children):
            raise TypeError("{}() recebe {} args, recebeu {}".format(self.value, len(func.children)-1, len(self.children)))
        stn = SymbolTable()
        for i in range(len(self.children)):
            stn.setSymbol(func.children[i].value, self.children[i].evaluate(st))
        func.children[-1].evaluate(stn)
        if "return" in stn.symbols.keys():
            return stn.getSymbol("return")
        return None

class Return(Node):
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, st):
        st.setSymbol(self.value, self.children[0].evaluate(st))

class SymbolTable():
    def __init__(self):
        self.symbols = defaultdict(dict)
    
    def setSymbol(self, symbol, value):
        self.symbols[symbol] = value
    
    def getSymbol(self, symbol):
        if symbol not in self.symbols.keys():
            raise NameError("{} nao definido".format(symbol))
        return self.symbols[symbol]

# class FuncTable():
#     funcs = defaultdict(Node)
    
#     @staticmethod
#     def setSymbol(symbol, node):
#         if symbol in FuncTable.funcs.keys():
#             raise NameError("{}() ja definido".format(symbol))
#         FuncTable.funcs[symbol] = node
    
#     @staticmethod
#     def getSymbol(symbol):
#         if symbol not in FuncTable.funcs.keys():
#             raise NameError("{}() nao definido".format(symbol))
#         return FuncTable.funcs[symbol]


def main():
    if len(sys.argv) <= 1:
        raise SyntaxError("Sem argumentos")
    
    if sys.argv[1][-5:] != ".zozo":
        raise TypeError("Arquivo tem que ser .zozo")

    with open(sys.argv[1]) as f:
        code = f.read()

    code = PrePro.filter(code)

    ast = Parser.run(code)

    st = SymbolTable()

    ast.evaluate(st)

if __name__ == "__main__":
    main()