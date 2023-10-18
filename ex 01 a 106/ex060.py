n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c>1 else ' = ', end="")
    f = f*c
    c -= 1

print('O fatorial de {} é {}'.format(n, f))

for c in range(n, 0, -1):
    f = f*c
print(f)