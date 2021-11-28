p = float(input('Qual o preço do produto: R$ '))
c = str(input('O pagamento será a VISTA ou a PRAZO: '))
if c == 'prazo':
    z = int(input('Em 2x ou 3x: '))
    if z == 2:
        print('O valor final não tem desconto então será de R$ {}'.format(p))
    elif z == 3:
        print('O valor final tem aumento de 20% então será de R$ {}'.format(p * 1.3))

if c == 'vista':
    m = str(input('O pagamento será em DINHEIRO, CHEQUE, ou CARTÃO: '))
    if m == 'dinheiro' or m == 'cheque':
        print('O valor final tem 10% de desconto então será de R$ {}'.format(p * 0.9))
    elif m == 'cartão':
        print('O valor final tem 5% de desconto então será de R$ {}'.format(p * 0.95))
