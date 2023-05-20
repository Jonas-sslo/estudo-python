""" Exercicio 03 """

from dados import linha_para_dict

with open('src/06-arquivos/exercicios/exercicio01-dados.txt', 'r', encoding='UTF-8') as arquivo:
    for dicionario in linha_para_dict(arquivo):
        print(dicionario)
