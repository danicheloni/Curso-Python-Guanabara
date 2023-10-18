import moeda

valor = float(input('Digite o valor: R$'))

print(f'O dobro de R${valor} é R${moeda.Dobro(valor)}')
print(f'Diminuindo 10%, temos R${moeda.Diminuir(valor, 10)}')
print(f'Aumentando 10%, temos R${moeda.Aumentar(valor, 10)}')
print(f'A metade de R${valor} é R${moeda.Metade(valor)}')