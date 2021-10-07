# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.
import datetime
repeticoes = int(input('Numero de pessoas: '))
posicao = 'dentre as pessoas selecionadas a '
pessoas_maiores_de_idade = 0
for c in range(1, repeticoes+1):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    maior_idade = int(nascimento + 18)
    if maior_idade <= datetime.date.today().year:
        pessoas_maiores_de_idade += 1
        posicao += '{}°, '.format(c)
if pessoas_maiores_de_idade > 1:
    posicao += 'são maiores de idade.'
elif pessoas_maiores_de_idade == 1:
    posicao += 'é maior de idade.'
else:
    posicao += 'nenhuma é mair de idade.'
print(posicao)
