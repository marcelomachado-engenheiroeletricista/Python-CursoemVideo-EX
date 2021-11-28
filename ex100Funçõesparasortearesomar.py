from random import randint
def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(0, 10))
    print(f'Sorteando 5 valores da Lista: {lst}', end='')
    print(f' PRONTO!')

def somapar(lst):
    pares = 0
    for c in range(0, len(lst)):
        if lst[c] % 2 == 0:
            pares += lst[c]
    print(f'Somando os valores pares de {lst}, temos {pares}')


lista = list()
sorteia(lista)
somapar(lista)