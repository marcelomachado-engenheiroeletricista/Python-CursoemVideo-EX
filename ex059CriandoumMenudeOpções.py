u = 0
while u != 5:
    print('Digite dois valores:')
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    u = int(input('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa \nEscolha uma das opções acima:'))
    if u == 1:
        n = n1 + n2
        print('O valor da soma é {}'.format(n))
    if u == 2:
        n = n1 * n2
        print('O valor da multiplicação é {}'.format(n))
    if u == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    if u == 4:
        u = 0
print('FIM - VOLTE SEMPRE')
