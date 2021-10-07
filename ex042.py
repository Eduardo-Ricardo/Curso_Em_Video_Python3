# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = int(input('Digite o lado a: '))
b = int(input('Digite o lado b: '))
c = int(input('Digite o lado c: '))
if abs(b-c) < a < b + c:
    if a == b and b == c:
        print('EQUILÁTERO: todos os lados iguais')
    elif a == b or b == c or c == a:
        print('ISÓSCELES: dois lados iguais, um diferente')
    else:
        print('ESCALENO: todos os lados diferentes')
else:
    print('Isso nem triângulo é')
