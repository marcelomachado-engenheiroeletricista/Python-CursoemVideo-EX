valores = []
while True:
    n = int(input('Digite um valor: '))
    if valores.count(n) == 0:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continua = str(input('Quer continuar? [s/n] '))
    if continua in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos')
print(f'Você digitou os valores {valores}')
if valores.count(5) != 0:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
