import lexico_transicao
import lexico_transicao
from lexico_simbolos import Tabela_Simbolos

# global quantidade_Abre_Parenteses, quantidade_Fecha_Parenteses
quantidade_Abre_Parenteses = 0
quantidade_Fecha_Parenteses = 0
quantidade_Abre_Chaves = 0
quantidade_Fecha_Chaves = 0
tem_transicao = False

def leitura_arquivo_entrada(arquivo_entrada):
    f = open(arquivo_entrada, "r") #abertura do arquivo de entrada
    
    qtd_linhas = 0
    while True:
        linha = f.readline() #leitura de cada linha da entrada
        if not linha: #se nao existir conteudo na linha, finaliza a leitura
            break
        qtd_linhas += 1
        qtd_colunas = 0
        for c in linha: #leitura de cada caractere
            qtd_colunas += 1
            yield {
                "cabeca": c, 
                "linha_caractere": qtd_linhas, 
                "coluna_caractere": qtd_colunas
            }

def analisador_lexico(arquivo_entrada):
    tabela_transicao = lexico_transicao.transicoes()
    flag = 0
    lexema = ""
    objeto_entrada = leitura_arquivo_entrada(arquivo_entrada)

    inicio_posicao_lexema = (0, 0)
    tem_transicao = False
    for c in objeto_entrada: #percorre cada caractere lido
        if len(lexema) == 0:
            inicio_posicao_lexema = (c["linha_caractere"], c["coluna_caractere"])
        
        if tabela_transicao[flag].EH_FINAL:
            if verifica_valores(lexema) == -1:
                return
            if tabela_transicao[flag].LOOKAHEAD:
                yield (lexema[:-1], tabela_transicao[flag].RETORNO, inicio_posicao_lexema)
                lexema = ""
                flag = 0
                inicio_posicao_lexema = (c["linha_caractere"], c["coluna_caractere"])
            else:
                yield (lexema, tabela_transicao[flag].RETORNO, inicio_posicao_lexema)
                lexema = ""
                flag = 0
                inicio_posicao_lexema = (c["linha_caractere"], c["coluna_caractere"])

        if not tabela_transicao[flag].EH_FINAL:
            lexema, flag, tem_transicao = troca_estado(tabela_transicao, c, flag, lexema)

        if not tem_transicao and not (tabela_transicao[flag].EH_FINAL):
            print("ERRO!\nLexema: " + str(lexema))
            print("Posicao: " + "Linha: " + str(c["linha_caractere"]) + " Coluna: " + str(c["coluna_caractere"]))
            break

def troca_estado(tabela, caractere, flag, lexema):
    lexema += caractere["cabeca"]

    tem_transicao = False

    for transicao in tabela[flag].TRANSICOES:
        if caractere["cabeca"] in transicao[0]:
            tem_transicao = True
            flag = transicao[1]
    
    return lexema, flag, tem_transicao

def inicia_lexico(arquivo_entrada, tabela):
    lexico = analisador_lexico(arquivo_entrada)
    
    for lexema in lexico:
        if not lexema[1] == lexico_transicao.Token.INICIO:
            resultado = insere_tabela(lexema, tabela)
            
            if resultado:
                yield resultado["tipo"], resultado["tipo"], lexema[2]
            else:
                yield lexema

def insere_tabela(lexema, tabela):
    tipo = lexema[1]
    lex = lexema[0]

    #definicao de palavras reservadas
    reservado = [
        "repeat",
        "until",
        "while",
        "if",
        "else",
        "then",
        "program",
        "begin",
        "end"
    ]

    #definicao dos operadores
    operadores = [
        ":=",
        "=",
        "!=",
        ">=",
        ">",
        "<=",
        "<",
        "+",
        "-",
        "*",
        "/",
        "^"
    ]

    if lex in reservado:
        retorno_insercao = tabela.insercao(tipo = tipo, lexema = lex)
        # return tabela.insercao(tipo = tipo, lexema = lex)
        # return
    
    elif lex in operadores:
        retorno_insercao = tabela.insercao(tipo = tipo, lexema = lex)
        # return
    
    elif tipo in [lexico_transicao.Token.ID]:
        retorno_insercao = tabela.insercao(tipo=tipo, lexema=lex, tipo_dado="ID", valor=None)
        # print(retorno_insercao)
        # print("ID Adicionado", end="")

    elif tipo in [lexico_transicao.Token.CONST_INT, lexico_transicao.Token.CONST_FLOAT, lexico_transicao.Token.NC, lexico_transicao.Token.CHAR]:
        retorno_insercao = tabela.insercao(tipo=tipo, lexema=lex, valor=None, tipo_dado=None)
        # print(retorno_insercao)
        # print("Constante Adicionada", end="")

    try:
        if (retorno_insercao):
            # print("\n")
            print("Tipo:", retorno_insercao["tipo"])
            print("Lexema:", retorno_insercao["lexema"])
            # if(retorno_insercao["dado"]):
            #     print("Tipo de dado:", retorno_insercao["dado"])
            print("Indice:", retorno_insercao["indice"])
            print("\n")
    except:
        pass

def verifica_valores(lexema):
    #contagem de caracteres que tem que ser fechados
    
    if lexema == "(":
        global quantidade_Abre_Parenteses
        quantidade_Abre_Parenteses += 1
        # print("abre", quantidade_Abre_Parenteses)
    
    if lexema == "{":
        global quantidade_Abre_Chaves
        quantidade_Abre_Chaves += 1

    if lexema == ")":
        global quantidade_Fecha_Parenteses
        quantidade_Fecha_Parenteses += 1
        # print("fecha", quantidade_Fecha_Parenteses)
    
    if lexema == "}":
        global quantidade_Fecha_Chaves
        quantidade_Fecha_Chaves += 1

    if lexema == '$':
        if quantidade_Abre_Parenteses == quantidade_Fecha_Parenteses and quantidade_Abre_Chaves == quantidade_Fecha_Chaves:
            print("Final de Arquivo. Leitura encerrada. Tudo OK!")
            # print("ta ok")
            pass
        else:
            print("ERRO! A utilizacao dos parenteses ou chaves nao esta correta")
        return -1