from time import sleep
def maior(* num):
    mai = 0
    for n in num:
        if n > mai:
            mai = n
    print('-' *30)
    print('Analisando valores...')
    sleep(1)
    print(f'Temos {num} ou seja, {len(num)} valores')
    print(f'O maior valor é {mai}')
    print('-' * 30)


maior(1, 2, 8, 1, 0)
maior(6)
maior(10, 1, 0, 100, 1)
maior(-1000, 1)
maior()