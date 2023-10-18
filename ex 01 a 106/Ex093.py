jogador = {}
gols_lista = []
saldo = 0

jogador["nome"] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))

for c in range(1, partidas+1):
    num_gol = (int(input(f'   Quantos gols na partida {c}? ')))
    gols_lista.append(num_gol)
    saldo += num_gol
jogador["gols"] = gols_lista
jogador["saldo"] = saldo
print('-=' * 30)

print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(1, partidas+1):
    print(f'   => Na partida {c}, fez {gols_lista[c-1]} gols.')
print(f'No total de {saldo} gols')