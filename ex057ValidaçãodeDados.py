s = 1
while s != 'M':
    s = str(input('Qual o seu SEXO [M/F]: ').strip().upper())
    if s == 'F':
        print('Tu é GURIA')
        s = 'M'
    else:
        if s == 'M':
            print('Tu é GURI')
print('FIM')
