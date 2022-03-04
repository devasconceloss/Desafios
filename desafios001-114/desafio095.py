avaliados = dict()
gols = list()
geral = list()

while True:
    avaliados['Nome'] = str(input('Nome: '))
    avaliados['Partidas'] = int(input(f'Quantas partidas {avaliados["Nome"]} jogou? '))
    for i in range(1,avaliados['Partidas']+1):
        gol = (int(input(f'Quantos gols {avaliados["Nome"]} fez na {i}ª partida? ')))
        gols.append(gol)
        avaliados['Gols'] = gols
    geral.append(avaliados.copy())
    gols.clear()
    r = str(input('Deseja cadastrar mais um jogador [S/N]? ')).lower()

    if r not in 'sn':
        while True:
            print('OPÇÃO INVÁLIDA')
            r = str(input('Deseja cadastrar mais um jogador [S/N]? ')).lower()
            if r == 'n':
                break
            if r == 's':
                break
    if r == 'n':
        break
print('-=-'*20)
print('DESEMPENHO DOS AVALIDADOS')
print(f'{"Cod.":>4}   {"Nome":<4}     {"Gols":<4}')
for i, v in enumerate(geral):
    print(f'{i+1:>4} {geral[i]["Nome"]:<4} fez {geral[i][]}')

'''for i, v in enumerate(gols):
    print(f'O jogador {avaliados["Nome"]} fez {v} gol(s) na {i+1}ª partida')'''

print('-=-'*20)