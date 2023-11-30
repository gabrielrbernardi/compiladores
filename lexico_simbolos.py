from lexico_transicao import Token

class Tabela_Simbolos:
    tabela_simbolos = {}
    indice = 0
    def init(self):
        self.tabela_simbolos = {}

    def insercao(self, tipo, lexema, valor=None, tipo_dado=""):
        #reconhecimento de palavras reservadas
        if lexema == "repeat":
            tipo = Token.REPEAT
        if lexema == "until":
            tipo = Token.UNTIL
        if lexema == "while":
            tipo = Token.WHILE
        if lexema == "if":
            tipo = Token.COND_IF
        if lexema == "else":
            tipo = Token.COND_ELSE
        if lexema == "then":
            tipo = Token.COND_THEN
        if lexema == "program":
            tipo = Token.PROGRAM
        if lexema == "begin":
            tipo = Token.BEGIN
        if lexema == "end":
            tipo = Token.END

        #OPERADORES RELACIONAIS - RELOP
        if lexema == "=":
            tipo = Token.RELOP_EQ
        if lexema == "!=":
            tipo = Token.RELOP_NE
        if lexema == ">=":
            tipo = Token.RELOP_GE
        if lexema == ">":
            tipo = Token.RELOP_GT
        if lexema == "<=":
            tipo = Token.RELOP_LE
        if lexema == "<":
            tipo = Token.RELOP_LT

        #OPERADORES ARITMETICOS
        if lexema == "+":
            tipo = Token.SUM
        if lexema == "-":
            tipo = Token.SUB
        if lexema == "*":
            tipo = Token.MUL
        if lexema == "/":
            tipo = Token.DIV
        if lexema == "^":
            tipo = Token.EXP

        #ATRIBUICAO
        if lexema == ":=":
            tipo = Token.ATRIBUICAO
        
        self.tabela_simbolos[lexema] = {
            "tipo": tipo,
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
