# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
c = 0
while True:
    pc = randint(1, 2)
    usuario = str(input('voce quer par ou impar?[P/I]')).lower().strip()
    numero = int(input('digite um valor (de preferencia entre um ou dois): '))
    if ((numero + pc) % 2 == 1 and usuario == 'i') or ((numero + pc) % 2 == 0 and usuario == 'p'):
        c += 1
        print(f'Eu escolhi {pc} você {numero}')
        print(f'voce venceu\ntotal de vitorias: {c}')
    else:
        print(f'Eu escolhi {pc} você {numero}')
        print('Voce perdeu')
        break
