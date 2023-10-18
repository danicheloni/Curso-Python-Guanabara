import datetime
ano = int(input('Digite seu ano de nascimento: '))

today = datetime.date.today()
year = today.year
idade = year - ano


if idade == 18:
    print('Você deve se alistar')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu ano de alistamento foi em {}'.format(ano + 18))
elif idade < 18:
    print('Ainda falta {} anos para o seu alistamento'.format(18-idade))
    print('Seu ano de alistamento será em {}'.format(ano + 18))
