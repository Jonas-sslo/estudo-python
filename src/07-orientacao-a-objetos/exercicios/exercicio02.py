""" Exercicio 02 """

from dados.dados2 import Projeto

projeto1 = Projeto('303030', 'Planetas', 'John Hawking')
projeto2 = Projeto('202020', 'Animais', 'Peter Darwin')
projeto3 = Projeto('303030', 'Livros', 'Bella King')

projetos = {projeto1, projeto2, projeto3}
print(projetos)
