"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
também um programa que importe esse módulo e use algumas dessas funções.
"""
from mod107 import aumentar, diminuir, dobro, metade

num = float(input('Digite um preço: '))
print(f'Aumentando 10% fica R$ {aumentar(num, 10):.2f}\n'
      f'Diminuindo 10% fica R$ {diminuir(num, 10):.2f}\n'
      f'O dobro é {dobro(num):.2f}\n'
      f'Metade é {metade(num):.2f}')