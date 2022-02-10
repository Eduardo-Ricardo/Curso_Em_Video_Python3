# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
ctps = {'nome': str(input('Nome: ')),
        'nascimento': int(input('Ano de nascimento: ')),
        'carteira': int(input('Carteira de Trabalho [0 nâo tem]: '))}

if ctps['carteira'] > 0:
    ctps.update({'contratacao': int(input('Ano de contratação: ')),
                 'Salario': float(input('Salário: '))})
    ctps.update({'aposentadoria': int(ctps['contratacao'] + 35 - ctps['nascimento'])})
    if ctps['aposentadoria'] < 60:
        ctps['aposentadoria'] = 60
    ctps.update({'ano_aposentadoria': ctps['nascimento'] + ctps['aposentadoria']})
for k, v in ctps.items():
    print(f'{k}: {v}')