n = int(input('Você quer ver a tabuada de que valor? '))

while True:
    c=0
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
        c+=1
    n = int(input('Você quer ver a tabuada de que valor? '))
    if n < 0:
        break