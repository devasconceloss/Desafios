import random

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)

tp = (a, b, c, d)
menor = 0

if a <= b and a <= c and a <= d:
    menor = a
if b <= a and b <= c and b <= d:
    menor = b
if c <= b and c <= d:
    menor = c
    if d <= c:
        menor = d


print(f'A tupla gerada aleatoriamente é: {tp}'
      f'\nO menor número é: {menor}')