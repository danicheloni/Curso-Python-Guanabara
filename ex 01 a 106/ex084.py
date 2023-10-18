pessoas = []
dado = []
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
     
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Continua? [S/N] ')).upper().strip()[0]
    if adicionar == 'N':
        break

print('-/-'*30)
print(f'Ao todo foram adicionadas {len(pessoas)} pessoas')

print(f'O menor peso foi {menor}kg pertencentas a: ', end= '')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

print(f'\nO maior peso foi {maior}Kg, pertencente a:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
