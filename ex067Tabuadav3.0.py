n = 0
c = 1
while True:
    print('-' * 20)
    n = int(input('Tabuada de qual valor: '))
    print('-' * 20)
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{c} X {n} = {c*n}')
            c += 1
print('Fim')