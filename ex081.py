# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# *
# A) Quantos números foram digitados.
# *
# B) A lista de valores, ordenada de forma decrescente.
# *
# C) Se o valor 5 foi digitado e está ou não na lista

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

# A) Quantos números foram digitados.
print(f'Numero digitados {len(lista)}')

# B) A lista de valores, ordenada de forma decrescente.

print(f'Lista ordenada de forma decrescente {lista.sort(reverse=True)}')

# C) Se o valor 5 foi digitado e está ou não na lista

if 5 in lista:
    print(f'O numero 5 foi digitado na posição {lista.index(5)}')
else:
    print('O numero 5 não esta na lista')