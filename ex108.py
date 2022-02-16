"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
valor monetário formatado.
"""

from mod107 import aumentar, diminuir, dobro, metade
from mod108 import moeda

num = float(input('Digite um preço: '))
print(f'Aumentando 10% de {moeda(num)} fica {moeda(aumentar(num, 10))}\n'
      f'Diminuindo 10% de {moeda(num)} fica {moeda(diminuir(num, 10))}\n'
      f'O dobro de de {moeda(num)} fica {moeda(dobro(num))}\n'
      f'Metade de {moeda(num)} fica {moeda(metade(num))}')


