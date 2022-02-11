"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:
 a) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada
"""
from time import sleep


def contator(inicio, fim, passo):
    print('-' * 40)
    d = 0
    for c in range(inicio, fim, passo):
        print(f'{c}', end='')
        sleep(0.3)
        print(f', ', end='')
        sleep(0.7)
        d += 1
        if d % 10 == 0:
            print()
    print('-' * 40)


contator(1, 11, 1)
contator(10, 0, -1)
contator(9, 69, 3)