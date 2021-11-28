a = float(input('N1: '))
b = float(input('N2: '))
c = float(input('N3: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('SIM, formam um triângulo', end=' ' )
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('NÃO formam um triãngulo')
