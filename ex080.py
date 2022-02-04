# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um numero [{c+1}/5]: ')))
    busca = numeros[c]
    print(f'o numero {numeros[c]} foi adicionado na posição ', end="")
    aux = numeros[:]
    for d in range(0, len(numeros)):
        numeros[d] = min(aux)
        mini = aux.index(min(aux))
        del aux[mini]
    if numeros.index(busca) == (len(numeros) - 1):
        print('final da lista')
    elif numeros.index(busca) == 0:
        print('no começo da lista')
    else:
        print(f'{numeros.index(busca)} da lista')

print(numeros)