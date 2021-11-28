'''matriz = list()
pares = 0
impares = 0
for c in range(0, 3):
    for l in range(0, 3):
        n = int(input(f'Digite um valor para[{c}. {l}]: '))
        matriz.append(n)
        if (n % 2) == 0:
            pares += n
        else:
            impares += n
if matriz[3] > matriz[4] and matriz[3] > matriz[5]:
    maior = matriz[3]
if matriz[4] > matriz[3] and matriz[4] > matriz[5]:
    maior = matriz[4]
if matriz[5] > matriz[3] and matriz[5] > matriz[4]:
    maior = matriz[5]
print('-=' * 30)
print(f'[ {matriz[0]} ][ {matriz[1]} ][ {matriz[2]} ]')
print(f'[ {matriz[3]} ][ {matriz[4]} ][ {matriz[5]} ]')
print(f'[ {matriz[6]} ][ {matriz[7]} ][ {matriz[8]} ]')
print('-=' * 30)
print(f'A Soma dos valores pares é {pares}')
print(f'A soma dos valores impares é {impares}')
print(f'A soma dos calores da terceira coluna é {matriz[2] + matriz[5] + matriz[8]}')
print(f'A soma dos calores da terceira coluna é {matriz[2] + matriz[5] + matriz[8]}')
print(f'O maior valor da segunda linha é {maior}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')