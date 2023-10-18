sum = 0
c = 0
maior = 0
menor = 0
replay = "S"

while replay == "S":
    num = int(input('Digite um numero: '))
    sum += num
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    replay = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
print('Voce digitou {} números e a média é {:.1f}'.format(c, (sum/c)))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))

