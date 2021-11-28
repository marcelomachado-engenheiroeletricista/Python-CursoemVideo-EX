s = float(input('Salário atual: '))
if s >= 1250:
    print('O aumento será de R${:.2f}'.format(s * 1.1))
else:
    print('O aumento será de R${:.2f}'.format(s * 1.15))
