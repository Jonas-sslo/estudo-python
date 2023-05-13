""" Exercicio 03 """

codigo = input('Insira o seu código identificador (Ex: BR0001X): ')

numeros = int(codigo[2:6])

VALIDACAO = len(codigo) == 7 and codigo[0:2] == 'BR' and codigo[-1] == 'X'

if VALIDACAO:
    if 1 <= numeros <= 9999:
        print('Código Válido')
else:
    print('Código Inválido')
