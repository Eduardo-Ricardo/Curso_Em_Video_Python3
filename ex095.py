"""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
"""

tabela = []
gols = []

while True:
    jogador = {'nome': str(input('Nome do jogador: ')).strip().title()}
    if jogador['nome'] == '':
        break
    jogador.update({'partidas_jogadas': int(input('Partidas disputadas: ')),
                    'gols': gols[:],
                    'total': int(0)})

    for c in range(0, jogador['partidas_jogadas']):
        gols.append(int(input(f'Gols marcados no {c+1}º jogo: ')))
        jogador['total'] += gols[-1]
        jogador.update({'gols': gols[:]})

    gols.clear()
    tabela.append(jogador)
    print(f'Jogador: {jogador}')
print(f'Tabela: {tabela}\n\n')
txt = str(f'+{"-" * 4}+{"-" * 25}+{"-" * 20}+{"-" * 7}+')
print(txt,
      f'\n|{"Id":^4}|{"Nome":^25}|{"Gols":<20}|{"Total":^7}|'
      f'\n{txt}')
for e, c in enumerate(tabela):
    txt_gols = str(c["gols"])
    print(f'|{e:^4}|{c["nome"]:^25}|{txt_gols:20}|{c["total"]:^7}|'
          f'\n{txt}')
while True:
    resp = str(input('\nDeseja ver dados especificos de algum jogardor?\n'
                     'Digite o Id [ou deixe vazio] e pressione enter para sair: '))
    if resp == '':
        break
    resp = int(resp)
    print(f'\n\nNome: {tabela[resp]["nome"]}')
    for e, c in enumerate(tabela[resp]["gols"]):
        print(f'......{e+1}° jogo: {c} gols......')
 