from lexico_transicao import Token

class Tabela_Simbolos:
    tabela_simbolos = {}
    indice = 0
    def init(self):
        self.tabela_simbolos = {}

    def inserir(self, token_tipo, lexema, valor=None, tipo_dado=""):
        #reconhecimento de palavras reservadas
        if lexema == "repeat":
            token_tipo = Token.REPEAT
        if lexema == "until":
            token_tipo = Token.UNTIL
        if lexema == "while":
            token_tipo = Token.WHILE
        if lexema == "if":
            token_tipo = Token.COND_IF
        if lexema == "else":
            token_tipo = Token.COND_ELSE
        if lexema == "then":
            token_tipo = Token.COND_THEN
        if lexema == "program":
            token_tipo = Token.PROGRAM
        if lexema == "begin":
            token_tipo = Token.BEGIN
        if lexema == "end":
            token_tipo = Token.END

        #OPERADORES RELACIONAIS - RELOP
        if lexema == "=":
            token_tipo = Token.RELOP_EQ
        if lexema == "!=":
            token_tipo = Token.RELOP_NE
        if lexema == ">=":
            token_tipo = Token.RELOP_GE
        if lexema == ">":
            token_tipo = Token.RELOP_GT
        if lexema == "<=":
            token_tipo = Token.RELOP_LE
        if lexema == "<":
            token_tipo = Token.RELOP_LT

        #OPERADORES ARITMETICOS
        if lexema == "+":
            token_tipo = Token.SUM
        if lexema == "-":
            token_tipo = Token.SUB
        if lexema == "*":
            token_tipo = Token.MUL
        if lexema == "/":
            token_tipo = Token.DIV
        if lexema == "^":
            token_tipo = Token.EXP

        #ATRIBUICAO
        if lexema == ":=":
            token_tipo = Token.ATRIBUICAO
        
        self.tabela_simbolos[lexema] = {
            "tipo": token_tipo,
            "lexema": lexema,
            "valor": valor,
            "dado": tipo_dado,
            "indice": self.indice
        }
        self.indice += 1

        return self.tabela_simbolos[lexema]

    def buscar(self, lexema):
        return self.tabela_simbolos.get(lexema, None)

    def listar_todos(self):
        return list(self.tabela_simbolos.values())
