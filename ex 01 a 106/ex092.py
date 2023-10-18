#nome, idade, ctps, -> só se tiver CTPS ano contratação, salario
from datetime import date

ano_atual = date.today().year
print(ano_atual)

pessoa = {}
pessoa["nome"] = str(input('Nome: '))
ano_nas = int(input('Ano de Nascimento: '))
pessoa["idade"] = ano_atual - ano_nas
pessoa["ctps"] = int(input('Nº CTPS: (0 não tem) '))

if pessoa["ctps"] != 0:
    pessoa["contratação"] = str(input('Ano de Contratação: '))
    pessoa["salário"] = float(input('Salário: '))
    pessoa["aposentadoria"] = 60 - (ano_atual - ano_nas)
print('-=' * 15)

for k, v in pessoa.items():
    print(f'o {k} tem valor: {v}')
print('-='*15)