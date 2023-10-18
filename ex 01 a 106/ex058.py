from random import randint

print('Sou seu computador!')
print('Acabei de pensar em um número de 0 a 10')
print('será que você consegue adivinhar qual é?')

pc = randint(0, 10)
palpite = int(input('qual o seu palpite? '))

while palpite > pc:
    palpite = int(input('Menor! Tenta de novo: '))
while palpite < pc:
    palpite = int(input('Mais! Tenta de novo: '))
print('Você acertou!')