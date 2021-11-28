'''c = 1
u = 1
n = int(input('N1: '))
q = n
while c != n:
    if c == 1:
        u = (q - 1) * q
        c = c + 1
        q = q - 2
    else:
        u = u * q
        q = q - 1
        c = c + 1
print('O fatorial de {} é {}'.format(n, u))'''

from math import factorial
n = int(input('N1: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
