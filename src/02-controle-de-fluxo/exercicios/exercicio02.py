""" Exercicio 02 """

notas = input('Insira as notas no formato (n1, n2, n3, ..., nm): ')
notas = notas.split(sep = ',')

soma = 0
for nota in notas:
    soma += float(nota)

media = soma / len(notas)

if media >= 6.0:
    print('Aprovado')
elif 4.0 <= media < 6.0: 
    print('Recuperação')
else:
    print('Reprovado') 


