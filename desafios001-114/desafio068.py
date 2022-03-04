#PAR OU IMPAR E VITORIAS CONSECUTIVAS

import random
seq = 0

print('----'*7)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('----'*7)

while True:

    ply = int(input('\nVocê escolhe 1 - PAR OU 2 - IMPAR? '))
    pln = int(input('Escolha um número inteiro: '))
    pcn = random.randint(0,10)
    res = pln + pcn

    if ply == 1:
        pc = 2
    else:
        pc = 1

    if (res % 2) == 0 and ply == 1:
         print(f'\nO Jogador escolheu Par e o número {pln}, o Pc escolheu {pcn}, o jogador venceu!')
         seq += 1
    if (res % 2) != 0 and ply == 2:
        print(f'\nO Jogador escolheu ìmpar e o número {pln}, o Pc escolheu {pcn}, o jogador venceu!')
        seq += 1
    if res % 2 == 0 and pc == 1:
        print(f'\nO Computador escolheu par e o número {pcn}, o Jogador escolheu {pln}, o computador venceu!')
        break
    if res % 2 != 0 and pc == 2:
        print(f'\nO Computador escolheu ìmpar e o número {pcn}, o Jogador escolheu {pln}, o computador venceu!')
        break
print('----'*20)
print(f'O jogador venceu {seq} partidas seguidas, mas agora o jogo está encerrado!')
print('----'*20)












