# Um algoritmo que escolhe de forma aleatoria entre 4 alunos
import random

aluno1 = input('Digite o nome do 1° aluno: ')
aluno2 = input('Digite o nome do 2° aluno: ')
aluno3 = input('Digite o nome do 3° aluno: ')
aluno4 = input('Digite o nome do 2° aluno: ')

print(random.choice((aluno1, aluno2, aluno3, aluno4)))
