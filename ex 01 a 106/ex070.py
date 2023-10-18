total = maior = menor = c =0
prod_barato = ""

print('-'*30)
print('     Loja Super Baratão')
print('-'*30)

while True:
    produto = str(input('Nome do produto: '))
    c += 1
    valor = int(input('R$'))
    total += valor
    if valor > 1000:
        maior += 1
    
    if c == 1:
        menor = valor
        prod_barato = produto
    else:
        if valor < menor:
            menor = valor
            prod_barato = produto
        
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Acrescentar mais itens: [S/N] ')).strip().upper()[0]
    if adicionar == 'N':
        break
print('*-------- FIM DO PROGRAMA --------*')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato} e custou R${menor:.2f}')
