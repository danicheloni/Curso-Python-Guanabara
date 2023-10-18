expressao = str(input('Digite a expressão:'))
cont_c = 0
cont_Ɔ = 0


for c in expressao:
    if c == '(':
        cont_c += 1
    if c == ')':
        cont_Ɔ += 1
if cont_c == cont_Ɔ:
    print('A expressão é VÁLIDA')
else:
    print('A expressão é INVÁLIDA')