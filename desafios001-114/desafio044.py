#calculo preço e forma de pgmnto

pgmnt = int(input('Qual será a forma de pagamento? 1 - A vista dinheiro/cheque, 2 - Á vista no cartão, 3 - 2x no cartão, 4 - 3x ou mais '))

prc = float(input('Qual é o preço do produto? '))

if pgmnt == 1:
    print(f'À vista no dinheiro/cheque, você terá 10% de desconto, então o valor do produto será {prc - (prc*0.1)}R$ ')
elif pgmnt == 2:
    print(f'À vista no cartão, o desconto é de 5%, ou seja, o preço será de {prc - (prc*0.5)}R$')
elif pgmnt == 3:
    print('Sem descontos')
elif pgmnt == 4:
    print(f'20% de juros, o preço será {prc + (prc*0.2)}R$ ')
else:
    print('Você digitou um número que não corresponde a uma forma de pagamento')