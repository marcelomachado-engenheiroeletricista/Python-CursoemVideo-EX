def moeda(a=0, sit=False):
    n = a
    if sit:
        n = f'R${n}'
    return n


def metade(a=0, sit=False):
    n = a / 2
    if sit:
        n = f'R${n}'
    return n


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

def resumo(a=0, b=10, c=5):

    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'Preço analisado: \t{moeda(a, True)}')
    print(f'Dobro do preço: \t{dobro(a, True)}')
    print(f'Metade do preço: \t{metade(a, True)}')
    print(f'{b}% de aumento: \t{aumentar(a, b, True)}')
    print(f'{c}% de redução: \t{diminuir(a, c, True)}')
    print('-' *30)
