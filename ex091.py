# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
aux = [[], []]
c = 0
dicio = {'Pedro': int(randint(1, 6)),
        'Gustavo': int(randint(1, 6)),
        'Lucas': int(randint(1, 6)),
        'Julia': int(randint(1, 6)),
         }
for k, v in dicio.items():
    print(f'{k} jogou o dado e caiu {v}')
    aux[0].append(v)
    aux[1].append(k)
    sleep(0.5)
dicio.clear()
print(f'\nEntão em ordem decrescente fica: \n')

# importar a biblioteca operator/ from operator import itemgetter
# criar uma lista ranking
# usar o comando ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# vai reduzir o laço a baixo em uma linha apenas.
for c in range(0, 4):
    ende = aux[0].index(max(aux[0]))
    dicio.update({aux[1][ende]: max(aux[0])})
    del aux[0][ende]
    del aux[1][ende]
for k, v in dicio.items():
    print(f'{k}: {v} ')
