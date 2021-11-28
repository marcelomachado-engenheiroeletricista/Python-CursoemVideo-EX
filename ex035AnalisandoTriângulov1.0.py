a = float(input('N1: '))
b = float(input('N2: '))
c = float(input('N3: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('SIM, formam um triângulo')
else:
    print('NÃO formam um triãngulo')

'''if n1 < (n2 + n3):
    if n2 < (n1 + n3):
        if n3 < (n1 + n2):
            print('Sim é um triângulo')

if n2 < (n1 + n3):
    if n3 < (n1 + n2):
        if n1 < (n3 + n2):
            print('Sim é um triângulo')

if n3 < (n1 + n2):
    if n1 < (n3 + n2):
        if n2 < (n3 + n1):
             print('Sim é um triângulo')'''
