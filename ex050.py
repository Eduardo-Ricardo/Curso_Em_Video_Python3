# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

count = 0
for c in range(0, 7):
    x = int(input('Digite um numero: '))
    if x % 2 == 0:
        count = x + count
print(count)
