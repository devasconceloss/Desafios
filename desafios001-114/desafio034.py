slr = float(input('Digite o seu salário por favor: '))
if slr > 1250:
    print(f'O seu salário após o aumento será de {slr+(slr*0.1)}R$')
else:
    print(f'O seu salário após o aumento será de {slr+(slr*0.15)}R$')
