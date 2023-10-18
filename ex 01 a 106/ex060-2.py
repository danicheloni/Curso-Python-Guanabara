n = int(input('Digite um número para encontrar seu fatorial: '))
print('Calculando o fatorial de {}'.format(n))

c = n
f = 1

while c > 0:
    print('{}'.format(c), end='')
    print(' ⇢ ' if c>1 else ' =', end='')
    f= f*c
    c-=1
print(' {}'.format(f))