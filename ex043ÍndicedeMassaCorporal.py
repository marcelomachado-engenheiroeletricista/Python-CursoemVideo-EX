a = float(input('Qual sua altura em m: '))
p = float(input('Qual seu peso em Kg: '))
imc = (p/(a ** 2))
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está: NO PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está: COM SOBREPESO')
elif 30 <= imc <= 40:
    print('Você está: COM OBESIDADE')
elif imc > 40:
    print('Você está: COM OBESIDADE MÓRBIDA')
