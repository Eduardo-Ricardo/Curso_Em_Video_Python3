# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
peso = []

while True:
    print('Deixe a caixa vazia para sair')
    dados.append(str(input('Digite um nome: ')))
    if dados[-1] == '':
        del dados[:]
        break
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    del dados[:]

for c in range(0, len(pessoas)):
    peso.append(pessoas[c][1])

pesado = []

for c in range(0, 2):
    pesado.append(pessoas[peso.index(max(peso))])
    peso.insert(peso.index(max(peso)), 0)
    del peso[peso.index(max(peso))]
del peso[:]

for c in range(0, len(pessoas)):
    peso.append(pessoas[c][1])
leve = []

for c in range(0, 2):
    leve.append(pessoas[peso.index(min(peso))])
    print(leve)
    peso.insert(peso.index(min(peso)), (max(peso)+1))
    del peso[peso.index(min(peso))]
del peso[:]


print(f'Ao todo foram cadastrado {len(pessoas)} pessoas')
print(f'pessoas mais pesadas foram {pesado[0][0]} e {pesado[1][0]} com {pesado[0][1]} Kg'
      f' e {pesado[1][1]} respectivamente')
print(f'pessoas mais leves foram {leve[0][0]} e {leve[1][0]} com {leve[0][1]} Kg'
      f' e {leve[1][1]} respectivamente')
