def LeiaInt(a):
    n = input(a)
    while n.isnumeric() == False:     
        print('ERRO! Digite um número inteiro válido')
        n = input(a)
      
    if n.isnumeric():
        return n
    

#Programa Principal
n = LeiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')