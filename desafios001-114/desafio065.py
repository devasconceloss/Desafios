r = 's'
cont = soma = maior = menor = 0

while r == 's':
    n = int(input('Digite um número por favor: '))
    cont += 1
    soma = soma + n
    if cont == 1:
        atual = menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja digitar outro número? [S/N] ')).lower()

print(f'\n A média dos termos digitados é: {soma/cont}'
      f'\n O maior número digitado foi o :{maior} e o menor foi {menor}')

