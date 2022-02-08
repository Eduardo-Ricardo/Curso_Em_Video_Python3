# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
from random import randint

resp = int(input('Como deseja preencher a matriz?'
                 '\n1. Manualmente'
                 '\n2. Aleatóriamente'
                 '\n..: '))

matriz = [[], [], []]
soma = somalinha = somapar = somacolum = 0
for c in range(0, 3):
    for d in range(0, 3):
        if resp == 2:
            matriz[c].append(randint(0, 20))
        elif resp == 1:
            matriz[c].append(int(input(f'Digite o numero para ocupar a posição [{c}, {d}]: ')))
        soma += matriz[c][d]
#print(matriz)
print('    1      2      3')
for c in range(0, 3):
    print(f'{c+1} ', end='')
    for d in range(0, 3):
        print(f'[ {matriz[c][d]:^2}], ', end='')
        somalinha += matriz[c][d]
        if matriz[c][d] % 2 == 0:
            somapar += matriz[c][d]
    print(f'Soma da {c+1}º linha = {somalinha} / Maior valor da linha: {max(matriz[c])}')
    somalinha = 0
for c in range(2, -1, -1):
    for d in range(0, 3):
        somacolum += matriz[d][c]
    print(f'  {"  |    "*(c)}  →Soma da Coluna = {somacolum}')
    somacolum = 0
print(f'\n  Soma total= {soma} / e a soma dos numeros pares: {somapar} ')
