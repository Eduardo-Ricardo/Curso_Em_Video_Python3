# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
termo01 = int(input('Digite o valor do primero termo: '))
termo02 = int(input('Digite o valor do segundo termo: '))
validador = 0
y = 0
for possivel_numero_primo in range(termo01, termo02):
    for teste in range(1, possivel_numero_primo+1):
        if possivel_numero_primo % teste == 0:
            validador = validador + 1
    if validador == 2:
        print(possivel_numero_primo)
        y = y + 1
    validador = 0
print(y)
