s = 0
q = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        q += 1
        s += c
print('a soma é {} e foram feitos {}'.format(s, q))
print('Acabou')
