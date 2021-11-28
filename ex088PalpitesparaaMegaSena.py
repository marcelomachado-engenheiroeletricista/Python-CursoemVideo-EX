from random import randint
from time import sleep
print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)
n = int(input('Quantos jofos você quer que eu sorteire: '))
jogo = list()
dado = list()
for c in range(0, n):
    for r in range(0, 6):
        while True:
            n = randint(1, 60)
            if dado.count(n) == 0:
                dado.append(n)
                break
    dado.sort()
    jogo.append(dado[:])  #[:] para criar copia
    dado.clear()
    print(f'Jogo {c+1}: {jogo[c]}')
    sleep(1)
