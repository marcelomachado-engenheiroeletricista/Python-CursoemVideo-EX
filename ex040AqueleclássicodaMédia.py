n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua médeia é: {:.1f} \n\033[31mREPROVADO\033[m '.format(m))
elif m >= 5 and m <= 6.9:
    print('Sua médeia é: {:.1f} \n\033[33mRECUPERAÇÃO\033[m '.format(m))
else:
    print('Sua médeia é: {:.1f} \n\033[34mAPROVADO\033[m '.format(m))
