import random
c = ['pedra', 'papel', 'tesoura']
c1 = random.choice(c)
u = str(input('JO-KEN-PÔ: '))

if u == 'pedra' and c1 == 'pedra':
    print('EMPATE')
elif u == 'papel' and c1 == 'papel':
    print('EMPATE')
elif u == 'tesoura' and c1 == 'tesoura':
    print('EMPATE')
elif u == 'tesoura' and c1 == 'papel':
    print('YOU WIN')
elif u == 'tesoura' and c1 == 'pedra':
    print('YOU LOSE')
elif u == 'papel' and c1 == 'pedra':
    print('YOU WIN')
elif u == 'papel' and c1 == 'tesoura':
    print('YOU LOSE')
elif u == 'pedra' and c1 == 'tesoura':
    print('YOU WIN')
elif u == 'pedra' and c1 == 'papel':
    print('YOU LOSE')
