# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Frase: ')).strip().upper()
frase = ' '.join(frase).split()
palindromo_acumulador = ''
for c in range(len(frase), 0, -1):
    frase = ''.join(frase)
    palindromo = str(frase[c-1])
    palindromo_acumulador = palindromo_acumulador + palindromo
if palindromo_acumulador == frase:
    print('a frase que voce digitou foi "{}"\nao contrario fica            "{}"'. format(frase, palindromo_acumulador))

    print('esa porra é um  palindromo')

else:
    print('a frase que voce digitou foi "{}"\nao contrario fica            "{}"'.format(frase, palindromo_acumulador))
    print('esa porra não é um  palindromo')