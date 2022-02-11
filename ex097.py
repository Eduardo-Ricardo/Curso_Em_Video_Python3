"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

Ex:
escreva(‘Olá, Mundo!’)

Saída:

~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""


def escreva(txt):
    print(f'{"_" * (len(txt) + 2)}\n {txt}\n{"_" * (len(txt) + 2)}')


escreva(str(input('...')))
