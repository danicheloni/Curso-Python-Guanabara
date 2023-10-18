from datetime import date
atual = date.today().year
c_maior = 0
c_menor = 0

for pess in range(1,8):
    nas = int(input('Que ano a pessoa nasceu? '))
    idade = atual - nas
    if idade >= 21:
        c_maior += 1
    else:
        c_menor =+ 1

print('Temos {} maiores de idade'.format(c_maior))
print('Temos {} menores de idade'.format(c_menor))


