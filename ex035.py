# escreva um algoritmo que leia 3 comprimentos de reta e diga se elas podem formar um triangulo
#| b - c | < a < b + c

a = int(input('Digite o valor do 1° lado: '))
b = int(input('Digite o valor do 2° lado: '))
c = int(input('Digite o valor do 3° lado: '))
if abs(b-c) < a & a < b + c:
    print("é um triângulo possivel")
else:
    print('Essa 3 retas não podem formar um triângulo')

