geral = list()
pares = list()
impares = list()


for c in range(1,8):
    n = int(input(f'Digite o {c} número inteiro: '))
    geral.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

print('-=-'*30)
print(f'A lista digitado foi {geral}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')
