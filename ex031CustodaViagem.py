v = float(input('Digite quantos KM irá viajar: '))
if v < 200:
    print('Sua viagem irá custar R${}'.format(v * 0.5))
else:
    print('Sua viagem irá custar R${}'.format(v * 0.45))
