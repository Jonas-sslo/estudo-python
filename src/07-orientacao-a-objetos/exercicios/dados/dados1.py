""" Dados do Exercicio 01 """

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Prontuario' deve estar preenchido")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Nome' deve estar preenchido")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value == '' or value is None:
            raise ValueError("O campo 'Email' deve estar preenchido")
        self._email = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f'(Prontuario: {self.prontuario}, Nome: {self.nome}, Email: {self.email})'