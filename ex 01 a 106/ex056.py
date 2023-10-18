c_idade = 0
c_fem = 0
nome_velho = ''
idade_velho = 0

for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).upper()
   
    c_idade += idade
    media = c_idade/ p
   
    if sexo == 'F' and idade < 21:
        c_fem += 1

    if sexo == 'M' and idade > idade_velho:
        nome_velho = nome.capitalize()
        idade_velho = idade

print('A média de idade das pessoas do grupo é de {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_velho, idade_velho))
print('Existem {} mulheres com menos de 20 anos'.format(c_fem))


