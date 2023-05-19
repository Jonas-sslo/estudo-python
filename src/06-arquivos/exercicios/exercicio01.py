""" Exercicio 01 """


def carregar_dados_alunos(arq):
    dados = []
    for linha in arq.readlines():
        dados.append(linha.split(','))

    dicionario = []
    for dado in dados:
        dicionario.append({'prontuario': dado[0], 'nome': dado[1], 'email': dado[2].strip()})

    return tuple(dicionario)


with open('src/06-arquivos/exercicios/exercicio01-dados.txt', 'r', encoding='UTF-8') as arq:
    print(carregar_dados_alunos(arq))
