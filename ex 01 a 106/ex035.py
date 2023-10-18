a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))

tri = [a, b, c]
n_tri = sorted(tri)
print(n_tri)

if n_tri[0]+n_tri[1]>n_tri[2]:
    print('Sim')
else:
    print('Não')