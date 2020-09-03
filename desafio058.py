from random import randint
cont = 1de
pc = randint(0,5)
ply = int(input('Digite um número e tente a sorte!: '))

while ply != pc:
    print('Você errou, tente novamente')
    ply = int(input('Digite um número e tente a sorte!: '))
    cont += 1
print(f'Você acertou na sua {cont}ª tentativa')

