""" Exercicio 04 """


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Código' deve estar preenchido")
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Título' deve estar preenchido")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Reponsável' deve estar preenchido")
        self._responsavel = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f'(Código: {int(self.codigo)}, Título: {self.titulo}, Responsável: {self.responsavel})'


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