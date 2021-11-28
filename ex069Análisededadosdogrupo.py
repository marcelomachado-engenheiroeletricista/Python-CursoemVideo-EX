homens = 0
mulheres = 0
adultos = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    '''if idade != int:
        idade = int(input('Idade: '))'''
    sexo = str(input('SEXO: [M/F] ').strip().upper()[0])
    while sexo not in 'MF':
        sexo = str(inputjt('SEXO: [M/F] ').strip().upper()[0])
    print('-' * 30)
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1
    if idade >= 18:
        adultos += 1
    new = str(input('Cadastrar novo: [S/N] '))
    while new not in 'SsNn':
        new = str(input('Cadastrar novo: [S/N] '))
    if new in 'Nn':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Adultos: {adultos}')
print(f'Homenes: {homens}')
print(f'Mulheres: {mulheres}')
