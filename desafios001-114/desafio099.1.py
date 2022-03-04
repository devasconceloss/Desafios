from time import sleep


def prog(I,P,F):
    print('-=-'*12)
    print(f'Do início: {I}, ao fim: {F}, no passo: {P}')
    for c in range(I,F+P,P):
        if F < 0:
            P = P * -1
            for c in range(I, F + P, P):
                print(c, end=' ')
                sleep(0.5)
            print()
        else:
            print(c, end=' ')
            sleep(0.5)
        print()



prog(1,1,10)
prog(10,-2,0)
prog(I= int(input('Inicio: ')),P= int(input('Passo: ')),F= int(input('Fim: ')) )
