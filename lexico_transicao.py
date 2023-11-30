from enum import Enum
import string

class Token(Enum):
    INICIO = 1
    ID = 2
    CONST_INT = 3
    NC = 4
    CONST_FLOAT = 5
    CHAR = 6
    DOIS_PONTOS = 7
    ATRIBUICAO = 8
    PONTO_E_VIRGULA = 9
    VIRGULA = 10
    RELOP_EQ = 11
    RELOP_NE = 12
    RELOP_GE = 13
    RELOP_GT = 14
    RELOP_LE = 15
    RELOP_LT = 16
    SUM = 17
    SUB = 18
    MUL = 19
    DIV = 20
    EXP = 21
    APAR = 22
    FPAR = 23
    FINAL_ARQUIVO = 24
    REPEAT = 25
    UNTIL = 26
    WHILE = 27
    COND_IF = 28
    COND_ELSE = 29
    COND_THEN = 30
    PROGRAM = 31
    BEGIN = 32
    END = 33

class TransicoesAFD:
    def __init__(
        self, N_TRANSICAO, EH_FINAL=False, TRANSICOES=[], LOOKAHEAD=False, RETORNO=None
    ):
        self.N_TRANSICAO = N_TRANSICAO
        self.EH_FINAL = EH_FINAL
        self.LOOKAHEAD = LOOKAHEAD
        self.RETORNO = RETORNO
        self.TRANSICOES = TRANSICOES

