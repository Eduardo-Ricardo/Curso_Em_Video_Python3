"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(nascimento_local):
    import datetime
    idade_local = datetime.date.today().year - nascimento_local
    if 15 < idade_local < 18 or idade_local >= 70 and idade_local > 0:
        print("Seu voto é facultativo.")
    elif idade_local >= 18:
        print('Seu voto é obrigatório.')
    elif 16 > idade_local > 0:
        print('Seu voto é proibido.')
    else:
        print('Data Inválida.')


voto(int(input('Digite seu ano de nascimento: ')))