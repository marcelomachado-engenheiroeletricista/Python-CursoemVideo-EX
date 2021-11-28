listagem = ('Lápis', 1.75,
            'Caderno', 2,
            'Transferidor', 5.4)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
