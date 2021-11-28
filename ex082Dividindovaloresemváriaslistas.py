valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    if valores.count(n) == 0:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continua = str(input('Quer continuar? [s/n] '))
    if continua == 'n':
        break
for c, v in enumerate(valores):
    if (v % 2) ==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
