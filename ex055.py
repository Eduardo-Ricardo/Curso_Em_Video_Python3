# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
repeticoes = int(input('Sera analizado o peso de quantas pessoas? '))
peso_menor = int(input('quanto pesa a pessoa 1° pessoa? '))
peso_maior = peso_menor
for c in range(2, repeticoes+1):
    analize = int(input(f'quanto pesa a pessoa {c}° pessoa? '))
    if analize > peso_maior:
        peso_maior = analize
    elif analize < peso_menor:
        peso_menor = analize
print(f'peso maior: {peso_maior}\npeso menor: {peso_menor}')