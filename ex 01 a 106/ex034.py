salario = float(input('Qual o salário do funcionário? '))

if salario > 1250:
    novo = salario + salario * 0.1
else:
    novo = salario + salario * 0.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))