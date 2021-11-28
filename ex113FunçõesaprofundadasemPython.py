def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digie um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrade dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digie um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;33mNada digitado.\033[m')
            return 0
        else:
            return f



n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n}.')
print(f'Você acabou de digitar o número {f}.')
