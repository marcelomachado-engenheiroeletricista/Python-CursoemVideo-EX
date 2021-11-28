maior = 0
menor = 0
valores = []
for c in range(0, 5):
    valores.insert(c, int(input(f'Digite na posição {c}: ')))
    if c == 0:
        maior = valores[0]
        menor = valores[0]
    else:
        if valores[c] >= maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Você digitou {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
