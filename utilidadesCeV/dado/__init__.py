def leia_dinheiro(numero):
    validacao_de_ponto = 0
    numero.strip()
    for c in range(0, len(numero)):
        if numero[c] in ',' or numero[c] in '.':
            retorno = f'{numero[0:c]}.{numero[c+1:]}'
            validacao_de_ponto += 1
            if validacao_de_ponto > 1:
                print(f'\033[1;31;48m{numero} não é valido\nDigite apenas numeros reais!')
                exit()
        elif numero[c] not in '0123456789':
            print(f'\033[1;31;48m {numero} não é valido\nDigite apenas numeros reais!')
            exit()
    return float(retorno)