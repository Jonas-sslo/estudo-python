""" Dados do Exercicio 03 """

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Código' deve estar preenchido")
        self._codigo = value
    
    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Data Inicio' deve estar preenchido")
        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Data Fim' deve estar preenchido")
        self._data_fim = value
    
    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Aluno' deve estar preenchido")
        self._aluno = value

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Projeto' deve estar preenchido")
        self._projeto = value
    
    def __repr__(self):
        return f'(Código: {self.codigo}, Data Inicio: {self.data_inicio}, Data Fim: {self.data_fim}, Aluno: {self.aluno}, Projeto: {self.projeto})'