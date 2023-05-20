""" Exercicio 04 """

from dados.dados2 import Projeto
from dados.dados3 import Participacao


projeto1 = Projeto('303030', 'Planetas', 'John Hawking')
projeto2 = Projeto('202020', 'Animais', 'Peter Darwin')

participacao1 = Participacao('1', '20/03', '20/05', 'Carlos', 'Construir robô')
participacao2 = Participacao('2', '10/02', '10/05', 'Marina', 'Organizar relatórios')


projeto1.add_participacao(participacao1)
projeto2.add_participacao(participacao2)

print(projeto1)
for participacao in projeto1.participacoes:
    print(participacao)

print(projeto2)
for participacao in projeto2.participacoes:
    print(participacao)
