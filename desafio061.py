#Progressão aritmética com comand while

p1 = int(input('Primeeiro termo: '))
rz = int(input('Informe a razão da P.A: '))
tr = p1
cont = 1
while cont <= 10:
    print(f' {tr} -> ', end= '')
    tr += rz
    cont += 1

