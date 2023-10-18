n = int(input('Digite um número: '))
total = 0
#msg = ('O número {} foi divisivel {} vezes.'.format(n, d))


for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=" ")
        total +=1
    else:
        print('\033[31m', end=" ")
    print(c, end=" ")

print('\n\033[mO número {} foi divisivel {} vezes'.format(n, total))

if total == 2:
    print('O número {} é PRIMO'.format(n))
else:
    print('O número {} não é primo'.format(n))
    