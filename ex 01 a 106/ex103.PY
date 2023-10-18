def Ficha(jogador='<desconhecido>', gols='0'):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


#Programa Principal
nome = str(input('Nome do Jogador: '))
n_gols = str(input('Número de gols: '))
if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0

if nome.strip() == '':
    Ficha(gols=n_gols)
else:
    Ficha(nome, n_gols)

