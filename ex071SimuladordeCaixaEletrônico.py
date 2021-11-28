valor = int(input('Valor do saque: '))
'''while True:
    if valor >= 50:
        cinquenta = valor // 50
        print(f'Total de notas de R$50,00: {cinquenta}')
        if (valor % 50) == 0:
            break
    if (valor % 50) >= 20:
        vinte = (valor % 50) // 20
        print(f'Total de notas de R$20,00: {vinte}')
        if ((valor % 50) % 20) == 0:
            break
    if ((valor % 50) % 20) >= 10:
        dez = ((valor % 50) % 20) // 10
        print(f'Total de notas de R$10,00: {dez}')
        if (((valor % 50) // 20) % 10) == 0:
            break
    if (((valor % 50) % 20) % 10) >= 1:
        um = (((valor % 50) % 20) % 10) // 1
        print(f'Total de notas de R$1,00 é: {um}')
        break
print('Volte sempre')'''
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('FIM')

