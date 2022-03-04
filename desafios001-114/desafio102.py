def fatorial(n,show=False):
    """
    :param n: Número que terá o fator calculado
    :param show: Se show for true, o programa mostrará a fatoração passo a passo, se falso, mostrará apenas o resultado
    :return:
    """

    fat = 1
    for i in range(n,1,-1):
        fat *= i
    if show == True:
        fat = 1
        for i in range(n,0,-1):
            fat *= i
            print(f'{n}x{i}', end=' ')
        print(f'= {fat}')
    if show == False:
        print(f'O fatorial de {n} é {fat}')


fatorial(n=int(input('Número: ')),show=True)
fatorial(5,False)
help(fatorial)