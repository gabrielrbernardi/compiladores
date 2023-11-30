import enum
import lexico_TransicoesAFD as TAFD
import string

class Token(enum.Enum):
    INICIO = 1
    PROGRAM = 2
    BEGIN = 3
    END = 4
    REPEAT = 5
    UNTIL = 6
    WHILE = 7

    #CONDICIONAIS
    COND_IF = 8
    COND_ELSE = 9
    COND_THEN = 10
    
    ATRIBUICAO = 11
    APAR = 12

    #CONSTANTES
    CONST_CHAR = 13
    CONST_INT = 14
    CONST_FLOAT = 15
    
    DIV = 16
    DOIS_PONTOS = 17
    EXP = 18
    FPAR = 19
    FINAL_ARQUIVO = 20
    ID = 21
    MUL = 22
    NC = 23 #NOTACAO CIENTIFICA
    PONTO_E_VIRGULA = 24
    
    #RELOP
    RELOP_EQ = 25
    RELOP_NE = 26
    RELOP_GE = 27
    RELOP_GT = 28
    RELOP_LE = 29
    RELOP_LT = 30
    SUM = 31
    SUB = 32
    VIRGULA = 33

def transicoes():
    ascii_characters = "".join(chr(i) for i in range(32, 127)) #caracteres tabela ascii
    letras = string.ascii_lowercase + string.ascii_uppercase + "_" #alfabeto
    numeros = [str(i) for i in range(10)] #numeros de 0 a 9
    numeros = "".join(numeros)

    #Estrutura da tabela de transicao
    transicoes_existentes = [
        TAFD.TransicoesAFD(N_TRANSICAO=0, TRANSICOES=[
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
        TAFD.TransicoesAFD(N_TRANSICAO=88,  EH_FINAL=False, TRANSICOES=[("}", 89), ("".join(char for char in ascii_characters if char not in ("}")), 88), ("\n", 88),],),

        #INICIO E FIM DE FUNCOES
        TAFD.TransicoesAFD(N_TRANSICAO=8,   EH_FINAL=True,  RETORNO=Token.PROGRAM),
        TAFD.TransicoesAFD(N_TRANSICAO=1,   EH_FINAL=True,  RETORNO=Token.INICIO),
        TAFD.TransicoesAFD(N_TRANSICAO=89,  EH_FINAL=True,  RETORNO=Token.INICIO),
        TAFD.TransicoesAFD(N_TRANSICAO=14,  EH_FINAL=True,  RETORNO=Token.BEGIN),
        TAFD.TransicoesAFD(N_TRANSICAO=29,  EH_FINAL=True,  RETORNO=Token.END),

        #PALAVRAS RESERVADAS
        TAFD.TransicoesAFD(N_TRANSICAO=46,  EH_FINAL=True,  RETORNO=Token.REPEAT),
        TAFD.TransicoesAFD(N_TRANSICAO=52,  EH_FINAL=True,  RETORNO=Token.UNTIL),
        TAFD.TransicoesAFD(N_TRANSICAO=39,  EH_FINAL=True,  RETORNO=Token.WHILE),
        TAFD.TransicoesAFD(N_TRANSICAO=17,  EH_FINAL=True,  RETORNO=Token.COND_IF),
        TAFD.TransicoesAFD(N_TRANSICAO=33,  EH_FINAL=True,  RETORNO=Token.COND_ELSE),
        TAFD.TransicoesAFD(N_TRANSICAO=25,  EH_FINAL=True,  RETORNO=Token.COND_THEN),

        #TRANSICOES GERAIS (ID, CONSTANTES, ORTOGRAFIA)
        TAFD.TransicoesAFD(N_TRANSICAO=101, EH_FINAL=False, TRANSICOES=[(letras + numeros, 101), ("\n", 5), ("".join(char for char in ascii_characters if char not in (letras + numeros)),5,),],),
        TAFD.TransicoesAFD(N_TRANSICAO=5,   EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.ID),
        TAFD.TransicoesAFD(N_TRANSICAO=53,  EH_FINAL=False, TRANSICOES=[(numeros, 53), (".", 54), ("".join(char for char in ascii_characters if char not in (numeros + ".")), 55, ), ("\n", 55),],),
        TAFD.TransicoesAFD(N_TRANSICAO=55,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.CONST_INT),
        TAFD.TransicoesAFD(N_TRANSICAO=54,  EH_FINAL=False, TRANSICOES=[(numeros, 157)]),
        TAFD.TransicoesAFD(N_TRANSICAO=157, EH_FINAL=False, TRANSICOES=[("\n", 58), (numeros, 157), ("E", 158), ("".join(char for char in ascii_characters if char not in (numeros + "E")), 58, ),],),
        TAFD.TransicoesAFD(N_TRANSICAO=158, EH_FINAL=False, TRANSICOES=[("-", 159), (numeros, 12)]),
        TAFD.TransicoesAFD(N_TRANSICAO=159, EH_FINAL=False, TRANSICOES=[(numeros, 12)]),
        TAFD.TransicoesAFD(N_TRANSICAO=12,  EH_FINAL=False, TRANSICOES=[(numeros, 12), ("".join(char for char in ascii_characters if char not in (numeros + ".")), 63, ), ("\n", 63),],),
        TAFD.TransicoesAFD(N_TRANSICAO=63,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.NC),
        TAFD.TransicoesAFD(N_TRANSICAO=58,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.CONST_FLOAT),
        TAFD.TransicoesAFD(N_TRANSICAO=64,  EH_FINAL=False, TRANSICOES=[("\n", 64), ("'", 66), ("".join(char for char in ascii_characters if char not in "'"), 64),],),
        TAFD.TransicoesAFD(N_TRANSICAO=66,  EH_FINAL=True,  RETORNO=Token.CONST_CHAR),
        TAFD.TransicoesAFD(N_TRANSICAO=77,  EH_FINAL=False, TRANSICOES=[("\n", 78), ("=", 79), ("".join(char for char in ascii_characters if char not in "="), 78),],),
        TAFD.TransicoesAFD(N_TRANSICAO=78,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.DOIS_PONTOS),
        
        #SIMBOLOS
        TAFD.TransicoesAFD(N_TRANSICAO=79,  EH_FINAL=True,  RETORNO=Token.ATRIBUICAO),
        TAFD.TransicoesAFD(N_TRANSICAO=80,  EH_FINAL=True,  RETORNO=Token.PONTO_E_VIRGULA),
        TAFD.TransicoesAFD(N_TRANSICAO=92,  EH_FINAL=True,  RETORNO=Token.VIRGULA),

        #RELOP
        TAFD.TransicoesAFD(N_TRANSICAO=74,  EH_FINAL=True,  RETORNO=Token.RELOP_EQ),
        TAFD.TransicoesAFD(N_TRANSICAO=70,  EH_FINAL=False, TRANSICOES=[("\n", 71), ("=", 72), ("".join(char for char in ascii_characters if char not in ">="), 71),],),
        TAFD.TransicoesAFD(N_TRANSICAO=72,  EH_FINAL=True,  RETORNO=Token.RELOP_LE),
        TAFD.TransicoesAFD(N_TRANSICAO=71,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.RELOP_LT),
        TAFD.TransicoesAFD(N_TRANSICAO=67,  EH_FINAL=False, TRANSICOES=[("\n", 68), ("=", 69), ("".join(char for char in ascii_characters if char not in "="), 68),],),
        TAFD.TransicoesAFD(N_TRANSICAO=69,  EH_FINAL=True,  RETORNO=Token.RELOP_GE),
        TAFD.TransicoesAFD(N_TRANSICAO=68,  EH_FINAL=True,  LOOKAHEAD=True, RETORNO=Token.RELOP_GT),
        TAFD.TransicoesAFD(N_TRANSICAO=75,  EH_FINAL=False, TRANSICOES=[("=", 76)]),
        TAFD.TransicoesAFD(N_TRANSICAO=76,  EH_FINAL=True,  RETORNO=Token.RELOP_NE),

        #OPERADORES ARITMETICOS
        TAFD.TransicoesAFD(N_TRANSICAO=63,  EH_FINAL=True,  RETORNO=Token.EXP),
        TAFD.TransicoesAFD(N_TRANSICAO=89,  EH_FINAL=True,  RETORNO=Token.SUM),
        TAFD.TransicoesAFD(N_TRANSICAO=90,  EH_FINAL=True,  RETORNO=Token.SUB),
        TAFD.TransicoesAFD(N_TRANSICAO=95,  EH_FINAL=True,  RETORNO=Token.MUL),
        TAFD.TransicoesAFD(N_TRANSICAO=91,  EH_FINAL=True,  RETORNO=Token.DIV),

        #PARENTESES
        TAFD.TransicoesAFD(N_TRANSICAO=96,  EH_FINAL=True,  RETORNO=Token.APAR),
        TAFD.TransicoesAFD(N_TRANSICAO=97,  EH_FINAL=True,  RETORNO=Token.FPAR),

        #FIM DO ARQUIVO
        TAFD.TransicoesAFD(N_TRANSICAO=100, EH_FINAL=True,  RETORNO=Token.FINAL_ARQUIVO),
    ]

    return verifica_transicoes(transicoes_existentes)


def verifica_transicoes(tabela):
    table = {}

    for elem in tabela:
        table[elem.N_TRANSICAO] = elem

    for _, x in table.items():
        for transicao in x.TRANSICOES:
            if transicao[1] not in table:
                print("Transicao Invalida!")
                print("Indice: " + str(x))
                print("Transicao: " + str(transicao))
                exit(-1)

    return table
