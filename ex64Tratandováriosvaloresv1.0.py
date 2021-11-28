u = n = c = 0
while u != 999:
    u = int(input('Digite um valor: '))
    if u != 999:
        n = n + u
        c = c + 1
print('Vc digitou {} números cuja a soma é {}'.format(c, n))
