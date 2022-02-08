# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from random import randint

resp = int(input('Como deseja preencher as notas?'
                 '\n1. Manualmente'
                 '\n2. Aleatóriamente'
                 '\n..: '))
aluno = []
c = 0
while True:
    nome = str(input('Digite o nome do auluno para lançar as notas [Deixa essa caixa vazia para continuar]: '))
    if nome == '':
        break
    aluno.append([nome])
    aluno[c].append([])
    for d in range(0, 4):
        if resp == 1:
            aluno[c][1].append(int(input(f'Digite a nota do {d + 1}° Bimestre: ')))
        elif resp == 2:
            aluno[c][1].append(randint(6, 20) / 2)
    c += 1
media = 0
txt = str(f'+{"-" * 4}+{"-" * 12}+{"------+" * 4}{"-" * 7}+')
print(f'{txt}\n| Id |{"Nome":^12}| 1°Bi | 2°Bi | 3°Bi | 4°Bi | Media |\n{txt}')
for c in range(0, len(aluno)):
    print(f'|{c:^4}|{aluno[c][0]:<12}|', end='')
    for d in range(0, 4):
        print(f'{aluno[c][1][d]:^6}|', end='')
        media += aluno[c][1][d]
    media = media / 4
    print(f'{media:^7.2f}|')
    print(f'{txt}')
    media = 0