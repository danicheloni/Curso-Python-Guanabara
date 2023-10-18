casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você vai pagar?'))

parcela = casa / (anos * 12)
teto = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, parcela))

if parcela > teto:
    print('Esse empréstimo não pode ser concedido!')
else:
    print('Esse empréstimo pode ser concedido')