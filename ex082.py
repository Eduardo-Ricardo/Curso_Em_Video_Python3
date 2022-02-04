# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

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
par = []
impar = []
for c in range(0, len(lista)):
    if lista[c] % 2 == 1:
        impar.append(lista[c])
    else:
        par.append(lista[c])
print(f'lista: {lista}')
if 0 >= par[0] or par[0] >= 0:
    print(f'Par: {par}')
if 0 >= impar[0] or impar[0] >= 0:
    print(f'Impar: {impar}')