from random import randint
from time import sleep
n = randint(0, 5)
u = int(input('Adivinhe um nº de 0 a 5: '))
print('Tã tã tããããã .....')
sleep(2)
if n == u:
    print('Ahhhh miseravel, certoooo')
else:
    print('Se lascasti')
print('O nº correto era: {}'.format(n))
