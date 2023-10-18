numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')
#minha solução
num = int(input('Digite um numero de 0 a 5: '))
while True:
    if num < 0 or num > 5:
        num = int(input('Digite um numero de 0 a 5: '))    
    if 0 <= num <= 5:
        print(f'Você digitou o número {numero[num]}')
        break

#solução Guanabara
while True:
    num = int(input('Digite um numero de 0 a 5: '))
    if 0<= num <= 5:
        break
    print('Tente novamente. ', end=' ')
print(f'Você digitou o número {numero[num]}')
