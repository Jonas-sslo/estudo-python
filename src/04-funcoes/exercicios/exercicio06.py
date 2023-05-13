""" Exercicio 06 """

def calculo_volume(usuario):
    volume = (usuario['comprimento'] * usuario['altura'] * usuario['largura']) / 1000
    return volume

def calculo_termostato(volume):
    termostato = volume * 0.05 * (usuario['temperatura desejada'] - usuario['temperatura ambiente'])
    return termostato

def qtd_filtragem(volume):
    filtragem = 2.5 * volume
    return filtragem


comprimento = float(input('Insira o valor do comprimento em cm: '))
altura = float(input('Insira o valor da altura em cm: '))
largura = float(input('Insira o valor da largura em cm: '))
temp_desejada = float(input('Insira a temperatura desejada em graus celsius: '))
temp_ambiente = float(input('Insira a temperatura ambiente em graus celsius: '))

usuario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temperatura desejada': temp_desejada,
    'temperatura ambiente': temp_ambiente
}

volume = calculo_volume(usuario)
termostato = calculo_termostato(volume)
filtragem = qtd_filtragem(volume)

print(f'O volume do aquário é de {volume} litros')
print(f'A potência do termostato é de {termostato} watts')
print(f'A quantidade em litros de filtragem por hora necessária para manter a qualidade de água é de {filtragem}')