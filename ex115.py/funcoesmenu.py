def Linha(tam=42):
    return '-' * tam


def Cabecalho(msg):
    print(Linha())
    print(msg.center(42))
    print(Linha())


def ImprColorido(msg1, msg2):
    print(f'\033[33m{msg1}\33[m - \033[34m{msg2}\033[m')

def Menu(lista):
    Cabecalho('Menu Principal')
    c = 1
    for item in lista:
        ImprColorido(c, item)
        c+=1
    print(Linha())


def Sair():
    Cabecalho('Saindo do sistema... Até logo!')


def LeiaInt(msg):
    while True:
        try:
            n_int = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        else:
            return n_int