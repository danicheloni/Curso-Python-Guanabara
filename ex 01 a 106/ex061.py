num = int(input('Digite um número: '))
raz = int(input('Digite a razão: '))

c = 0

while c <10:
    pa = raz*c + num
    print('{}'.format(pa), end='')
    print(' - ' if c<10 else ' = ', end="")
    c += 1
print('Fim')