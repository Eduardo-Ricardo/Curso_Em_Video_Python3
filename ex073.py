# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

times = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense",
         "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR",
         "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense", )

# a) Os 5 primeiros times.
c = 0
print(f'{"-"*28}Lista de times do Brasileirão{"-"*28}')
for d in range(0, 5):
    print(f'+{"-" * 4}+{"-" * 15}' * 4, end="")
    print('+')
    while c < 20:
        print(f'|{c+1:>4}|{times[c]:<15}', end="")
        c += 5
    print('|')
    c = d + 1
    if c == 20:
        break
print(f'+{"-" * 4}+{"-" * 15}' * 4, end="")
print('+')

# a) Os 5 primeiros times.
print('\n\n* Os 5 primeiros times. *')
for c in range(0, 5):
    print(f'+{"-" * 4}+{"-" * 15}+')
    print(f'|{c+1:>4}|{times[c]:<15}|')
print(f'+{"-" * 4}+{"-" * 15}+')

# b) Os últimos 4 colocados.
print('\n\n* Os últimos 4 colocados. *')
for c in range(-4, 0):
    print(f'+{"-" * 4}+{"-" * 15}+')
    print(f'|{c + 21:>4}|{times[c]:<15}|')
print(f'+{"-" * 4}+{"-" * 15}+')

# c) Times em ordem alfabética.
print(f'\n\n{"-"* 19}Times em ordem alfabética.{"-"* 20}')
c = 0
for d in range(0, 5):
    print(f'+{"-" * 15}' * 4, end="")
    print('+')
    while c < 20:
        print(f'|{sorted(times)[c]:<15}', end="")
        c += 5
    print('|')
    c = d + 1
    if c == 20:
        break
print(f'+{"-" * 15}' * 4, end="")
print('+')

# d) Em que posição está o time da Chapecoense.
print(f'O time {times[19]}, se encontra na posicção {times.index("Chapecoense") + 1}')
