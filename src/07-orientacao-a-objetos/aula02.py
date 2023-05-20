""" Aula 02 - Atributos de classe e instância """


# Classe Pessoa possui
# atributos de instancia: nome e email
# atributos de classe: especie
class Pessoa:
    especie = 'Humano' # atributo de classe

    def __init__(self, nome, email): # atributo de instancia
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Santos', 'pedro@email.com')


# alterar um atributo de classe na instancia (objeto)
# altera somento para aquela instancia 
pessoa1.especie = 'Alienigena'

# alterando um atributo de classe na classe 
# altera todos os objetos na classe tambem
Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)
