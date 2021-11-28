from datetime import date
ano = int(input('Digite seu ano ou 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
d = ano % 4
if d == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano é BISSEXTO')
else:
    print('Esse ano não é BISSEXTO')
