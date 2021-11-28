'''todos = list()
impares = list()
pares = list()
for c in range(0, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if (n % 2) == 0:
        pares.append(n)
    else:
        impares.append(n)
impares.sort()
pares.sort()
todos.append(pares[:])
todos.append(impares[:])
print(todos)'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if (valor % 2) == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares foram {num[0]}')
print(f'TOdos os valores ímpares foram {num[1]}')
