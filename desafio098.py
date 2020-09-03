from time import sleep


def prog(I,P,F):
    if P == 0:
        P = 1
    if F < 0:
        P = P*-1
    print('-=-'*12)
    if P < 0:
        print(f'Do início: {I}, ao fim: {F}, no passo {P*-1}')
    else:
        print(f'Do início: {I}, ao fim: {F}, no passo: {P}')

    for c in range(I,F+P,P):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('-=-'*12)


prog(1,1,10)
prog(10,-2,0)
print('\nAGORA É SUA VEZ DE DEFINIR A CONTAGEM!')
prog(I= int(input('Inicio: ')),P= int(input('Passo: ')),F= int(input('Fim: ')) )