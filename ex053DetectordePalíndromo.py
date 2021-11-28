frase = str(input('FRASE: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]


'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('Palíndromo')
else:
    print('Não Palíndromo')