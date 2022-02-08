# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a
# matriz na tela, com a formatação correta.
from random import randint

resp = int(input('Como deseja preencher a matriz?'
                 '\n1. Manualmente'
                 '\n2. Aleatóriamente'
                 '\n..: '))

matriz = [[], [], []]

for c in range(0, 3):
    for d in range(0, 3):
        if resp == 2:
            matriz[c].append(randint(0, 20))
        elif resp == 1:
            matriz[c].append(int(input(f'Digite o numero para ocupar a posição [{c}, {d}]: ')))

print('    0      1      2')
for c in range(0, 3):
    print(f'{c} ', end='')
    for d in range(0, 3):
        print(f'[ {matriz[d][c]:^2}], ', end='')
    print('')