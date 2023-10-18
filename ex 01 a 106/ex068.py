from random import randint

print('='*40)
print('             Par ou Ímpar?')
print('='*40)

c = 0

while True:    
    jogador = int(input('Digite um valor? '))
    computador = randint(0,10)
    tipo = ' '
    soma = jogador + computador
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. A soma é {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!')
            c += 1       
        else:
            print('GAME OVER!!', end=' ')
            break
    elif tipo == 'I':
        if soma % 2 !=0:
            print('Você VENCEU!!')
            c += 1          
        else:
            print('GAME OVER!!', end=' ')
            break
print(f'Você ganhou {c} vezes antes de perder')
