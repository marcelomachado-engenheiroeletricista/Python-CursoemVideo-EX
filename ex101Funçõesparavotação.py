def voto(ano):
    from datetime import date
    a = date.today().year - ano
    if 18 <= a < 65:
        return f'Com {a}: VOTO OBRIGATÓRIO.'
    if a < 16:
        return f'Com {a} anos: VOTO PROIBIDO.'
    if 16 <= a < 18 or a >= 65:
        return f'Com {a} anos: VOTO OPCIONAL.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
