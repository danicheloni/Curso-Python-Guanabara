def Fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    param num: O número a ser calculado
    param show: (opcional) Mostrar ou não o calculo
    return: mostra o resultado do cálculo do Fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f    



#Programa Principal
#print(Fatorial(5, True))
help(Fatorial)