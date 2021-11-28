n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 >n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor é {} e o maior é {}'.format(menor, maior))

'''if n1 > n2:
    if n1 > n3:
        print('O maior é {}'.format(n1))
if n2 > n1:
    if n2 > n3:
        print('O maior é {}'.format(n2))
if n3 > n1:
    if n3 > n2:
        print('O maior é {}'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('O menor é {}'.format(n1))
if n2 < n1:
    if n2 < n3:
        print('O menor é {}'.format(n2))
if n3 < n1:
    if n3 < n2:
        print('O menor é {}'.format(n3))'''
