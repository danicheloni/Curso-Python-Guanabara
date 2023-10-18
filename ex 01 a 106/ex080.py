valores = []
for count in range(0,5):
    num = int(input('Digite um valor: '))
    if count == 0 or num > valores[-1]:
        valores.append(num)
    else:   
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print('-='*30)
print(f'Você digitou os números {valores}')