# Crie um programa que leia um numero e mostre na tela se ele é par ou impar

x = int(input('Digite um numero: '))
if x%2 == 1:
    print('o numero {} é impar!'.format(x))
else:
    print('O numero {} é par!'.format(x))
