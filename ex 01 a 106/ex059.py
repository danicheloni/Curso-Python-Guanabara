n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
maior = 0

while opcao != 5:
    print('''Essas são as suas opções: 
          [1] SOMAR
          [2] MULTIPLICAR
          [3] MAIOR
          [4] DIGITAR NOVOS NÚMEROS
          [5] SAIR''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma de {} e {} é: {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('Informe os número novamente')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Obrigada por usar nosso programa!')
    else:
        print('Opção Inválida')
print('Fim do Programa')





