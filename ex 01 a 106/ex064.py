n = int(input('Digite um número [999 para parar]: '))

sum = n
c = 1
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        sum = sum + n
        c += 1
print('Você digitou {} números e a soma é {}'.format(c, sum))
