#cálculo imc

peso = float(input('Quantos kg você pesa? '))
alt = float(input('Qual é a sua altura em metros? '))
imc = peso/(alt ** alt)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
