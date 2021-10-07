# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número para ser convertido: '))
escolha = int(input("""Binário: 1.
octal: 2.
hexadecimal: 3.
Agora escolha uma das opções acima: """))
if escolha == 1:
    print('O número decimal {}, convertido para binário é {}.'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número decimal {}, convertido para binário é {}.'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número decimal {}, convertido para binário é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Digitou uma escolha inválida\nPresta atenção ai! \033[1;31m>:(')
