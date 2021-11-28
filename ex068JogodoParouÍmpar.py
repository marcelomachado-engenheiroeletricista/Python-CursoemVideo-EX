from random import randint
cont = 0
while True:
    c = randint(0, 5)
    #n = int(input('Valor: '))
    v = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
    n = int(input('Valor: '))
    while v not in 'PI':
        v = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
    g = (n+c) % 2
    if g == 0:
        if v == 'P':
            print(f'Você jogou {n} e eu {c}. A soma é {(n + c)} que é PAR')
            print('GANHOU')
            cont += 1
        else:
            print(f'Você jogou {n} e eu {c}. A soma é {(n + c)} que é PAR')
            print('PERDEU')
            break
    if g != 0:
        if v == 'I':
            print(f'Você jogou {n} e eu {c}. A soma é {(n + c)} que é ÍMPAR')
            print('GANHOU')
            cont += 1
        else:
            print(f'Você jogou {n} e eu {c}. A soma é {(n + c)} que é ÍMPAR')
            print('PERDEU')
            break
print(f'GAME OVER! Você ganhou {cont} vezes')
