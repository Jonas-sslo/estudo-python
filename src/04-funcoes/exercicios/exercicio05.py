""" Exercicio 05 """

def calculo_imc(usuario):
    """ retorna o imc de um indivíduo com base na sua altura e peso """
    imc = peso_usuario / (altura_usuario * altura_usuario)
    return imc

def obter_classificacao(imc):
    """ retorna a classificação com base no imc """
    if imc < 18.5:
        return('Baixo peso')
    elif 18.5 <= imc <= 24.9:
        return('Peso Normal')
    elif 25 <= imc <= 29.9:
        return('Excesso de peso')
    elif 30 <= imc <= 34.9:
        return('Obesidade de Classe 1')
    elif 35 <= imc <= 39.9:
        return('Obesidade de Classe 2')
    else:
        return('Obesidade de Classe 3')

def situacao_usuario(imc):
    """ retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no imc"""
    if imc < 18.5:
        return('Ganhar peso')
    elif 18.5 <= imc <= 24.9:
        return('Peso normal')
    else:
        return('Perder peso')

peso_usuario = float(input('Insira o seu peso (kg): '))
altura_usuario = float(input('Insira a sua altura (m): '))

usuario = {
    'peso': peso_usuario,
    'altura': altura_usuario
}

imc = calculo_imc(usuario)
classificacao = obter_classificacao(imc)
situacao = situacao_usuario(imc)

print('IMC:',imc)
print('Classificação:', classificacao)
print('Situação:', situacao)

