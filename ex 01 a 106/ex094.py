pessoas_list = []
cadastro = {}

idade = 0

while True:
    cadastro["nome"] = str(input('Nome: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[F/M] ')).strip().upper()[0]
        cadastro["sexo"] = sexo
        if sexo not in "MF":
            print('ERRO! Digite M ou F')
            
    cadastro["idade"] = int(input('Idade: '))
    idade += cadastro["idade"]

    pessoas_list.append(cadastro.copy())

    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Acrescentar mais números: [S/N] ')).strip().upper()[0]
        if adicionar not in 'SN':
            print('ERRO! Digite S ou N')
    if adicionar == 'N':
        break
print('-=' * 20)
print(f'A) Ao todo temos {len(pessoas_list)} pessoas cadastradas')
print(f'B) A media das idade é de {idade/len(pessoas_list):.1f} anos')

print(f'C) As mulheres cadastradas foram: ')
for p in pessoas_list:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}' , end=' ')

print(f'\nD) a lista de pessoas que estão acima da média de idade são: ')
for p in pessoas_list:
    if p["idade"] > idade/len(pessoas_list):
        print(p)
        