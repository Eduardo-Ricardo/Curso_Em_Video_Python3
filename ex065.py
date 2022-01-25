# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
c = 0
soma = 0
resposta = 's'
while resposta != 'n':
    c += 1
    numero = int(input('Digite um numero: '))
    if c == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    soma += numero
    resposta = str(input('Quer continuar? [s/n]: ')).lower()
    while resposta != 's' and resposta != 'n':
        print('Resposta invalida')
        resposta = str(input('Quer continuar? [s/n]: ')).lower()
print('maior = {} \nmenor = {} \nmedia = {}'.format(maior, menor, soma/c))