from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = (date.today().year) - (int(input('Ano de Nascimento: ')))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ((date.today().year) - (pessoa['idade']))) + 35
print(f'O nome é {pessoa["nome"]}')
print(f'Ele(a) tem {pessoa["idade"]} anos')
if pessoa['ctps'] != 0:
    print(f'Sua CTPS é {pessoa["ctps"]}')
    print(f'Foi contratato em {pessoa["contratação"]}')
    print(f'Seu salário é R${pessoa["salario"]}')
    print(f'Irá se aposentar com {pessoa["aposentadoria"]} anos')
print(pessoa)
