# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
n = int(input('Quantidade de termos: '))
c = 1
fibonacci = 1
soma = 0
while c <= (n):
    if c >= 2:
        print(' ; {}'.format(fibonacci), end='')
        aux = fibonacci
        fibonacci += soma
        soma = aux
    else:
        print('0', end='')
    c += 1
