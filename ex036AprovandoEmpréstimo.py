s = float(input('Digite seu salário: R$ '))
v = float(input('Qual o valor do imovel: R$ '))
a = float(input('Em quantos anos você quer pagar: '))
p = (v / (a * 12))
if p < (s * 0.3):
    print('Meus parabéns, fechamos negócio e você irá pagar R$ \033[34m{:.2f}\033[m por mês'.format(p))
else:
    print('\033[41mFoi mal, esse imovel não é para você\033[m')
