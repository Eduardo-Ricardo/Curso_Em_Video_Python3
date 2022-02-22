"""Vamos criar um menu em Python, usando modularização."""
from utilidadesCeV.edit import *
from utilidadesCeV.dado import leia_int

titulo('Menu Principal')

pergunta = f"""{edit('bold', 'yellow')}1 - {edit('underline', 'blue')}Ver pessoas cadastradas{edit('none')}
{edit('bold', 'yellow')}2 - {edit('underline', 'blue')}Cadastras nova pessoa{edit('none')}
{edit('bold', 'yellow')}3 - {edit('underline', 'blue')}Sair{edit('none')}
{edit('bold', 'yellow')}Sua opção: {edit('none')}"""
try:
    while True:
        resp = leia_int(pergunta)
        if resp == 1:
            print(f'{edit("none", "blue")}', end='')
            titulo(f'Opção 1')
            print(f'{edit("none")}')
        elif resp == 2:
            print(f'{edit("none", "blue")}', end='')
            titulo(f'Opção 2')
            print(f'{edit("none")}')
        elif resp == 3:
            print(f'{edit("none", "blue")}', end='')
            titulo(f'Programa Finalizado')
            print(f'{edit("none")}')
            break
        else:
            print('Valor invalido')
except(ValueError, TypeError, KeyboardInterrupt):
    print('programa deu pau')