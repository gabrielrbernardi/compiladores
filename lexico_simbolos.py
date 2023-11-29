from lexico_transicao import Token

class Tabela_Simbolos:
    tabela_simbolos = {}
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

        
        self.tabela_simbolos[lexema] = {
            "tipo": token_tipo,
            "lexema": lexema,
            "valor": valor,
            "dado": tipo_dado,
        }

        return self.tabela_simbolos[lexema]

    def buscar(self, lexema):
        return self.tabela_simbolos.get(lexema, None)

    def listar_todos(self):
        return list(self.tabela_simbolos.values())
