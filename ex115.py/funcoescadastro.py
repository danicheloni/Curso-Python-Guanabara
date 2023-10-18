from funcoesmenu import *

def ArquivoExite(arq):
    try:
        a = open(arq, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {arq} criado com sucesso')


def VerCadastro(arq):
    try: 
        a = open(arq, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        Cabecalho('CADASTRO DE PESSOAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())

    finally:
        a.close()
    
    


def Cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro')
        else:
            print(f'\033[32mCadastro de {nome} feito com sucesso\033[m')
            a.close()
