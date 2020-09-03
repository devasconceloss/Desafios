num = list()

menor = maior = 0
for cont in range(0, 5):
    num.append(int(input('Digite um valor inteiro: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] <= menor:
            menor = num[cont]
        if num[cont] >= maior:
            maior = num[cont]

print(f'\nA lista que você digitou foi {num}')

for c, v in enumerate(num):
    if v == maior:
        print(f'O maior valor digitado foi {max(num)} na posição {c+1}')
    if v == menor:
        print(f'O menor valor digitado foi {min(num)} na posição {c+1}')


