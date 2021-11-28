exp = str(input('Digite uma expressão: '))
if ((exp.count('(') + exp.count(')')) % 2) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
