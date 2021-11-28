from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(ca, co)
print('A hypotenusa é {}'.format(h))
