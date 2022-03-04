#ordem crescente do peso de 5 pessoas
from datetime import date
cont = 0
for i in range(1,8):
    n = int(input(f'Digite o ano de nascimendo da {i}ª pessoa: '))
    if date.today().year - n > 18:
        cont += 1
print(f'o número de maiores de idade é: {cont} e os número de menores é: {i - cont}')