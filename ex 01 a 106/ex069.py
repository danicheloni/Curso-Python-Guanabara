maior = homem = mulher = mulher_menor = 0

while True:
    print('-'*30)
    print('Cadastre uma pessoa: ')
    print('-'*30)
    
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
        
    if idade < 20 and sexo == 'F':
        mulher_menor += 1

    continua = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if continua not in 'NS':
        continua = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menor} mulheres menores de idade cadastradas')