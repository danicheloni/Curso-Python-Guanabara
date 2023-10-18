n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
nove = pares = 0



print('Você digitou os números: ', end=' ')
for n in tupla:
    print(n, end=' ')

print(f'\nO número 9 aparece {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 aparece a primeira vez na posição {tupla.index(3)}')

print('Os números pares digitados foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')