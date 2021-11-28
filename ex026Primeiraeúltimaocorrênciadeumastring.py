frase = str(input('Digite uma frase: ')).strip()
print('Número de "a" é: ', frase.upper().count('A'))
print('O primeiro "a" aparece em: {}'.format(frase.upper().find('A') + 1))
print('O ultimo"a" aparece em: {}'.format(frase.upper().rfind('A') + 1))
