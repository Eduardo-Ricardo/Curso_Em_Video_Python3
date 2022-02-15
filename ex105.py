"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""


def notas(*notas, sit=False):
    txt = ''
    analize = {}
    soma = 0
    for c in range(0, len(notas)):
        soma += notas[c]
    media = soma / len(notas)
    analize = {'qtd de notas': len(notas),
               'maior nota': max(notas),
               'menor nota': min(notas),
               'media': media}
    if sit:
        if media < 4:
            txt = 'Péssima'
        elif media < 6:
            txt = 'Ruim'
        elif media < 8:
            txt = 'Boa'
        elif media < 10:
            txt = 'Ótima'
        analize.update({'situacao': txt})
    return analize


print(notas(4, 4, 6, 0, sit=True))
