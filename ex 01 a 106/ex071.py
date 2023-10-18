nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Qual o valor que você deseja sacar: '))
while valor > 0:
    nota50 = valor // 50
    valor = valor - nota50 * 50
    
    nota20 = valor // 20
    valor = valor - nota20 * 20
    
    nota10 = valor // 10
    valor = valor - nota10 * 10

    nota5 = valor // 5
    valor = valor - nota5 * 5

    nota2 = valor // 1
    valor = valor - nota2 * 1

print(f'Total de {nota50:.0f} cédulas de R$50')
print(f'Total de {nota20:.0f} cédulas de R$20')
print(f'Total de {nota10:.0f} cédulas de R$10')
print(f'Total de {nota5:.0f} cédulas de R$5')
print(f'Total de {nota2:.0f} cédulas de R$1')




