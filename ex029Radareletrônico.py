import emoji

v = float(input('Qual sua velocidade: '))
if v > 80.0:
    m = (v - 80) * 7
    print(emoji.emojize('Você foi multado em R${:.2} :rage:'.format(m), use_aliases=True))
else:
    print(emoji.emojize('Tenha uma boa viagem! :smiley:', use_aliases=True))
