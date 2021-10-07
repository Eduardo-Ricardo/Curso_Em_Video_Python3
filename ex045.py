# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
sistema = randint(1, 3)
if sistema == 1:
    sistema1 = str('preda')
elif sistema == 2:
    sistema1 = str('tisora')
elif sistema == 3:
    sistema1 = str('papier')
jogador = int(input("""Agora é a sua vez, eu ja fiz a minha escolha:
1. Preda
2. Tisora
3. Papier
\033[32mEscolha:"""))

if jogador == 1 and sistema == 1:
    print('\033[36mHe He, parece que empatou! :|')
elif jogador == 1 and sistema == 2:
    print('\033[35mOOoOoohhH MMYYY GOOOOD, ok ok voce venceu :(')
elif jogador == 1 and sistema == 3:
    print('\033[31mHa! Perdeu vacilão!')
elif jogador == 2 and sistema == 1:
    print('\033[31mHa! Perdeu vacilão!')
elif jogador == 2 and sistema == 2:
    print('\033[36mHe He, parece que empatou! :|')
elif jogador == 2 and sistema == 3:
    print('\033[35mOOoOoohhH MMYYY GOOOOD, ok ok voce venceu :(')
elif jogador == 3 and sistema == 1:
    print('\033[35mOOoOoohhH MMYYY GOOOOD, ok ok voce venceu :(')
elif jogador == 3 and sistema == 2:
    print('\033[31mHa! Perdeu vacilão!')
elif jogador == 3 and sistema == 3:
    print('\033[36mHe He, parece que empatou! :|')
print('Eu escolhi '+sistema1)
