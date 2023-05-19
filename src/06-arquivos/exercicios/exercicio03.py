""" Exercicio 03 """


def linha_para_dict(arquivo):
    dados = []
    for linha in arquivo:
        dados.append(linha.split(','))

    lista_chaves = ['prontuario', 'nome', 'email']
    dicionario = []

    for dado in dados:
        dicionario.append({lista_chaves[0]: dado[0], lista_chaves[1]: dado[1], lista_chaves[2]: dado[2].strip()})

    return dicionario


with open('src/06-arquivos/exercicios/exercicio01-dados.txt', 'r', encoding='UTF-8') as arquivo:
    for dicionario in linha_para_dict(arquivo):
        print(dicionario)
