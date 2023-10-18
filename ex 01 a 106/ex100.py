from random import randint

numero = []


def Sorteia():
    for v in range(0,5):
        num = randint(0, 50)
        numero.append(num)
        v += 1
    print(numero)


def Soma_par():
    soma = 0
    for v in numero:
        if v % 2 == 0:
            soma += v
    print(soma)


#Programa Principal
Sorteia()
Soma_par()