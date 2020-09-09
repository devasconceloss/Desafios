def ficha(nome='',gols=''):
    if nome == '':
        nome = 'fantasma'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gols no campeonato')


ficha(nome=str(input('Nome: ')),gols=str(input('Gols: ')))
