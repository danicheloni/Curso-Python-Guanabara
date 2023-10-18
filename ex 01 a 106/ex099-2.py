from random import randint


num = randint(1, 10)
lista= []
num2 = 0


def maior(): 
    print('-=' * 20)
    print('Analisando os valores passados: ')
    for c in range(0, num):
        num2 = randint(0,50)
        lista.append(num2)
        c += 1
        print(f'{num2}', end=' ')
    print(f'\nforam informados {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {sorted(lista)[-1]}')
    print('-=' * 20)

maior()