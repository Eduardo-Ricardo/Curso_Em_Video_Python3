"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
"""


def fatorial(numero_local, show=False):
    """
    Fatorial retorna o fatorial de um número.
    :param numero_local: rece o numeor para o cálculo.
    :param show: se == True mostra o cálculo, caso contraio não mostra.
    :return: retorna o valor inteiro do fatorial.
    """
    for c in range(numero_local - 1, 1, -1):
        numero_local = numero_local * c
        if show:
            if c == 2:
                print(f'{c} * 1 = ', end='')
                return numero_local
            elif c + 1 == numero_local / c:
                print(f'{numero_local / c:.0f}! = {numero_local / c:.0f} * ', end='')
            else:
                print(f'{c} * ', end='')
    return numero_local


print(fatorial(int(input('Digite um número: ')), show=True))
