from random import randint
sort = list()
par = list()


for n in range(5):
    d = randint(1, 10)
    sort.append(d)
    if d % 2 == 0:
        par.append(d)




def sorteio(*num):
    print('Sorteando 5 números aleatórios: ', end='')
    print(sort)


def somapar(*num):
    print(f'A soma dos números pares da lista sorteada {sort} é igual a {sum(par)}')


sorteio(sort)
somapar(par)