
r = 'S'

while r == 'S':
    n1 = float(input('Digite o primeiro número por favor: '))
    n2 = float(input('Digite o segundo número por favor: '))

    print('OPERAÇÕES '
          '\n \033[1;34;40m[1]\033[m \033[1;34;40m- ADIÇÃO       \033[m '
          '\n \033[1;34;40m[2]\033[m \033[1;34;40m- SUBTRAÇÃO    \033[m '
          '\n \033[1;34;40m[3]\033[m \033[1;34;40m- MULTIPLICAÇÃO\033[m '
          '\n \033[1;34;40m[4]\033[m \033[1;34;40m- DIVISÃO      \033[m '
          '\n \033[1;34;40m[5]\033[m \033[1;34;40m- NOVOS NÚMEROS\033[m '
          '\n \033[1;34;40m[6]\033[m \033[1;34;40m- MAIOR        \033[m '
          '\n')
    op = int(input('Qual operação vc deseja fazer? '))

    if op == 1:
        print(f'Você escolheu Adição, então, {n1} + {n2} = {n1+n2}')
    if op == 2:
        print(f'Você escolheu Subtração, então, {n1} - {n2} = {n1-n2}')
    if op == 3:
        print(f'Você escolheu Multiplicação, então, {n1} x {n2} = {n1*n2}')
    if op == 4:
        print(f'Você escolheu Divisão, então, {n1} / {n2} = {n1/n2}')
    if op == 6 and n1 > n2:
        print(f'O 1º número: ({n1}) é maior que o 2º: ({n2})')
    if op == 6 and n2 > n1:
        print(f'O 2º número: ({n2}) é maior que o 1º: ({n1})')
    if op == 6 and n1 == n2:
        print('Ambos os números são iguais')
    if op == 5:
        nv1 = float(input('Digite o 1º número novamente: '))
        nv2 = float(input('Digite o 2º número novamente: '))

        print('OPERAÇÕES '
          '\n \033[1;34;40m[1]\033[m \033[1;34;40m- ADIÇÃO       \033[m '
          '\n \033[1;34;40m[2]\033[m \033[1;34;40m- SUBTRAÇÃO    \033[m '
          '\n \033[1;34;40m[3]\033[m \033[1;34;40m- MULTIPLICAÇÃO\033[m '
          '\n \033[1;34;40m[4]\033[m \033[1;34;40m- DIVISÃO      \033[m '
          '\n \033[1;34;40m[5]\033[m \033[1;34;40m- NOVOS NÚMEROS\033[m '
          '\n \033[1;34;40m[6]\033[m \033[1;34;40m- MAIOR        \033[m '
          '\n')
        op = int(input('Qual operação vc deseja fazer? '))

        if op == 1:
            print(f'Você escolheu Adição, então, {nv1} + {nv2} = {nv1 + nv2}')
        if op == 2:
            print(f'Você escolheu Subtração, então, {nv1} - {nv2} = {nv1 - nv2}')
        if op == 3:
            print(f'Você escolheu Multiplicação, então, {nv1} x {nv2} = {nv1 * nv2}')
        if op == 4:
            print(f'Você escolheu Divisão, então, {nv1} / {nv2} = {nv1 / nv2}')
        if op == 6 and nv1 > nv2:
            print(f'O 1º número: {nv1} é maior que o 2º {nv2}')
        if op == 6 and nv2 > nv1:
            print(f'O 2º número: {nv2} é maior que o 1º {nv1}')
        if op == 6 and nv1 == nv2:
            print('Ambos os números são iguais')

    r = str(input('Você deseja continuar com as operações [S/N]? ')).upper()

print('\nok, obg')


