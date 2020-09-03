vel = int(input('Eae meu parceiro em que velocidade você esta dirigindo? '))
multa = (vel - 80)*7
if vel >= 80:
    print(f'Vc esta dirigindo acima da velocidade permitida, sua multa será de {multa}R$ ')
else:
    print('Continue assim meu garoto')