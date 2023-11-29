import lexico_analisador
import lexico_transicao
import lexico_simbolos

if __name__ == '__main__':
    tabela_simbolos = lexico_simbolos.Tabela_Simbolos() #inicia tabela de simbolos
    tabela_transicao_lexico = lexico_transicao.transicoes()

    for lexema in lexico_analisador.inicia_lexico("teste.txt", tabela_simbolos):
        # print(lexema)
        pass
