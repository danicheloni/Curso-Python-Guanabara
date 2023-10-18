p = str(input('Digite uma frase: ')).strip().upper()

count = 0
palavra = ''
inverso = ''

#tirando os espaços
for l in p:
    if l != ' ':
        palavra += l

#invertendo a string
for l in range(len(palavra)-1, -1, -1):
    inverso += palavra[l]

print('O inverso de {} é {}'.format(palavra, inverso))

if palavra == inverso:
    print('\033[32mTemos um palíndromo\033[m')
else:
    print('\033[31mNão temos um palíndromo\033[m')
