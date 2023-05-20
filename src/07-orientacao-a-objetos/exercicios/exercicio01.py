""" Exercicio 01 """

from dados.dados1 import Aluno

aluno1 = Aluno('SP0101', 'João da Silva', 'joao@email.com')
aluno2 = Aluno('SP0102', 'Maria da Silva', 'maria@email.com')
aluno3 = Aluno('SP0101', 'Pedro Santos', 'pedro@email.com')

alunos = {aluno1, aluno2, aluno3}
print(alunos)
