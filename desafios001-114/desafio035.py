#Com o comando \033[style;text;backm é possivel colorir o terminal

from time import sleep

print('-=-'*30)

r1 = float(input('Informe o valor da 1ª reta: '))
r2 = float(input('Informe o valor da 2ª reta: '))
r3 = float(input('Informe o valor da 3ª reta: '))

print('Calculando...')
sleep(2)

if r1 == r2 and r1 == r3:
        print('Este triângulo é equilátero')
elif r1 == r2 or r2 == r3:
    print('Este triângulo é isósceles')
elif r1 != r2 and r2 != r3:
    print('Este triangulo é escaleno')

if (r1-r3) < r2 < r1 + r3 and (r2 - r3) < r1 < r2 + r3 and (r1 - r2) <r3 < r1 + r2:
    print('\033[0;34;40mCom estes valores de reta é possivel formar um triangulo\033[m')

else:
    print('\033[0;34;40mCom estes valores não é possivel formar um triangulo\033[m')