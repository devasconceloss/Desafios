LP = dict()
Geral = list()
lg = list()
while True:
    LP.clear()
    lg.clear()
    LP['Nome'] = str(input('Nome: '))
    LP['Partidas'] = int(input('Partidas jogadas? '))

    for i in range(1, LP['Partidas'] + 1):
        lg.append(int(input(f'Quantos gols {LP["Nome"]} fez na partida {i}? ')))

    LP['Gols'] = lg[:]
    LP['Total'] = sum(lg)
    Geral.append(LP.copy())
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

print('-=-'*30)
print('Cod', end=' ')
for i in LP.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(Geral):
    print(f'{i:>2}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-'*30)

while True:
    b = int(input('\nInforme o códigoo do jogador que deseja buscar: (999 para interromper) '))
    if b == 999:
        print('FIM DE PROCESSO, VOLTE SEMPRE!!')
        break
    if b >= len(Geral):
        print('Não existe este código, tente novamente!')
        b = int(input('Informe o códigoo do jogador que deseja buscar: (999 para interromper) '))
    else:
        print('-=-'*15)
        print(f'\nFicha do jogador {Geral[b]["Nome"]}')
        for k, v in enumerate(Geral[b]['Gols']):
            print(f'O jogador fez {v} gols na partida {k+1}')







