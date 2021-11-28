from time import sleep
def contadors(a, b, c):
    print('-' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for r in range(a, b+1, c):
        print(r, end=' ')
        sleep(1)
    print('FIM')
    print('-'*30)


def contadord(a, b, c):
    print('-' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for r in range(a, b-c, -c):
        print(r, end=' ')
        sleep(1)
    print('FIM')
    print('-'*30)


contadors(1, 10, 1)
contadord(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
q = int(input('Início: '))
w = int(input('Fim: '))
e = int(input('Passo: '))
if e <= 0:
    e *= (-1)
if e == 0:
    e = 1
if w < q:
    contadord(q, w, e)
else:
    contadors(q, w, e)
