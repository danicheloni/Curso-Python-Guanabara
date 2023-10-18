r1 = float(input('Digite uma medida: '))
r2 = float(input('Digite uma medida: '))
r3 = float(input('Digite uma medida: '))

if r1 <r2+r3 and r2<r1+r3 and r3<r2+r1:
    if r1==r2==r3:
        print('As medidas acima formam um triangulo EQUILÁTERO')
    if r1==r2 or r1==r3 or r2==r3:
        print('As medidas acima formam um triangulo ISÓCELES')
    else:
        print('As medidas acima formam um triangulo ESCALENO')
else:
    print('As medidas acima não formam um triangulo')