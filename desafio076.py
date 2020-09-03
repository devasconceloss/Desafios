#LISTAGEM DE PREÇOS

Card = ('Pão', 3, 'Ovo', 5, 'Presunto', 6, 'Queijo', 8)
print('-=-=-'*8)
print(f'{"Cardápio":^35}')
print('-=-=-'*8)
for pos in range(0, len(Card)):
    if pos % 2 == 0:
        print(f'{Card[pos]:.<30}', end='')
    else:
        print(f'R${Card[pos]:>4.2f}')
