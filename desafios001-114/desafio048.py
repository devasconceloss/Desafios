# Somatório de impares, multiplos de 3 entre 1 e 500
s = 0
cont = 0
for i in range (1,501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        cont = cont + 1
print(f'O somatório dos {cont} números múltiplos de 3, entre 1 e 500 é: {s}')


# divisão por 2, restando 1 para verificar que é impar
# divisão por 3, para verificar se é multiplo do mesmo