import math
n = float(input('Ângulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('Seno: {}, Cosseno: {}, Tangente: {}'.format(s, c, t))
