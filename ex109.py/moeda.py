def Aumentar(valor = 0, perc = 0):
    novo_valor = valor * (perc/100) + valor
    return novo_valor

def Dobro(valor = 0):
    dobro = valor * 2
    return dobro

def Metade(valor = 0):
    metade = valor / 2
    return metade

def Diminuir(valor = 0, perc = 0):
    novo_valor = valor - valor * (perc/100)
    return novo_valor

def Moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
    