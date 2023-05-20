""" Exercicio 02 """

from dados import carregar_dados_projetos

with open('src/06-arquivos/exercicios/exercicio02-projetos.txt', 'r', encoding='UTF-8') as arquivo:
    print(carregar_dados_projetos(arquivo))
