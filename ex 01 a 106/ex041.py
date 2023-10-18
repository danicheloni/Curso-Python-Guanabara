import datetime
ano = int(input('Digite seu ano de nascimento: '))

today = datetime.date.today()
year = today.year
idade = year - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif idade <= 14:
    print('CLASSIFICAÇÃO: Infantil')
elif idade <= 19:
    print('CLASSIFICAÇÃO: Júnior')
elif idade < 25:
    print('CLASSIFICAÇÃO: Senior')
elif idade >= 25:
    print('CLASSIFICAÇÃO: Master')
