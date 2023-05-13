""" Exercicio 04 """

codigo = input('Insira o seu código identificador (Ex: BR0001X): ')

erros = []

numeros = int(codigo[2:6])

VALIDACAO = len(codigo) == 7 and codigo[0:2] == 'BR' and codigo[-1] == 'X'

if len(codigo) != 7:
    erros.append('O código deve possuir 7 caracteres')
if codigo[0:2] != 'BR':
    erros.append("O código deve começar com 'BR'")
if codigo[-1] != 'X':
    erros.append("O código deve finalizar com a letra 'X'")
if 1 > numeros < 9999:
    erros.append('Os 4 digítos numéricos devem ser inseridos')


if VALIDACAO:
    if 1 <= numeros <= 9999:
        print('Código Válido')
else:
    print('Código Inválido')

print(erros)
