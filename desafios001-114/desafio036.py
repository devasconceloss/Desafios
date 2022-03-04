'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado'''


slr = float(input('Quanto é o seu salário? '))
temp = int(input('Em quantos anos você pretende pagar? '))
casa = float(input('Qual é o valor da casa? '))
anos = temp*12
prest = casa/anos
if prest > slr*0.3:
    print('O empréstimo foi negado')
else:
    print(f'O empréstimo foi aprovado, a prestação mensal será de {prest}')