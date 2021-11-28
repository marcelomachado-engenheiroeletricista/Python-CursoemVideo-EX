num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}º')
else:
    print('O 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')
