# Faça o computador pensar em um numero entre 0 a 5 e peça para o usuário
# tentar adivinhar qual foi o número escolhido pelo computador
# O programa devera escrever na tela se o usuário vencou ou perder.
from random import randint

x = int(randint(0, 5))
y = int(input('Adivinhe que numero eu escolhi, hihi :) '))
if y == x:
    print("""
    Oh!!..
    Parece que voce acertou, parabens!""")
else:
    print("""
    Hihi!
    Errrou!... Eu escolhi {}
    Mais sorte da próxima vez""".format(x))
