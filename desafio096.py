def titulo(msg):
    print('-=-' * 10)
    print(msg)
    print('-=-' * 10)


def area(a: object, b: object) -> object:
    tm = a * b
    print(f'A área do terreno é {a} x {b} = {tm}m²')


titulo('  DIMENSIONAMENTO DE TERRENO')
area(a=float(input('Largura: ')), b=float(input('Comprimento: ')))
