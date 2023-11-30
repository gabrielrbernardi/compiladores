class TransicoesAFD:
    def __init__(self, N_TRANSICAO, EH_FINAL=False, TRANSICOES=[], LOOKAHEAD=False, RETORNO=None):
        self.N_TRANSICAO = N_TRANSICAO
        self.EH_FINAL = EH_FINAL
        self.LOOKAHEAD = LOOKAHEAD
        self.RETORNO = RETORNO
        self.TRANSICOES = TRANSICOES
