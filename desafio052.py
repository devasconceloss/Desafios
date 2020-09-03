#numeros primos
'''
Números primos são aqueles cujo valor esta cima de 1 e só pode ser DIVIDIDO por um e ele mesmo
end fez com que o print escreva em uma linha só'''

tot = 0
n= int(input('Digite um número inteiro: '))
print(f'Estes são os divisores de {n}: ')

for i in range(1,n + 1):
  if n % i == 0:
    print(i, end=' ')
    tot +=1
if tot == 2:
  print(f'\nO número {n} é primo')
else:
  print(f'\nO número {n} não é primo')


