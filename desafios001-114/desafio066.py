
n = s = 0

while True:
    n = int(input('Digite um número inteiro por favor: '
                  '\nSe desejar interromper o programa digite 999'))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitos equivale a {s}')