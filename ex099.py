"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.
"""
from typing import List


def comparador(*numeros):
    return max(numeros)


print(comparador(6, 8, 78, 10))

