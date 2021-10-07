# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

nn = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = 1
print(nn)
while n < 10:
  nn += razao
  print(nn)
  n += 1
