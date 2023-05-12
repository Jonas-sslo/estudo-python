""" Aula 03 - Tipos de Dados - Sets"""

# sets (conjunto)
# não ordenados
# mutáveis
# não indexáveis
# não aceitam elementos duplicados

# criar um set
numeros = {1, 12, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(50 in numeros)

# adicionar itens no set
print(numeros)
numeros.add(8)
print(numeros)

# adicionar elementos de um set em outro
print('----')
numeros2 = {1, 5, 4, 4, 3, 11, 9}
print(numeros)
numeros.update(numeros2)
print(numeros2)
print(numeros, type(numeros))