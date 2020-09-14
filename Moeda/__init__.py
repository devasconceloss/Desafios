def dobro(num=int, formatar=False):
    num *= 2
    if not formatar:
         return num
    else:
        return real(num)


def metade(num=0, formatar=False):
    num *= 0.5
    if not formatar:
         return num
    else:
        return real(num)



def infla(num=0, aumento=0, formatar=False):
    num += num * (aumento / 100)
    if not formatar:
        return num
    else:
        return real(num)


def dim(num=0, diminuicao=0, formatar=False):
    num -= num * (diminuicao / 100)
    if not formatar:
        return num
    else:
        return real(num)


def real(num=0, cambio='R$'):
    return f'{cambio}{num}'.replace('.', ',')


def resumo(num=0, aumento=0, diminuicao=0, cambio='R$'):
    """

    :param num: Valor a ser convertido em real
    :param aumento: Acréscimo ao valor digitado anteriormente
    :param diminuicao: Decréscimo ao valor digitado anteriormente
    :param cambio: R$
    :return:
    """
    double = num*2
    half = num*0.5
    aume = num + (num * aumento/100)
    dimi = num - (num * diminuicao/100)

    titulo = 'Análise'
    print('--' * 20)
    print(titulo.center(40))
    print('--' * 20)
    print(f'\nPreço digitado: {cambio}{num}'
          f'\nDobro: {cambio}{double}'
          f'\nMetade: {cambio}{half}'
          f'\nAumentando {aumento}%: {cambio}{aume}'
          f'\nDiminuindo {diminuicao}%: {cambio}{dimi}'.replace('.', ','))

