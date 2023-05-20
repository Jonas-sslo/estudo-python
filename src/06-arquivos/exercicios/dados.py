""" Dados dos exercicios 01, 02 e 03 """

# exercicio 01
def carregar_dados_alunos(arq):
    dados = []
    for linha in arq.readlines():
        dados.append(linha.split(','))

    dicionario = []
    for dado in dados:
        dicionario.append(
            {'prontuario': dado[0], 'nome': dado[1], 'email': dado[2].strip()})

    return tuple(dicionario)

# exercicio 02
def carregar_dados_projetos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        dados.append(linha.split(','))

    dicionario = []
    for dado in dados:
        dicionario.append(
            {'Codigo': dado[0], 'Titulo': dado[1], 'Responsavel': dado[2].strip()})

    return tuple(dicionario)

# exercicio 03
def linha_para_dict(arquivo):
    dados = []
    for linha in arquivo:
        dados.append(linha.split(','))

    lista_chaves = ['prontuario', 'nome', 'email']
    dicionario = []

    for dado in dados:
        dicionario.append(
            {lista_chaves[0]: dado[0], lista_chaves[1]: dado[1], lista_chaves[2]: dado[2].strip()})

    return dicionario
