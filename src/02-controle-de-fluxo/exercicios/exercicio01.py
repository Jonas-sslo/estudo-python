""" Exercicio 01 """

numeros = []


for numero in range(3):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

numero1 = 0 <= numeros[0] <= 10
numero2 = 0 <= numeros[1] <= 10
numero3 = 0 <= numeros[2] <= 10


if numero1 and numero2 and numero3:
    media = (numeros[0] + numeros[1] + numeros[2]) / 3


print(media)
