lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 1:
        impares.append(num)
    else:
        pares.append(num)
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Acrescentar mais números: [S/N] ')).strip().upper()[0]
    if adicionar == 'N':
        break

print('-='*30)
print(f'Você digitou os números: {lista}')
print(f'Os números pares foram: {pares}')
print(f'Os números ímpares foram: {impares}')
