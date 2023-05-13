""" Exercicio 04 """

def somar(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

resultado = somar(10, 5, 7, 9, 6)
print(resultado)