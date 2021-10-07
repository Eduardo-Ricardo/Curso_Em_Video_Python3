# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

x, y = int(input('Digite o 1° número: ')), int(input('Digite o 1° número: '))

if x == y:
    print('O valor de ambos são iguais.')
else:
    if x > y:
        maior = int(x)
        menor = int(y)
    elif y > x:
        maior = y
        menor = x
    print(f'o número {maior} é o maior e o {menor} é menor')
