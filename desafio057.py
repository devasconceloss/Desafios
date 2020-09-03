

while True:
    nm = str(input('Qual é o seu nome? '))
    sx = str(input('Qual é o seu sexo [M/F]? ')).upper()

    if sx != 'M' and sx != 'F':
        print('Você digitou um valor inesperado, tente novamente')
    else:
        print(f'Ok {nm}, anotado!')