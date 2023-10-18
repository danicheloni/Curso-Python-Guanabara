lista = []
for pessoa in range(1, 6):
    peso = str(input('Digite o peso: '))
    lista += peso
peso_em_ordem = sorted(lista)

print('A pessoa com o MAIOR peso tem {} quilos'.format(peso_em_ordem[4]))
print('A pessoa com o MENOR peso tem {} quilos'.format(peso_em_ordem[0]))
