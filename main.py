import lexico_analisador
import lexico_simbolos

teste01 = "C:\\Users\\gabri\\Documentos\\UFU\\2023 - 2023-1\\CC\\Trabalho Final Final\\Codigo\\exemplos\\exemplo01.txt"
teste02 = "C:\\Users\\gabri\\Documentos\\UFU\\2023 - 2023-1\\CC\\Trabalho Final Final\\Codigo\\exemplos\\exemplo02.txt"
teste03 = "C:\\Users\\gabri\\Documentos\\UFU\\2023 - 2023-1\\CC\\Trabalho Final Final\\Codigo\\exemplos\\exemplo03.txt"
teste04 = "C:\\Users\\gabri\\Documentos\\UFU\\2023 - 2023-1\\CC\\Trabalho Final Final\\Codigo\\exemplos\\exemplo04.txt"

if __name__ == '__main__':
    print("1 - Caso de teste 01")
    print("2 - Caso de teste 02")
    print("3 - Caso de teste 03")
    print("4 - Caso de teste 04")
    resposta = int(input("Selecione o caso de teste: "))

    # resposta = 2

    if resposta == 1:
        test_file = teste01
    elif resposta == 2:
        test_file = teste02
    elif resposta == 3:
        test_file = teste03
    elif resposta == 4:
        test_file = teste04

    for _ in lexico_analisador.inicia_lexico(test_file, lexico_simbolos.Tabela_Simbolos()):
        pass
