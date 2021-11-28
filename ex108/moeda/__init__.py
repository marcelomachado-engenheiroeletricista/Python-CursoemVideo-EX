def metade(a=0):
    n = a / 2
    return n


def dobro(a=0):
    n = a * 2
    return n


def aumentar(a=0, p=0):
    per = a + (a * (p / 100))
    return per


def diminuir(a=0, p=0):
    per = a - (a * (p / 100))
    return per

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

