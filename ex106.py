"""
Faça um minissistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""


def linha(x):
    from random import randint
    cores = ['\033[1;30;48m', '\033[1;31;48m', '\033[1;32;48m', '\033[1;33;48m',
             '\033[1;34;48m', '\033[1;35;48m', '\033[1;36;48m', '\033[1;37;48m']
    for c in range(0, x):
        print(f'{cores[randint(0, 7)]}-=', end='')
    print()
    for c in range(0, x):
        cores_0 = ['\033[1;30;41m', '\033[1;30;42m', '\033[1;30;43m', '\033[1;30;44m',
                   '\033[1;30;45m', '\033[1;30;46m', '\033[1;30;47m']
        print(f'{cores_0[randint(0, 6)]}-=', end='')
    print('\033[1;30;48m')
    for c in range(0, x):
        print(f'{cores[randint(0, 7)]}-=', end='')
    print()


def ajuda(funcao):
    from random import randint
    cores = ('\033[1;30;48m', '\033[1;31;48m', '\033[1;32;48m', '\033[1;33;48m',
             '\033[1;34;48m', '\033[1;35;48m', '\033[1;36;48m', '\033[1;37;48m',)
    cor_linha = cores[randint(0, 7)]
    letra = cores[randint(0, 7)]
    linha(50)
    help(funcao)
    linha(50)


while True:
    texto = str(input('Digine o nome da função[ deixe vazio para finalizar]: '))
    if texto == '':
        break
    ajuda(texto)
