""" Dados do Exercicio 02 """

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