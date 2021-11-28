jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, p):
    n = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(n)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
print(jogador)
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for r in range(0, len(gols)):
    print(f'   => Na partida {r+1} ele fez {gols[r]} gols')
print(f'Foi um total de {jogador["total"]} gols')


#sum(gols) - Somar dentro da lista.