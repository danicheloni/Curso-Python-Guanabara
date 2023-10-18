print('-' *20)
print('     Fibonacci')
print('-' *20)

n = int(input('Quantos números você quer mostrar? ' ))
c = 0
t1= 0
t2=1

print('0 ⇢ 1 ⇢ ', end='')
while c < n-2:
    t3 = t1+t2
    c+=1
    t1 = t2
    t2 = t3
    print(' {}'.format(t3), end=' ⇢ ')
print('fim')

