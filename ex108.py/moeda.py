def Aumentar(valor = 0, perc = 0, formatar = False):
    novo_valor = valor * (perc/100) + valor
    if formatar is False:
        return novo_valor
    else:
        return Moeda(novo_valor)

def Dobro(valor = 0, formatar = False):
    dobro = valor * 2
    if formatar is False:
        return dobro
    else:
        return Moeda(dobro)

def Metade(valor = 0, formatar = False):
    metade = valor / 2
    if formatar is False:
        return metade
    else:
        return Moeda(metade)

def Diminuir(valor = 0, perc = 0, formatar = False):
    novo_valor = valor - valor * (perc/100)
    if formatar is False:
        return novo_valor
    else:
        return Moeda(novo_valor)

def Moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
    