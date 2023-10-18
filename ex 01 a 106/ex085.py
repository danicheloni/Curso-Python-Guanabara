lista = [[], []]

for cont in range(1,8):   
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
       lista[0].append(num)
    else:
       lista[1].append(num)
print('-=' * 25)
print(f'Valores pares digitados {sorted(lista[0])}')
print(f'Valores impares digitados {sorted(lista[1])}')
