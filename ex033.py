# Faça um algoritmo que leia 3 numero e mostre qual é o maior e qual é o menor

a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))
c = int(input('Digite o 3° valor: '))

if a > b:
    if a > c:
        print('O maior numero é o {}'.format(a))
if b > a:
    if b > c:
        print('O maior numero é o {}'.format(b))
if c > a:
    if c > b:
        print('O maior numero é o {}'.format(c))
if a < b:
    if a < c:
        print('O menor numero é o {}'.format(a))
if b < a:
    if b < c:
        print('O menor numero é o {}'.format(b))
if c < a:
    if c < b:
        print('O menor numero é o {}'.format(c))