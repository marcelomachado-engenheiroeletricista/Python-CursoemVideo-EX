def moeda(a=0, sit=False):
    n = a
    if sit:
        n = f'R${n}'
    return n


def metade(a=0, sit=False):
    n = a / 2
    return n if sit is False else moeda(a, True)


def dobro(a=0, sit=False):
    n = a * 2
    if sit:
        n = f'R${n}'
    return n


def aumentar(a=0, p=0, sit=False):
    per = a + (a * (p / 100))
    if sit:
        per = f'R${per}'
    return per


def diminuir(a=0, p=0, sit=False):
    per = a - (a * (p / 100))
    if sit:
        per = f'R${per}'
    return per