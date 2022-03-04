cont = 0

n = (int(input('Digite um número inteiro: ')),
     int(input('Digite um número inteiro: ')),
     int(input('Digite um número inteiro: ')),
     int(input('Digite um número inteiro: ')))

print(f'\nVocê digitou os valores {n}'
      f'\nO valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'\nO valor 3 foi digitado na {n.index(3) + 1}ª posição ')
else:
    print('O valor 3 não foi digitado')

print(f'\nO(s) número(s) par(es) desta tupla são: ')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')
