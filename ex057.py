# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
sexo = 'w'
while sexo not in 'MF':
    sexo = str(input('Qual teu sexo? ')).upper().strip()[0]

