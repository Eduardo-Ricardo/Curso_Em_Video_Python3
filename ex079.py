# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from random import randint
lista = []
resp = 's'

while True:
    if resp == 'n':
        break
    elif resp != 'n' and resp != 's':
        resp = str(input('Resposta Invalida!\nQuer continar? [S/N]').lower())
    else:
        lista.append(int(input('Digite um numero: ')))
        resp = str(input('Quer continar? [S/N]').lower())

aux = lista[:]

for c in range(0, len(lista)):
    lista[c] = min(aux)
    mini = aux.index(min(aux))
    del aux[mini]
# ou somplesmente usar (lista.sort())
c = 1

while True:
    if c == len(lista):
        break
    if lista[(c-1)] == lista[c]:
        del lista[c-1]
        c -= 1
    c += 1

print(lista)
