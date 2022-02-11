"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los na lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""


def sorteia(x):
    from random import randint
    lista = []
    for c in range(0, x):
        lista.append(randint(1, 100))
    return lista


def somaPar(numeros = []):
    par = 0
    for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0:
            if par == 0:
                par = numeros[c]
            else:
                par += numeros[c]
    return par


lista = (sorteia(5))
print(lista)
print(somaPar(lista))
