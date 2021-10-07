# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
x = randint(1, 10)
count = 0
jogador = int(input('Blz vo te dar 5 chances para acertar o numero que to pensando\nComeçando agora!: '))
while count <= 4:
    x = randint(1, 10)
    if jogador == x:
        print('Oh, acertou kkkkkkk')
        count = 4
    else:
        print(end='Há! Eu escolhi {}. '.format(x))
        if count < 4:
            jogador = int(input('Bora mais uma vez: '))
        elif count == 4:
            jogador = int(input('Oh, sua ultima chance: '))
            print('Oh, acertou kkkkkkk') if x == jogador else False
    count += 1
