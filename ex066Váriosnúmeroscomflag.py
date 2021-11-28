n = s = c = 0
while True:
    n = int(input('Digite um valor, ou 999 para parar: '))
    if n == 999:
        break
    else:
        s += n
        c += 1
print(f'A soma é {s} com os {c} nº digitados')
