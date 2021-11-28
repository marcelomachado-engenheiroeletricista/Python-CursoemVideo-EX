maior = 0
menor = 0
maiornome = 0
menornome = 0
contproduto = 0
maisdemil = 0
total = 0
print('CADASTRE A VENDA')
while True:
    produto = str(input('Nome do produto: ').strip())
    preco = float(input('Preço: R$'))
    if contproduto == 0:
        maior = menor = preco
        menornome = maiornome = produto
    else:
        if preco > maior:
            maior = preco
            maiornome = produto
        if preco < menor:
            menor = preco
            menornome = produto
    if preco > 1000:
        maisdemil += 1
    total += preco
    contproduto += 1
    new = ' '
    while new not in 'SsNn':
        new = str(input('Cadastrar novo: [S/N] '))
    if new in 'Nn':
        break
print('{:=^40}'.format(' Fim da Compra '))
print(f'O valor total da compra é de {total:.2f}')
if maisdemil > 0:
    print(f'Foram comprados {maisdemil} produtos de mais e R$1000,00')
if contproduto > 1:
    print(f'O produto mais barato foi {menornome} que custa R${menor}')
    print(f'O produto mais caro foi {maiornome} que custa R${maior}')
