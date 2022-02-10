# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.
dicio = {'nome': str(input('Nome: ')),
         'media': float(input('Media: ')),
         'situacao': ''
         }

if dicio['media'] >= 7:
    dicio['situacao'] = 'Aprovado'
elif dicio['media'] < 4:
    dicio['situacao'] = 'Reprovado'
else:
    dicio['situacao'] = 'Recuperacao'

print(f'O aluno {dicio["nome"]} com a media {dicio["media"]} esta {dicio["situacao"]}')