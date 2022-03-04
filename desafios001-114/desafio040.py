# calculo de média e aprovação/reprovação

n1 = float(input('Qual foi o valor da sua primeira nota? '))
n2 = float(input('Qual foi o valor da sua segunda nota? '))
média = (n1 + n2)/2

if média >= 7:
    print('Parabéns você foi aprovado')
elif média <= 6.9 and média >= 5:
    print('Você está em recuperação')
else:
    print('REPROVADO')