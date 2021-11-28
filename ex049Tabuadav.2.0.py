n = int(input('Digite um valor: '))
print('=' * 20)
print('A tabuada de {} é:'.format(n))
for c in range(1, 11):
    print('{} * {} = {}'.format(n, c, c*n))
print('=' * 20)
