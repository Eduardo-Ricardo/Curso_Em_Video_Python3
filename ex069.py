# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
mais_18 = homens = mulheres_menos_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).lower().strip()
    if idade > 18:
        mais_18 += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulheres_menos_20 += 1
    resposta = str(input('Deseja continuar [s/n]: '))
    if resposta == 'n':
        break
print(f"""Pessoas com mais de 18 anos: {mais_18}
Homens cadastrados cadastradas: {homens}
Mulhreres com menos de 20 anos cadastradas: {mulheres_menos_20}""")