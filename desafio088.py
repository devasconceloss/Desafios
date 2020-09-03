from random import randint
from time import sleep

lista = list()
jogos = list()

print('-=-'*10)
print('      JOGO DA MEGA SENA')
print('-=-'*10)

n = int(input('Quantos jogos você deseja que eu sorteie? '))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=-'*4 ,'Gerando apostas', '-=-'*4)
for i, v in enumerate(jogos):
    print(f'Jogo nº{i+1}: {v}')
    sleep(3)
print('-=-'*5, 'BOA SORTE', '-=-'*5)

