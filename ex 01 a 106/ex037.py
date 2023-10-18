num = int(input('Digite um número inteiro: '))
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print(bin(num)[2:])
elif escolha == 2:
    print(oct(num)[2:])
elif escolha == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida, tente novamente!')