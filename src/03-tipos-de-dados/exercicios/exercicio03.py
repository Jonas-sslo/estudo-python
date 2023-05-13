""" Exercicio 03 """

mes = int(input('Insira o mês do ano pelo seu número (Ex: 1 corresponde a Janeiro): '))

nome_mes = {
    1: 'Janeiro',
    2: 'Fevereiro', 
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

if 1 <= mes <= 12:
    print(f'O mês solicitado é: {nome_mes[mes]}')