from funcoesmenu import *
from funcoescadastro import *


menu = ['Ver Cadastrads', 'Cadastrar Pessoas', 'Sair']
arquivo = 'CadastroDeUsuários.txt'

if ArquivoExite(arquivo):
    print('Arquivo encontrado!')
else:
    print('Arquivo NÃO encontrado')
    CriarArquivo(arquivo)


while True:
    Menu(menu)
        
    try:
        opcao = int(input('Sua Opção: '))
    except ValueError:
        print('\033[31mERRO! Digite um número válido\033[m')
    else:
        if opcao == 1:
            VerCadastro(arquivo)
        elif opcao == 2:
            Cabecalho('NOVO CADASTRO')
            nome = str(input('Digite um nome: '))
            idade = LeiaInt('Digite a idade: ')
            Cadastrar(arquivo, nome, idade)
        elif opcao == 3:
            Sair()
            break
        else:
            print('\033[31mERRO! Digite um número válido\033[m')