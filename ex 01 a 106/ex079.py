lista = []


while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Numero repetido. Não Vou adicionar!')
    
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Acrescentar mais números: [S/N] ')).strip().upper()[0]
    if adicionar == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(lista)}')