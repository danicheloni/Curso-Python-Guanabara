notas = []
dados = []

while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(float(input('Digite uma nota: ')))
    dados.append(float(input('Digite outra nota: ')))
    notas.append(dados[:])
    dados.clear()

    adicionar = ' '
    while adicionar not in 'SN':
        adicionar  = str(input('Continua? [S/N]')).strip().upper()[0]
    if adicionar == 'N':
        break
print('-='*30)

print(f'{"N":<4} {"Nome":<10} {"Média":>8}')
for p in notas:
    media = (p[1]+p[2])/2
    
    print(f'{notas.index(p):<4} {p[0]:<10} {media:>8}')
print('-='*30)

mostrar = int(input('Mostrar notas de qual aluno? '))
print(f'As notas de {notas[mostrar][0]} são : {notas[mostrar][1], notas[mostrar][2]}')
        