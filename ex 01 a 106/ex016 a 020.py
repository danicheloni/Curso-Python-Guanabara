#ex020 ordem
"""import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
my_list = [a1, a2, a3, a4]
random.shuffle(my_list)
print('A apresentação se dará na seguinte ordem {}'.format(my_list))"""

#ex019 sorteio
"""import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
my_list = [a1, a2, a3, a4]
escolhido = random.choice(my_list)
print('O aluno escolhido foi {}'.format(escolhido))"""

#ex18 angulos
"""import math
angulo = float(input('Digite o angulo que você deseja: '))
rad = math.radians(angulo)
sin = math.cos(rad)
cos = math.sin(rad)
tan =math.tan(rad)
print('O angulo de {}° tem o \nCOSSENO de {:.2f} \nSENO de {:.2f} \nTANGENTE de {:.2f}.'.format(angulo, cos, sin, tan))"""

#ex017 cateto e hipotenusa
"""from math import sqrt, hypot
cato = float(input('Qual o comprimento do Cateto Oposto? '))
cata = float(input('Qual o comprimento do Cateto Adjacente? '))
hipo = sqrt(cato**2 + cata**2)
hipo2 = hypot(cato, cata)
print('A hipotenusa vai medir {}'.format(hipo2))"""

#ex016
"""import math
n1 = float(input('Digite um valor: '))
inteiro = math.trunc(n1)
print('A porção inteira de {} é {}'.format(n1, inteiro))"""