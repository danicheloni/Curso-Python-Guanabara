valores = []
while True:
    valores.append(int(input('Digite um número: ')))

    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Continua? [S/N] ')).strip().upper()[0]
    if adicionar == 'N':
        break
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são: {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O número 5 está na lista!')