def transicoes():
    ascii_characters = "".join(chr(i) for i in range(32, 127)) #caracteres tabela ascii
    letras = string.ascii_lowercase + string.ascii_uppercase + "_" #alfabeto
    numeros = [str(i) for i in range(10)] #numeros de 0 a 9
    numeros = "".join(numeros)

    #Estrutura da tabela de transicao
    transicoes_existentes = [
        TransicoesAFD(N_TRANSICAO=0, TRANSICOES=[
            ("PROGRAM", 8),
            ("BEGIN", 14),
            ("END", 29),
            ("REPEAT", 46),
            ("UNTIL", 52),
            ("WHILE", 39),
            ("COND_IF", 17),
            ("COND_ELSE", 33),
            ("COND_THEN", 25),
            (" " + "\n", 1), 
            ("{", 88), 
            (letras, 101), 
            (numeros, 53), 
            ("'", 64), 
            (":", 77), 
            (";", 80), 
            (",", 92), 
            ("=", 74), 
            ("<", 70), 
            (">", 67), 
            ("!", 75), 
            ("^", 63), 
            ("+", 89), 
            ("-", 90), 
            ("*", 95), 
            ("/", 91), 
            ("(", 96), 
            (")", 97), 
            ("$", 100),            

        ],),

        #Tratamento de COMENTARIO
        TransicoesAFD(N_TRANSICAO=88,  EH_FINAL=False, TRANSICOES=[("}", 89), ("".join(char for char in ascii_characters if char not in ("}")), 88), ("\n", 88),],),

        #INICIO E FIM DE FUNCOES
        TransicoesAFD(N_TRANSICAO=8,   EH_FINAL=True,  RETORNO=Token.PROGRAM),
        TransicoesAFD(N_TRANSICAO=1,   EH_FINAL=True,  RETORNO=Token.INICIO),
        TransicoesAFD(N_TRANSICAO=89,  EH_FINAL=True,  RETORNO=Token.INICIO),
        TransicoesAFD(N_TRANSICAO=14,  EH_FINAL=True,  RETORNO=Token.BEGIN),
        TransicoesAFD(N_TRANSICAO=29,  EH_FINAL=True,  RETORNO=Token.END),

        #PALAVRAS RESERVADAS
        TransicoesAFD(N_TRANSICAO=46,  EH_FINAL=True,  RETORNO=Token.REPEAT),
        TransicoesAFD(N_TRANSICAO=52,  EH_FINAL=True,  RETORNO=Token.UNTIL),
        TransicoesAFD(N_TRANSICAO=39,  EH_FINAL=True,  RETORNO=Token.WHILE),
        TransicoesAFD(N_TRANSICAO=17,  EH_FINAL=True,  RETORNO=Token.COND_IF),
        TransicoesAFD(N_TRANSICAO=33,  EH_FINAL=True,  RETORNO=Token.COND_ELSE),
        TransicoesAFD(N_TRANSICAO=25,  EH_FINAL=True,  RETORNO=Token.COND_THEN),

        #TRANSICOES GERAIS (ID, CONSTANTES, ORTOGRAFIA)
        TransicoesAFD(N_TRANSICAO=101, EH_FINAL=False, TRANSICOES=[(letras + numeros, 101), ("\n", 5), ("".join(char for char in ascii_characters if char not in (letras + numeros)),5,),],),
        TransicoesAFD(N_TRANSICAO=5,   EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.ID),
        TransicoesAFD(N_TRANSICAO=53,  EH_FINAL=False, TRANSICOES=[(numeros, 53), (".", 54), ("".join(char for char in ascii_characters if char not in (numeros + ".")), 55, ), ("\n", 55),],),
        TransicoesAFD(N_TRANSICAO=55,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.CONST_INT),
        TransicoesAFD(N_TRANSICAO=54,  EH_FINAL=False, TRANSICOES=[(numeros, 157)]),
        TransicoesAFD(N_TRANSICAO=157, EH_FINAL=False, TRANSICOES=[("\n", 58), (numeros, 157), ("E", 158), ("".join(char for char in ascii_characters if char not in (numeros + "E")), 58, ),],),
        TransicoesAFD(N_TRANSICAO=158, EH_FINAL=False, TRANSICOES=[("-", 159), (numeros, 12)]),
        TransicoesAFD(N_TRANSICAO=159, EH_FINAL=False, TRANSICOES=[(numeros, 12)]),
        TransicoesAFD(N_TRANSICAO=12,  EH_FINAL=False, TRANSICOES=[(numeros, 12), ("".join(char for char in ascii_characters if char not in (numeros + ".")), 63, ), ("\n", 63),],),
        TransicoesAFD(N_TRANSICAO=63,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.NC),
        TransicoesAFD(N_TRANSICAO=58,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.CONST_FLOAT),
        TransicoesAFD(N_TRANSICAO=64,  EH_FINAL=False, TRANSICOES=[("\n", 64), ("'", 66), ("".join(char for char in ascii_characters if char not in "'"), 64),],),
        TransicoesAFD(N_TRANSICAO=66,  EH_FINAL=True,  RETORNO=Token.CHAR),
        TransicoesAFD(N_TRANSICAO=77,  EH_FINAL=False, TRANSICOES=[("\n", 78), ("=", 79), ("".join(char for char in ascii_characters if char not in "="), 78),],),
        TransicoesAFD(N_TRANSICAO=78,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.DOIS_PONTOS),
        
        #SIMBOLOS
        TransicoesAFD(N_TRANSICAO=79,  EH_FINAL=True,  RETORNO=Token.ATRIBUICAO),
        TransicoesAFD(N_TRANSICAO=80,  EH_FINAL=True,  RETORNO=Token.PONTO_E_VIRGULA),
        TransicoesAFD(N_TRANSICAO=92,  EH_FINAL=True,  RETORNO=Token.VIRGULA),

        #RELOP
        TransicoesAFD(N_TRANSICAO=74,  EH_FINAL=True,  RETORNO=Token.RELOP_EQ),
        TransicoesAFD(N_TRANSICAO=70,  EH_FINAL=False, TRANSICOES=[("\n", 71), ("=", 72), ("".join(char for char in ascii_characters if char not in ">="), 71),],),
        TransicoesAFD(N_TRANSICAO=72,  EH_FINAL=True,  RETORNO=Token.RELOP_LE),
        TransicoesAFD(N_TRANSICAO=71,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.RELOP_LT),
        TransicoesAFD(N_TRANSICAO=67,  EH_FINAL=False, TRANSICOES=[("\n", 68), ("=", 69), ("".join(char for char in ascii_characters if char not in "="), 68),],),
        TransicoesAFD(N_TRANSICAO=69,  EH_FINAL=True,  RETORNO=Token.RELOP_GE),
        TransicoesAFD(N_TRANSICAO=68,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.RELOP_GT),
        TransicoesAFD(N_TRANSICAO=75,  EH_FINAL=False, TRANSICOES=[("=", 76)]),
        TransicoesAFD(N_TRANSICAO=76,  EH_FINAL=True,  RETORNO=Token.RELOP_NE),

        #OPERADORES ARITMETICOS
        TransicoesAFD(N_TRANSICAO=63,  EH_FINAL=True,  RETORNO=Token.EXP),
        TransicoesAFD(N_TRANSICAO=89,  EH_FINAL=True,  RETORNO=Token.SUM),
        TransicoesAFD(N_TRANSICAO=90,  EH_FINAL=True,  RETORNO=Token.SUB),
        TransicoesAFD(N_TRANSICAO=95,  EH_FINAL=True,  RETORNO=Token.MUL),
        TransicoesAFD(N_TRANSICAO=91,  EH_FINAL=True,  RETORNO=Token.DIV),

        #PARENTESES
        TransicoesAFD(N_TRANSICAO=96,  EH_FINAL=True,  RETORNO=Token.APAR),
        TransicoesAFD(N_TRANSICAO=97,  EH_FINAL=True,  RETORNO=Token.FPAR),

        #FIM DO ARQUIVO
        TransicoesAFD(N_TRANSICAO=100, EH_FINAL=True,  RETORNO=Token.FINAL_ARQUIVO),
    ]

    return verifica_tabela_simbolos(transicoes_existentes)


def verifica_tabela_simbolos(tabela):
    table = {}

    for elem in tabela:
        table[elem.N_TRANSICAO] = elem

    for k, v in table.items():
        for trans in v.TRANSICOES:
            if trans[1] not in table:
                raise Exception(f"TRANSIÇÃO INVALIDA EM [{v}] NA TRANSICAO {trans}")

    return table
