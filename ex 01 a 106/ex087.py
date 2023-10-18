matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número para [{l},{c}]:' ))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()

print("\o/" *13)
for l in matriz:
    for c in l:
        if c % 2 == 0:
            pares += c
print(f'A soma dos valores pares é {pares}.')

for l in range(0,3):
    coluna3 += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {coluna3}')

for c in range(0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
print("\o/" *13)