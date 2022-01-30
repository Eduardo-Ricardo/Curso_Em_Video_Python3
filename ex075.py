# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares

tupla = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'O numero de vezes que o valor 9 se repetiu: {tupla.count(9)}\n'
      f'O número 3 apareceu pela primeira vez na posição {tupla.index(3)}\n'
      f'Os numeros pares são: ', end="")
for e in tupla:
    if e % 2 == 0:
        print(f'{e} ; ', end="")

