"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
contudo fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ')
"""


def leia_int(txt_loc):
    numero = str(input(txt_loc))
    for c in range(0, len(numero)):
        if numero[c] not in '0123456789':
            print('\033[1;31;48mDigite apenas numeros!')
            exit()
    return int(numero)


n = leia_int('Digite um número: ')
print(f'Você digitou o numero {n}.')