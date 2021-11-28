import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
Lista = [a1, a2, a3, a4]
random.shuffle(Lista)
print('A ordem é:')
print(Lista)
