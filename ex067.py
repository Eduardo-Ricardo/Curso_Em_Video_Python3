# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    numero = int(input('Calcular tabuada: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{c:>2} * {numero} = {numero*c:^2}')
        c += 1
