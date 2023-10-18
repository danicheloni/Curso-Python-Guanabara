num = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))

c = 1
total = 0
acres = 10

while acres != 0:
    total = total + acres
    while c < total:
        pa = raz * c + num
        print('{}'.format(pa), end='')
        print(' ⇢ ' if c<(total) else ' = ', end="")
        c += 1
    print('Pausa')
    acres = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada com {} termos'.format(total))