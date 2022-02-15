"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.
"""


def ficha_jogador(j, g):
    txt_local = f'o jogador {j} fez {g} gols nesta temporada.'
    return txt_local


ficha = {'nome': str(input('Nome: ')),
               'gols': str(input('Gols: '))}
if ficha['nome'] == '':
    ficha['nome'] = '<desconhecido>'
if ficha['gols'] == '' or not ficha['gols'].isnumeric():
    ficha['gols'] = '0'
print(ficha_jogador(ficha['nome'], ficha['gols']))