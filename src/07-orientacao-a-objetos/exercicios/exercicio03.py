""" Exercicio 03 """

from dados.dados3 import Participacao

participacao1 = Participacao('1', '20/03', '20/05', 'Carlos', 'Construir robô')
participacao2 = Participacao('2', '10/02', '10/05', 'Marina', 'Organizar relatórios')

participacoes = {participacao1, participacao2}
print(participacoes)
