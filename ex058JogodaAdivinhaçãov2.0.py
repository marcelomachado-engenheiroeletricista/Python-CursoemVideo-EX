from random import randint
n = randint(0, 10)
c = 1
u = int(input('Adivinhe um nº de 0 a 10: '))
while u != n:
    c = c + 1
    print('Se lascasti')
    if n > u:
        print('É MAIS QUE ISSO CABEÇA')
    else:
        print('MENOS MEU FILHO')
    u = int(input('Adivinhe um nº de 0 a 10: '))

print('Ahhhh miseravel, certoooo em {} tentativas'.format(c))
