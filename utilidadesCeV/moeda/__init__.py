def moeda(din):
    retorno = str(f'R$ {din:.2f}')
    return retorno


def aumentar(n, porcentagem, contabil=False):
    if contabil:
        return moeda(n + n * (porcentagem/100))
    return n + n * (porcentagem/100)


def diminuir(n, porcentagem, contabiil=False):
    if contabiil:
        return moeda(n - n * (porcentagem / 100))
    return n - n * (porcentagem / 100)


def dobro(n, contabil=False):
    if contabil:
        return moeda(n * 2)
    return n * 2


def metade(n, contabil=False):
    if contabil:
        return moeda(n / 2)
    return n / 2


def resumo(num, aumentar_loc, diminuir_loc):
    print(f'{"=" * 45}\n'
          f'Aumentando {aumentar_loc} % de {moeda(num)}:....{aumentar(num, aumentar_loc, contabil=True)}\n'
          f'Diminuindo {diminuir_loc} % de {moeda(num)}:....{diminuir(num, diminuir_loc, contabiil=True)}\n'
          f'O dobro de {moeda(num)}:............{dobro(num, contabil=True)}\n'
          f'Metade de {moeda(num)}:.............{metade(num, contabil=True)}\n'
          f'{"=" * 45}')