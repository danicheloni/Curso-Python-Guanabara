print('-=' *20)
print('         Gerador de PA')
print('-=' *20)

n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))

c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c < total:
        pa = r*c + n
        print('{}'.format(pa), end='')
        print(' ⇢ ' if c<total else '=', end='')
        c+=1
    print('Pausa')
    mais = int(input('Quantos termos mais?'))
print('PA finalizada com {} numeros'.format(total))