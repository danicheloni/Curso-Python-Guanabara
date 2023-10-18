from time import sleep


def maior(* num):
    c = n = 0
    print('-='*20)
    print('Analisando os números: ')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.4)
        if c == 0:
            n = valor
        else:
            if valor > n:
                n = valor
        c += 1
    print(f'\nO maior número digitado foi: {n}')
    print(f'Foram digitados {c} números')
    print('-='*20)



#Programa Principal
maior(1, 5, 10, 5, 8, 30)
#maior(1, 2)
#maior(6)
#maior()
