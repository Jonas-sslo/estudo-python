""" Exercicio 1 """

numeros = []


for numero in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

menor = numeros[0]
maior = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print(f'O menor número é: {menor} e o maior é: {maior}')