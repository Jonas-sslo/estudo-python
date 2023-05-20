""" Exercicio 02 """

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.real(p)} é {moeda.real(moeda.metade(p))}')
print(f'O dobro de {moeda.real(p)} é {moeda.real(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.real(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.real(moeda.diminuir(p, 13))}')
