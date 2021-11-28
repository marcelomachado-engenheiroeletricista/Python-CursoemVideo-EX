menor = maior = 0
nomemaior = list()
nomemenor = list()
pessoas = list()
dado = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    if dado[1] >= maior:
        maior = dado[1]
        nomemaior.append(dado[0])
    if menor == 0:
        menor = dado[1]
        nomemenor.append(dado[0])
    else:
        if dado[1] <= menor:
            menor = dado[1]
            nomemenor.append(dado[0])
    dado.clear()
    continua = str(input('Quer continuar? [s/n] '))
    if continua not in 'NnSs':
        continua = str(input('Quer continuar? [s/n] '))
    if continua in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {nomemaior}.')
print(f'O menor peso foi de {menor}Kg. Peso de {nomemenor}.')
