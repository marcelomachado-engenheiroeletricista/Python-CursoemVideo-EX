maior = 0
menor = 0
from datetime import date
for c in range(1, 8):
    n = int(input('Infome o ano de nascimento da pessoa {}: '.format(c)))
    idade = date.today().year - n
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} são maiores de idade e {} são menores de idade'. format(maior, menor))
