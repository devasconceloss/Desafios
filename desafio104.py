def leia_int(msg):
    """

    :param msg: A função informa se a mensagem passada é um valor inteiro, porém não consegui fazê-la declarar que é um
    numero real(1.2 por exemplo)
    Se a mensagem for uma string, o laço se repetirá até receber um número ''inteiro''
    :return:
    """
    estado = False
    valor = 0
    while True:
        d = str(input(msg))
        if d.isnumeric():
            valor = int(d)
            estado = True
            break
        else:
            print(f'Erro, {d}, não é um valor inteiro, é um {type(d)}')
    return valor


d = leia_int('\nDigite algo: ')
print(f'{d}, é um valor inteiro')
