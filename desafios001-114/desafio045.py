#jokenpô
import  random
from time import sleep
print('1 - Pedra, 2 - Papel, 3 - Tesoura')
ply = int(input('Escolha sua jogada: '))

jkp = [1, 2, 3]
pc = random.choice(jkp)

print('-=-=-=-='*10)
print('         JO')
print('         KEN')
print('         PO!!!!!!')
print('-=-=-=-='*10)


if ply == pc:
    print('Ninguém ganhou')
elif ply == 2 and pc == 3:
    print('O computador venceu')
elif ply == 2 and pc == 1:
    print('Você venceu!')
elif ply == 1 and pc == 2:
    print('O computador venceu')
elif ply == 1 and pc == 3:
    print('Você venceu')
elif ply == 3 and pc == 1:
    print('O computador venceu')
elif ply == 3 and pc == 2:
    print('Você venceu')
else:
    print('Você digitou um valor não correspondente á uma jogada')






