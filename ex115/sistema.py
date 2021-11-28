from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta ==1:
        #Opção de criar um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)
