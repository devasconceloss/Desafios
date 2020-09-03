from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)
         }
# ranking = dict() ---> novo dicionario para a ordenação
# itemgetter = 1 pois estamos ordenando a lista pelos valores e não pelas chaves(0)

print('VALORES SORTEADOS: ')
for i, v in jogos.items():
    print(f'O {i} tirou {v} no dado.')
    sleep(1)
print('-=-' * 10)
print('         RANKING:')
print('-=-'*10)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]};')
#dicionario se tornou uma tuplas com listas dentros por isso utilizou-se o v[0] e v[1]