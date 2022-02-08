# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = []
numeros = []
n = d = 1
qtd_jogos = int(input('Quantos jogos serão feitos: '))
for c in range(0, qtd_jogos):
    print(f'+{"-=-"*17}+\n')
    sleep(1)
    print(f'Palpite para o {c+1}° jogo\n')
    while d <= 6:
        numeros.append(randint(1, 60))
        if numeros[-1] in numeros[0:-1]:
            del numeros[-1]
            d -= 1
        d += 1
    d = 1
    numeros.sort()
    jogos.append(numeros[:])
    for linha in range(0, 6):
        for coluna in range(0, 10):
            if n in numeros:
                print(f'\033[1;30;42m({n:^2})', end='')
                print('\033[0;38;43m ', end='')
            else:
                print(f'[{n:^2}] ', end='')
            n += 1
        print()
    print('\n', numeros, '\n')
    del numeros[:]
    n = 1

