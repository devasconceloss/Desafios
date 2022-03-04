jog = dict()
soma = 0
gol = list()

jog['Nome'] = str(input('Nome do jogador: '))
jog['Partidas'] = int(input('Quantas partidas ele jogou? '))

for c in range(1, jog['Partidas'] + 1):
    gols = int(input(f'Quantos gols {jog["Nome"]} fez na partida {c}? '))
    soma += gols
    gol.append(gols)
    jog['Lista de gols'] = gol
    jog['Total de Gols'] = soma

print('-=-'*10)
print('Lista de gols')
print('-=-'*10)
for i,v in enumerate(gol):
    print(f'O {jog["Nome"]} fez {v} gols na partida {i+1}')

print('-=-'*10)
print('DESEMPENHO COMPLETO')
print(jog)
print('-=-'*10)