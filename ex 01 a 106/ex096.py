def area(comp, larg):
    area = larg*comp
    print(f'A área de um terreno {larg}x{comp} é {area}m²')
    
#Programa Principal
c = float(input('COMPRIMENTO (m): '))
l = float(input('LARGURA (l): '))
area(c, l)