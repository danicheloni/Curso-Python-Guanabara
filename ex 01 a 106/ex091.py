from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
jogo = {'jogador1' : randint(1,6),
        'jogador2' : randint(1,6),
        'jogador3' : randint(1,6),
        'jogador4' : randint(1,6)}

for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} pontos')
    sleep(0.5)
print('-=' * 15)



"""jogada = {}
jogo = []
ranking = {}

print('Valores Sorteados:')
for c in range(1, 5):
    jogada["jogador"] = c
    jogada["num"] = randint(1,6)
    print(f'O jogador{c} tirou {jogada["num"]}')
     jogo.append(jogada.copy())    
    c += 1

ranking = sorted


print('-=' * 15)
print(jogo)"""


#print(f'jogador{c} tirou {num} no dado')