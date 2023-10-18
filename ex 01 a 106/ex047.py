#ex048
soma = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
print(soma)

#ou

for c in range(1, 51, 2):
    if c % 3 == 0:
        soma += c
print(soma)



#ex047
"""for c in range(1,51):
    if c % 2 == 0:
        print(c, end=' ')"""