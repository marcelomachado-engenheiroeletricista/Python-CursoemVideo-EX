def escreva(txt):
    n = (4 + len(txt))
    print(f'-' *n)
    print(f'{txt:^{n}}')
    print(f'-' *n)
    print()


escreva('ola')
escreva('Marcel')