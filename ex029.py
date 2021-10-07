# Escreva um algoritimo que leia a velocidade do carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado,
# A multa vai custar R$ 7,00 para cada Km acima do limite.
from random import uniform

vel = int(uniform(50, 130))
if vel > 80:
    print("""
    Sua velocidade é de {} Km/h
    Parece que você esta acima do limite de velocidade permitido!
    Você sera multado em de R$ {:.2f}!!! >:(""".format(vel, (vel-80)*7))
else:
    print("""
    Sua velicidade é de {} Km/h
    Voce esta abaixo do limite de velocidade permitido!
    Siga sua viagem com segurança! :)""".format(vel))
