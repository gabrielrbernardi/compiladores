import lexico_transicao
class Tabela_Simbolos:
    tabela_simbolos = {}
    indice = 0
    def init(self):
        self.tabela_simbolos = {}

    def insercao(self, tipo, lexema, valor=None, posicao = (0,0)):
        #reconhecimento de palavras reservadas
        if lexema == "repeat":
            tipo = lexico_transicao.Token.REPEAT
        if lexema == "until":
            tipo = lexico_transicao.Token.UNTIL
        if lexema == "while":
            tipo = lexico_transicao.Token.WHILE
        if lexema == "if":
            tipo = lexico_transicao.Token.COND_IF
        if lexema == "else":
            tipo = lexico_transicao.Token.COND_ELSE
        if lexema == "then":
            tipo = lexico_transicao.Token.COND_THEN
        if lexema == "program":
            tipo = lexico_transicao.Token.PROGRAM
        if lexema == "begin":
            tipo = lexico_transicao.Token.BEGIN
        if lexema == "end":
            tipo = lexico_transicao.Token.END

        #OPERADORES RELACIONAIS - RELOP
        if lexema == "=":
            tipo = lexico_transicao.Token.RELOP_EQ
        if lexema == "!=":
            tipo = lexico_transicao.Token.RELOP_NE
        if lexema == ">=":
            tipo = lexico_transicao.Token.RELOP_GE
        if lexema == ">":
            tipo = lexico_transicao.Token.RELOP_GT
        if lexema == "<=":
            tipo = lexico_transicao.Token.RELOP_LE
        if lexema == "<":
            tipo = lexico_transicao.Token.RELOP_LT

        #OPERADORES ARITMETICOS
        if lexema == "+":
            tipo = lexico_transicao.Token.SUM
        if lexema == "-":
            tipo = lexico_transicao.Token.SUB
        if lexema == "*":
            tipo = lexico_transicao.Token.MUL
        if lexema == "/":
            tipo = lexico_transicao.Token.DIV
        if lexema == "^":
            tipo = lexico_transicao.Token.EXP

        #ATRIBUICAO
        if lexema == ":=":
            tipo = lexico_transicao.Token.ATRIBUICAO
        
        self.tabela_simbolos[lexema] = {
            "indice": self.indice,
            "lexema": lexema,
            "posicao": posicao,
            "tipo": tipo,
            "valor": valor
        }
        self.indice += 1

        return self.tabela_simbolos[lexema]

    def buscar(self, lexema):
        return self.tabela_simbolos.get(lexema, None)

    def listar_todos(self):
        return list(self.tabela_simbolos.values())
