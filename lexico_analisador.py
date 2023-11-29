import lexico_transicao
import lexico_transicao
from lexico_simbolos import Tabela_Simbolos

# global quantidade_Abre_Parenteses, quantidade_Fecha_Parenteses
quantidade_Abre_Parenteses = 0
quantidade_Fecha_Parenteses = 0
quantidade_Abre_Chaves = 0
quantidade_Fecha_Chaves = 0
tem_transicao = False

def leitura_arquivo_entrada(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        qtd_linhas = 0
        for x in f:
            qtd_linhas += 1
            qtd_colunas = 0
            for c in x:
                qtd_colunas += 1
                yield {"cabeca": c, "linha_caractere": qtd_linhas, "coluna_caractere": qtd_colunas}

def analisador_lexico(nome_arquivo):
    tabela = lexico_transicao.transicoes()
    flag = 0
    lexema = ""
    leitor = leitura_arquivo_entrada(nome_arquivo)

    inicio_lexema = (0, 0)
    tem_transicao = False
    for char in leitor:
        if len(lexema) == 0:
            inicio_lexema = (char["linha_caractere"], char["coluna_caractere"])
            
        if tabela[flag].EH_FINAL:
            if verifica_valores(lexema) == -1:
                return
            if tabela[flag].LOOKAHEAD:
                yield (lexema[:-1], tabela[flag].RETORNO, inicio_lexema)
                lexema = ""
                flag = 0
                inicio_lexema = (char["linha_caractere"], char["coluna_caractere"])
            else:
                yield (lexema, tabela[flag].RETORNO, inicio_lexema)
                lexema = ""
                flag = 0
                inicio_lexema = (char["linha_caractere"], char["coluna_caractere"])

        if not tabela[flag].EH_FINAL:
            lexema, flag, tem_transicao = troca_estado(
                tabela, char, flag, lexema
            )

        if not tem_transicao and not (tabela[flag].EH_FINAL):
            flag = -1

        if flag == -1:
            print(
                f'Erro no char {char} no lexema = "{lexema}" len = {len(lexema)}')
            break

        if tabela[flag].EH_FINAL:
            if verifica_valores(lexema) == -1:
                return
            if tabela[flag].LOOKAHEAD:
                yield (lexema[:-1], tabela[flag].RETORNO, inicio_lexema)
                lexema = ""
                flag = 0
                inicio_lexema = (char["linha_caractere"], char["coluna_caractere"])
                lexema, flag, tem_transicao = troca_estado(
                    tabela, char, flag, lexema
                )
            else:
                yield (lexema, tabela[flag].RETORNO, inicio_lexema)
                lexema = ""
                flag = 0
                inicio_lexema = (char["linha_caractere"], char["coluna_caractere"])

def troca_estado(tabela, char, estado, lexema):
    lexema = lexema + char["cabeca"]
    # print(f'TransicoesAFD = {estado}, char = {char}, lexema = "{lexema}", len = {len(lexema)}')

    tem_transicao = False

    for trans in tabela[estado].TRANSICOES:
        if char["cabeca"] in trans[0]:
            estado = trans[1]
            tem_transicao = True
    return lexema, estado, tem_transicao

def inicia_lexico(nome_arquivo, tabela_simbolo):
    for lexema in analisador_lexico(nome_arquivo):
        if not lexema[1] == lexico_transicao.Token.INICIO:
            resultado = insere_tabela(lexema=lexema, tabela=tabela_simbolo)
            if resultado:
                yield resultado["tipo"], resultado["tipo"], lexema[2]
            else:
                yield lexema

def insere_tabela(lexema, tabela):
    tipo = lexema[1]
    lex = lexema[0]

    # print(lexema, tipo, lex)

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
        retorno_insercao = tabela.inserir(token_tipo = tipo, lexema = lex)
        # return tabela.inserir(token_tipo = tipo, lexema = lex)
        # return
    
    elif lex in operadores:
        retorno_insercao = tabela.inserir(token_tipo = tipo, lexema = lex)
        # return
    
    elif tipo in [lexico_transicao.Token.ID]:
        retorno_insercao = tabela.inserir(token_tipo=tipo, lexema=lex, tipo_dado="ID", valor=None)
        # print(retorno_insercao)
        # print("ID Adicionado", end="")

    elif tipo in [lexico_transicao.Token.CONST_INT, lexico_transicao.Token.CONST_FLOAT, lexico_transicao.Token.NC, lexico_transicao.Token.CHAR]:
        retorno_insercao = tabela.inserir(token_tipo=tipo, lexema=lex, valor=None, tipo_dado=None)
        # print(retorno_insercao)
        # print("Constante Adicionada", end="")

    try:
        if (retorno_insercao):
            # print("\n")
            print("Tipo", retorno_insercao["tipo"])
            print("Lexema", retorno_insercao["lexema"])
            if(retorno_insercao["dado"]):
                print("Tipo de dado", retorno_insercao["dado"])
            print("Indice", retorno_insercao["indice"])
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