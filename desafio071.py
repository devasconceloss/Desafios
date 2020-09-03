'''
CAIXA ELETRONICO
VALOR SACADO
CEDULAS DE CADA VALOR QUE SERÃO ENTREGUE
'''


saque = int(input('Quantos reais você deseja sacar? '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced += 1
    else:
        if totced >= 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break



