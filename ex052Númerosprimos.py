n = int(input('N1: '))
tot = 0
for c in range(1, n+1):
    if (n % c) == 0:
        print('\033[31m{}\033[m'.format(c), end=' ')
        tot += 1
    else:
        print('\033[33m{}\033[m'.format(c), end=' ')
if tot == 2:
    print('PRIMO')
else:
    print('NÃO PRIMO')
