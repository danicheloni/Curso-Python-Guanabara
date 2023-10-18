def Voto(ano_nasc):
    from datetime import date
    ano = date.today().year
    
    print('-' * 30)
    idade = ano - ano_nasc
    print(f'Com {idade} anos: ', end='')
    
    if idade < 16:
        return 'VOTO PROIBIDO'
    elif 16 <= idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
     

#Programa Principal:
ano_nasc = int(input('Em que ano você nesceu? '))
s = Voto(ano_nasc)
print(s)