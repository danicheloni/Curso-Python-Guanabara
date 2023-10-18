def LeiaInt(msg):
    while True:
        try:
            n_int = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        else:
            return n_int

def LeiaFloat(msg):
    while True:
        try:
            n_float = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido!\033[m')
            continue
        else:
            return n_float


#Programa Principal
n = LeiaInt('Digite um número inteiro: ')
r = LeiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {r}.')

