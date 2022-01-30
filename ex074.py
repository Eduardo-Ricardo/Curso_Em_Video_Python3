# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print(f'A tupla sortida na ordem padão {tupla},\n'
      f'Seu o maior e o menor valor respectivamente:{sorted(tupla)[-1]}, {sorted(tupla)[0]},\n'
      f'agora na ordem Crescente {sorted(tupla)}')
