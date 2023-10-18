n = int(input('Digite um número para ver sua tabuada: '))

count = 0
for c in range(0,11):
    print('{} x {:0} = {}'.format(n, c, n*c))
print('fim')