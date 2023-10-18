from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)
    f = f+1
    for n in range(i, f, p):
        print(f'{n}', end=' ')
    print('FIM!')
    print('-=' * 20)


#Programa Principal
contador(1, 10, 1)
contador(10, 0, -2 )

print(f'Agora é sua vez de personalizar a contagem')
comeco = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(comeco, fim, passo)