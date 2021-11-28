c = 0
s = 0
q = 0
maior = 0
menor = 0
while q != 'N':
    u = int(input('Digite um valor: '))
    s = s + u
    c = c + 1
    if c == 1:
        maior = menor = u
    else:
        if u > maior:
            maior = u
        if u < menor:
            menor = u
    q = str(input('Continuar [S/N]: ').upper())
print('A soma é {}, a média é {:.2f}, o maior {} e o menor {}.'.format(s, (s / c), maior, menor))
