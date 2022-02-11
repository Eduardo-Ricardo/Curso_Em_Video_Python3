"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    print(f'Valor da area: {largura*comprimento:.2f} unidades de medida')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
