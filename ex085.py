# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for c in range(0, 7):
    entrada = int(input(f'Digite um número [{c+1}/7]: '))
    if entrada % 2 == 0:
        numeros[0].append(entrada)
    else:
        numeros[1].append(entrada)
numeros[0].sort()
numeros[1].sort()
print(numeros)