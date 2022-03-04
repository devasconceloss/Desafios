tab = list()

while True:
    num = int(input('Digite um valor inteiro: '))
    if num not in tab:
        tab.append(num)
    else:
        print('Número já adicinado anteriormente!'
              '\nNão adicionarei novamente')
    r = str(input('Deseja continuar? [S/N] ')).lower()
    if r in 'sn':
        if r == 'n':
            print('\nFIM DE PROGRAMA!')
            break
    else:
        while True:
            print('Escolha uma opção válida')
            r = str(input('Deseja continuar? [S/N] '))
            if r in 'sn':
                break
tab.sort()
print(f'A lista digitada e ordenada foi: {tab}')

