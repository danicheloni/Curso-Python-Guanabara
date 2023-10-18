print('='*40)
print('         10 TERMOS DE UMA PA')
print('='*40)

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for c in range(0, 10):
    print('{} - '.format(r*c+n), end= "")
print('ACABOU')