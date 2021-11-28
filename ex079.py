valores = []
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
valores.sort()
print(f'Você digitou os valores {valores}')
