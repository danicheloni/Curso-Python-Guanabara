def Notas(*n, sit=False):
    """
    =>Função que retorna dados sobre numeros inseridos
    =>param1: n, numero indeterminado de notas a serem calculadas
    =>param2: sit, opcional. Boleano. Se a situação das médias será retornada
    =>return: retorna indicando a situação das notas da turma 
    """

    dict = {}
    dict["total"] = len(n)
    dict["maior"] = max(n)
    dict["menor"] = min(n)
    dict["media"] = sum(n)/len(n)
    if sit == True:
        if dict["media"] > 8:
            dict["situação"] = 'BOA'
        elif dict["media"] < 4:
            dict["situação"] = 'RUIM'
        else:
            dict["situação"] = 'MÉDIA'
    return dict



#Programa Principal
resp = Notas(5.5, 2.5, 1.5, sit=True)
print(resp)