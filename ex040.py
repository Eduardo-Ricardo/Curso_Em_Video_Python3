# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota01 = float(input('Digite a 1° nota: '))
nota02 = float(input('Digite a 2° nota: '))
media = (nota01 + nota02) / 2
if media > 7:
    print('APROVADO')
elif media > 4:
    print('Em RECUPERAÇÃO')
else:
    print('REPROVADO')
