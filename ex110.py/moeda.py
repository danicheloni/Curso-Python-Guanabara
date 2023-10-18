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

def Resumo(valor, aum, dim):
    """retorna o Dobro, Metade, Aumento Percentual e Diminuição Percentual do valor no parametro

    Args:
        valor (_float_): valor a ser manipulado
        aum (_float_): percentual a ser aumentado
        dim (_float_): percentual a ser diminuido
    """
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{Moeda(valor)}')
    print(f'Dobro do Preço: \t{Dobro(valor, True)}')
    print(f'Metade do Preço: \t{Metade(valor, True)}')
    print(f'20% de aumento: \t{Aumentar(valor, aum, True)}')
    print(f'12% de Redução: \t{Diminuir(valor, dim, True)}')
    print(f'-'*30)
