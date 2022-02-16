"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from mod109 import aumentar, diminuir, dobro, metade, moeda
num = float(input('Digite um preço: '))
print(f'Aumentando 10% de {moeda(num)} fica {aumentar(num, 10, contabil=True)}\n'
      f'Diminuindo 10% de {moeda(num)} fica {diminuir(num, 10, contabiil=True)}\n'
      f'O dobro de {moeda(num)} fica {dobro(num, contabil=True)}\n'
      f'Metade de {moeda(num)} fica {metade(num, contabil=True)}')