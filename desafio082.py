geral = list()
pares = list()
impares = list()


while True:
    n = int(input('Digite um número inteiro: '))
    geral.append(n)
    r = str(input('Deseja continuar [S/N]? ')).lower()
    while True:
        if r not in 'sn':
            print('DIGITE UMA OPÇÃO VÁLIDA')
            r = str(input('Deseja continuar [S/N]? ')).lower()

        if r == 's':
            n = int(input('Digite um número inteiro: '))
            geral.append(n)
            r = str(input('Deseja continuar [S/N]? '))
        if r == 'n':
            break

    for i, v in enumerate(geral):
        if v % 2 == 0:
            pares.append(v)
        elif v % 2 != 0:
            impares.append(v)
    break

b = geral[:]



print(f'\nLista geral {b}'
      f'\nLista de pares {pares}'
      f'\nLista de ímpares {impares}')