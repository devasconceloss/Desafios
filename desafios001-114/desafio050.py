# leitura de 6 numeros inteiros e soma apenas dos pares
s = 0
cont = 0
for i in range (1,7):
    n = int(input('Digite um número por favor: '))
    if n % 2 == 0:
        cont += 1
        s += n

print(f'A soma dos {cont} número(s) par(es) é: {s}')


