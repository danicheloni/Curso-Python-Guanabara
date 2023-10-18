import moeda

valor = float(input('Digite o valor: R$'))

print(f'O dobro de {moeda.Moeda(valor)} é {moeda.Dobro(valor, True)}')
print(f'Diminuindo 10%, temos {moeda.Diminuir(valor, 10, True)}')
print(f'Aumentando 10%, temos {moeda.Aumentar(valor, 10, True)}')
print(f'A metade de {moeda.Moeda(valor)} é {moeda.Metade(valor, True)}')