""""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
from time import sleep

media = 0
pessoas = []

while True:
    print('Deixe vazio e aperte enter para sair')
    dados = {'nome': str(input('Nome: ')).strip().title()}
    if dados['nome'] == '':
        break
    dados.update({'sexo': str(input('Sexo: ')).strip().upper()})
    while dados['sexo'] != 'F' and dados['sexo'] != 'M':
        print('Digite somente [M/F]')
        dados.update({'sexo': str(input('Sexo: ')).strip().upper()})
    dados.update({'idade': int(input('Idade: '))})
    while dados['idade'] <= 0:
        print('Idade Invalida!')
        print('Tente novamente', sleep(1))
        dados.update({'idade': int(input('Idade: '))})
    media += dados['idade']
    pessoas.append(dados.copy())
media = media/len(pessoas)
print(f'{"_" * 80}\n'
      f'Total de pessoas cadastradas: {len(pessoas)}\n'
      f'Media de idade: {media}')

mulheres = []
idade_acima = []

for dados in pessoas:
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    if dados['idade'] > media:
        idade_acima.append(dados['nome'])
print(f'Mulheres Cadastradas: {mulheres}\n'
      f'Pessoas com a idade acima da média: {idade_acima}\n'
      f'{"_" * 80}')