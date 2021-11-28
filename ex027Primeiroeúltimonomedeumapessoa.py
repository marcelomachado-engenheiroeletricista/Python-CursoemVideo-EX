name = str(input('Digite seu nome completo: ')).strip()
separa = name.split()
print('Seu primeiro nome é: {}'.format(separa[0]))
print('Seu ultimo nome é: {}'.format(separa[len(separa)-1]))
