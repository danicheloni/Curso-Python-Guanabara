sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos, por favor digite novamente: [M/F]: ')).strip().upper()[0]
print('Dados corretos! Obrigada')