n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Difite a segunda nota: '))

media = (n1+n2)/2

if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('EM RECUPERAÇÂO')