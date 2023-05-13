""" Aula 01 - Introdução a funções """

# Função é um bloco que realiza uma tarefa específica
# Dividir o problema em pequenas partes
# Evitar duplicação de código 

# 1. Standard Library Function - built-in functions
# ex: print, len

print('Ola', 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)


# 2. User Defined Functions 
# Definidas pelo desenvolvedor(a)
# Fazerem parte da solução do problema

# declaracao
# nome: saudacoes
#parametros: nenhum
# retorno: nenhum
def saudacoes():
    print('Ola')


# Chamada
saudacoes()
saudacoes()
saudacoes()


# declaracao
# nome: saudacoes
#parametros: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Ola {nome}')

# Chamada
# valores, variáveis, expressoes => argumentos 
# 'Maria" é um argumento passado para o parâmetro nome
saudacoes('Maria')
saudacoes('Pedro')
nome = 'Carlos'
saudacoes(nome)

# declaracao
# nome: calcular_media
#parametros: nota1, nota2, nota3
# retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)


# Chamada
# argumentos literais
calcular_media(10.0, 3.0, 6.0)

n1 = 10.0
n2 = 3.0
n3 = 8.0
# argumentos variaveis
calcular_media(n1, n2, n3)


# declaracao
# nome: calcular_media
#parametros: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media = calcular_media(10.0, 8.4, 3.2)
print('valor da media', media)
# enviar no email
# salvar no banco de dados
# salvar no arquivo