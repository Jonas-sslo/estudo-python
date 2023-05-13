""" Exercicio 02 """

mes = int(input('Insira o mês do ano pelo seu número (Ex: 1 corresponde a Janeiro): '))

nome_mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

if 1 <= mes <= 12:
    print(f'O mês solicitado é: {nome_mes[mes - 1]}')
else:
    print('Insira um mês que seja válido!')
