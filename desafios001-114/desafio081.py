cont = 0
valores = []

while True:
    n = int(input('Digite um número inteiro: '))
    r = str(input('Deseja continuar? [S/N] ')).lower()
    valores.append(n)
    while True:
        if r not in 'sn':
            print('Opção inválida, tente novamente!')
            r = str(input('Deseja continuar? [S/N] ')).lower()
        elif r == 's':
            n = int(input('Digite um número inteiro: '))
            r = str(input('Deseja continuar? [S/N] ')).lower()
            valores.append(n)
        else:
            break
    break



print(f'\nEsta é a lista digitada {valores},'
      f'\nEsta é a lista ordenada de forma decrescente:')
valores.sort(reverse=True)
print(f'{valores}')

desaif 5 in valores:
    print(f'O valor 5 foi digitado na lista')
else:
    print('Não há nenhum 5 na lista')


