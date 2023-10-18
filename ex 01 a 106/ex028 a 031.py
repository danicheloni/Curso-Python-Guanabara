cores = {'limpa' : '\033[m', 
         'azul' : '\033[34m', 
         'amarelo' : '\033[33m', 
         'negrito' : '\033[1m'}

#031
dist = float(input('Qual a distancia da viagem? '))
print('Sua viagem tem {:.2f}km'.format(dist))
if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.5

print("O valor da sua viagem é de R${:.2f}".format(valor))



#ex030 par
"""num = int(input('{}Me diga um número qualquer:{} '.format(cores['azul'], cores['limpa'])))
if num % 2 == 0:
    print('O número digitado é {}par{}'.format(cores['negrito'], cores['limpa']))
else:
    print('O número digitado é {}impar{}'.format(cores['negrito'], cores['limpa']))"""


#ex029
"""velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade <= 80:
    print('\033[32mDentro do limite\033[m')
else:
    print('\033[1;31mMULTADO!\033[m')
    print('Você excedeu o limite de velocidade que é de 80km/h')
    print('Você será multado em R$280,00')
print('\033[1;36mTenha um bom dia!\033[m')"""

#ex028
"""from random import randint

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('Vou pensar em um número de 0 a 5. Tente advinhar')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

n_pc = randint(0,5) #o computador escolhe um número

n1 = int(input('Em que número eu pensei? '))

if n1 == n_pc:
    print('Isso mesmo!')
else:
    print('Foi esse número não... Pensei no número {}'.format(n_pc))"""