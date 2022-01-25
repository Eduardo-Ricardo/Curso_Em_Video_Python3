# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
troco = int(input('Qual o valor a ser sacado: '))
while True:
    if troco >= 50:
        notas_50 = (troco // 50)
        troco = troco % 50
        print(f'{notas_50} nota(s) de R$ 50')
    if troco >= 20:
        notas_20 = (troco // 20)
        troco = troco % 20
        print(f'{notas_20} nota(s) de R$ 20')
    if troco >= 10:
        notas_10 = (troco // 10)
        troco = troco % 10
        print(f'{notas_10} nota(s) de R$ 10')
    if troco >= 1:
        notas_1 = (troco // 1)
        print(f'{notas_1} nota(s) de R$ 1')
    break
