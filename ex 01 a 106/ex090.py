aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno["media"] > 7:
    aluno["status"] = 'Aprovado'
elif aluno["media"] > 6:
    aluno["status"] = 'em Recuperação'
else:
    aluno["status"] = 'Reprovado'

print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situação é igual a {aluno["status"]}')