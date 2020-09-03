
cont = 0

a = int(input('Digite um número por favor: '))
b = int(input('Digite um número por favor: '))
c = int(input('Digite um número por favor: '))
d = int(input('Digite um número por favor: '))

tp = (a, b, c, d)

if a == 9:
    cont += 1
if b == 9:
    cont += 1
if c == 9:
    cont += 1
if d == 9:
    cont += 1



print(f'Você digitou os valores {tp}'
      f'\nO valor 9 foi digitado {cont} vezes')
if a == 3 or b == 3 or c == 3 or d == 3:
   print(f'O valor 3 foi digitado na posição {tp.index(3)}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

if a/2 == 0:
    print('Os numeros')