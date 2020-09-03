
while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print('\nPROGRAMA ENCERRADO')
        break

    print(f'---'*20)
    print(f'{n} x 1 = {n*1}'
          f'\n{n} x 2 = {n*2}'
          f'\n{n} x 3 = {n*3}'
          f'\n{n} x 4 = {n*4}'
          f'\n{n} x 5 = {n*5}'
          f'\n{n} x 6 = {n*6}'
          f'\n{n} x 7 = {n*7}'
          f'\n{n} x 8 = {n*8}'
          f'\n{n} x 9 = {n*9}'
          f'\n{n} x 10 = {n*10}')
