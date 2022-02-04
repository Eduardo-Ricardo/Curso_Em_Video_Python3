# Faça um programa que leia 5 valores numéricos e guarde-os numa lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    lista.insert(c, int(input(f'Digite um valor de que ocupara a poscição [{c}]: ')))
print(f'Maior: {max(lista)}\nMenor: {min(lista)}')
print(f'E suas respectivas posicções {lista.index(max(lista))}, {lista.index(min(lista))}')

