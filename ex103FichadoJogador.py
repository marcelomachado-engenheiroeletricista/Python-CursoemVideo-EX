def ficha(j='<desconhecido>', gol=0):
    print(f'O jogador {j} fez {g} gols.')


n = str(input("Nome do Jogador: "))
g = str(input("Número de gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
