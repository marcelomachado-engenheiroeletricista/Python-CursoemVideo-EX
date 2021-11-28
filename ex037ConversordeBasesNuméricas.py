num = int(input('N1: '))
print('''Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} para B. é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} para Oc. é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} para Hex. é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
