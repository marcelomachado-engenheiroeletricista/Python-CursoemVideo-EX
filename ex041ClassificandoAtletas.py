from datetime import date
a = int(input('Ano de nascimento: '))
b = date.today().year - a
print('O atleta tem {} anos'.format(b))
if b <= 9:
    print('Atleta MIRIM')
elif 9 < b <= 14:
    print('Atleta INFANTIL')
elif 14 < b <= 19:
    print('Atleta JUNIOR')
elif 19 < b <= 20:
    print('Atleta SÊNIOR')
elif b > 20:
    print('Atleta MASTER')
