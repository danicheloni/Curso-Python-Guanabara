valores = list()
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))

max = max(valores)
min = min(valores)

print(f'o MAIOR valor foi {max} nas posições ', end='')
for v in range(0, len(valores)):
    if valores[v] == max:
        print(f'{v}', end='... ')

print(f'\no MENOR valor encontrado foi {min} nas posições ', end='')
for v in range(0,len(valores)):
    if valores[v] == min:
        print(f'{v}', end='... ')
