import random
from time import sleep

print(f'-'*30)
print(f'      JOGAR NA MEGASENA')
print(f'-'*30)

n = int(input('Quantos jogos você quer gerar? '))

print('-=' * 3, end='')
print('SORTEANDO 10 JOGOS', end='')
print('-=' * 3)

for i in range(0,n):
    jogo = range(0,60)
    print(f'Jogo {i+1}: ', end='')
    print(sorted(random.sample(jogo, 6)))
    sleep(0.5)

print('-='*15)

