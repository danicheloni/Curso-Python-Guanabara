time = []
jogador = {}
gols_lista = []
saldo_gols = 0

while True:
    jogador["nome"] = str(input('Nome: '))

    partidas = int(input('Quantas partidas jogadas? '))
    for c in range(1, partidas+1):
        num_gol = int(input(f'   ->Quantos gols feitos na {c}ª partida? '))
        saldo_gols += num_gol
        gols_lista.append(num_gol)
    jogador["gols"] = gols_lista[:]
    gols_lista.clear()
    jogador["saldo"] = saldo_gols

    time.append(jogador.copy())
    
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Continua? [S/N] ')).upper().strip()[0]
    if adicionar == 'N':
        break
print('-=' * 25)
print(f'{"cod":<4} {"nome":<8} {"gols":<10} {"saldo":>20}')
print("-"*50)

for p in time:
    print(f'{time.index(p):<4}{p["nome"]:<10}{p["gols"]}{p["saldo"]:>15}')
print("-"*50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    else:
        print(f'Levantamento do Jogador {time[busca]["nome"]}')
        for c in time[busca]["gols"]:
            print(f'No jogo {c+1} fez {c} gols')

print('-=' * 25)
print('Obrigada por usar nosso APP')    