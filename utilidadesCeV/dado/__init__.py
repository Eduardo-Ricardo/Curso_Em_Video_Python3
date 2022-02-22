def leia_dinheiro(numero):
    validacao_de_ponto = 0
    numero.strip()
    for c in range(0, len(numero)):
        if numero[c] in ',' or numero[c] in '.':
            retorno = f'{numero[0:c]}.{numero[c + 1:]}'
            validacao_de_ponto += 1
            if validacao_de_ponto > 1:
                print(f'\033[1;31;48m{numero} não é valido\nDigite apenas numeros reais!')
                exit()
        elif numero[c] not in '0123456789':
            print(f'\033[1;31;48m {numero} não é valido\nDigite apenas numeros reais!')
            exit()
    return float(retorno)


def leia_int(txt):
    from Curso_Em_Video_Python3.utilidadesCeV.edit import titulo, edit
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print(f'\n{edit("bold", "red")}Erro: {edit("underline", "red")}Digite um valor valido{edit()}\n')
        except KeyboardInterrupt:
            print(f'\n\n{edit("bold", "red")}Erro: {edit("underline", "red")}'
                  f'O usuario preferiu não digitar um valor{edit()}\n')
        else:
            return numero


def leia_float(txt):
    while True:
        try:
            numero = float(input(txt))
        except (ValueError, TypeError):
            print('Erro')
        except KeyboardInterrupt:
            print('Erro')
        else:
            return numero

