from datetime import date
a = int(input('Qual seu ano de nascimento: '))
b = date.today().year - a
if b > 18:
    print('Você capinou a {} anos'.format(b - 18))
elif b < 18:
    print('Calma rapaizinho, ainda falta {} anos para você capinar'.format(18 - b))
else:
    print('GAFANHOTO, esse é seu ano de capinar')
