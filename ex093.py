# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome': str(input('Nome do jogador: ')),
           'partidas_jogadas': int(input('Partidas disputadas: ')),
           'total': int(0)}

for c in range(0, jogador['partidas_jogadas']):
    jogador.update({f'jogo{c+1}': int(input(f'Gols marcados no {c+1}º jogo: '))})
    jogador['total'] += jogador[f'jogo{c+1}']

print(f'{"__" * 30}\n{jogador}\n{"__" * 30}')

print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'Gols: [ ', end="")
for c in range(0, jogador['partidas_jogadas']):
    print(f'{jogador[f"jogo{c+1}"]}, ', end="")
print(f']\nO campo total tem o valor {jogador["total"]}\n{"__" * 30}')

for c in range(0, jogador['partidas_jogadas']):
    print('Jogo {}: {} gol(s)'.format(c+1, jogador[f'jogo{c+1}']))
