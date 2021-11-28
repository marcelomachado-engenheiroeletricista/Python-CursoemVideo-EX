from random import randint
n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Sorteados {n}')
maior = menor = cont = 0
for c in n:
    if cont == 0:
        maior = menor = c
        cont += 1
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'Maior: {maior}. Menor: {menor}')
