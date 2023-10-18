from random import randint
#numero = randint(1,5)
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(tupla)

print(f'O Maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')
