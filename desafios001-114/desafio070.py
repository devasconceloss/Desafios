'''
A) total gasto
B) quantos produtos + 1000
C) nome do mais barato
'''

cont = ptotal = cont2 = maisbr = nomebr = 0
while True:
    nome = str(input('\nInsira o nome do produto aqui: '))
    cont2 += 1
    prç = float(input('Insira o preço do produto aqui: '))

    while True:
        c = str(input('Deseja inserir novos produtos? [S/N] ')).lower()
        if c in 'sn':
            break


    ptotal += prç
    if cont2 == 1:
        nomebr = nome
        maisbr = prç
    elif prç < maisbr:
        nomebr = nome
    if prç > 1000:
        cont += 1
    if c == 'n':
        break


print(f'\nMERCADINHO DO SEU ZÉ'
      f'\nO total gasto foi R${ptotal}, '
      f'\n{cont} produtos custando mais de R$1000 foram comprados'
      f'\nO produto mais barato foi o {nomebr}')