import moeda

valor = float(input('Digite o valor: R$'))

print(f'O dobro de {moeda.Moeda(valor)} é {moeda.Moeda(moeda.Dobro(valor))}')
print(f'Diminuindo 10%, temos {moeda.Moeda(moeda.Diminuir(valor, 10))}')
print(f'Aumentando 10%, temos {moeda.Moeda(moeda.Aumentar(valor, 10))}')
print(f'A metade de {moeda.Moeda(valor)} é {moeda.Moeda(moeda.Metade(valor))}')