""" Exercicio 02 """


def carregar_dados_projetos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        dados.append(linha.split(','))

    dicionario = []
    for dado in dados:
        dicionario.append({'Codigo': dado[0], 'Titulo': dado[1], 'Responsavel': dado[2].strip()})

    return tuple(dicionario)


with open('src/06-arquivos/exercicios/exercicio02-projetos.txt', 'r', encoding='UTF-8') as arquivo:
    print(carregar_dados_projetos(arquivo))
