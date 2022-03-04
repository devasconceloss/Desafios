#CONTADOR DE VOGAIS

vogais: int = 0
consoantes: int = 0

tp = ('Notebook', 'Pao', 'Mouse')

for n in tp:
    print(f'\nNa palavra {n} temos as vogais: ', end='')
    for letra in n:
        if letra in 'aeiou':
            vogais += 1
            print(letra, end='')
        else:
            consoantes += 1

print(f'\nExistem {vogais} vogais nesta tupla e {consoantes} consoantes')
