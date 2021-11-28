def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m²')


print('Controle de IPTU')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
