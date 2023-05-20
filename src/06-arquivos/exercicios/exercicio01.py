""" Exercicio 01 """

from dados import carregar_dados_alunos

with open('src/06-arquivos/exercicios/exercicio01-dados.txt', 'r', encoding='UTF-8') as arq:
    print(carregar_dados_alunos(arq))
