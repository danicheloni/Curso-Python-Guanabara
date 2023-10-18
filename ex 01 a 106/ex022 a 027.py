#ex027
"""nome = str(input('Digite seu nome completo: ')).strip().lower()
lista = nome.split(' ')
prim = lista[0].capitalize()
ult = lista[-1].capitalize()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(prim))
print('Seu último nome é {}'.format(ult))"""

#ex026
"""frase = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Qual letra você quer investigar: ')).strip().upper()
rep = frase.count(letra)
prim = frase.find(letra) + 1
ult = frase.rfind(letra) + 1

print('A letra {} aparece {} vezes na frase.'.format(letra, rep))
print('A primeira letra {} apareceu na posição {}'.format(letra, prim))
print('A última letra {} apareceu na posição {}'.format(letra, ult))
"""

#ex025 Silva
"""nome = str(input('Digite seu nome completo: ')).strip().upper()
a = 'SILVA' in nome
print('Seu nome tem Silva?', a)"""

#ex024
"""cid = str(input('Digite a cidade que você nasceu: ')).strip().upper()
#print(cid[:5]== "SANTO")
print('SANTO' in cid)
"""

#ex 023
"""num = int(input('Digite um número: '))
u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o número {}:'.format(num))
print('Unidade: {}'. format(u))
print('Dezena: {}'. format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))"""