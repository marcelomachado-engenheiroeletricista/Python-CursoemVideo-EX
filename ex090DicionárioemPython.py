aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
print(f'Situação é igual a {aluno["situação"]}')
