def moeda(din):
    retorno = str(f'R$ {din:.2f}')
    return retorno


def aumentar(n, porcentagem, contabil=False):
    if contabil:        return moeda(n + n * (porcentagem/100))
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