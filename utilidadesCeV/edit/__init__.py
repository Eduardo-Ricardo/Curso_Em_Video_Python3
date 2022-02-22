def edit(tip='none', let='white', fun='black'):
    tipo = {'none': '[0',
            'bold': '[1',
            'underline': '[4',
            'negative': '[7'}

    cor_letra = {'red': ';31',
                 'green': ';32',
                 'yellow': ';33',
                 'blue': ';34',
                 'purprle': ';35',
                 'blue2': ';36',
                 'gray': ';37',
                 'white': ';38'}
    cor_fundo = {'red': ';41m',
                 'green': ';42m',
                 'yellow': ';43m',
                 'blue': ';44m',
                 'purple': ';45m',
                 'blue2': ';46m',
                 'gray': ';47m',
                 'black': ';48m'}
    txt = f'\33{tipo[tip]}{cor_letra[let]}{cor_fundo[fun]}'
    return txt


def titulo(txt, let='white'):
    cor_letra = {'red': '\033[0;31;48m',
                 'green': '\033[32m',
                 'yellow': '\033[33m',
                 'blue': '\033[34m',
                 'purprle': '\033[35m',
                 'blue2': '\033[36m',
                 'gray': '\033[37m',
                 'white': '\033[38m'}
    print('-' * 42)
    print(f'{cor_letra[let]}{txt.center(42)}', edit())
    print('-' * 42)


def menu(*ops):
    for c in range(0, len(ops)):
        print(f'{edit("bold", "yellow")}{c+1} - {edit("underline", "blue")}{ops[c]}{edit()}')
    txt = f'{edit("bold", "yellow")}Sua opção: {edit()}'
    return txt