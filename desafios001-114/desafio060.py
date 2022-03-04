''' 4! = 4*3*2*1 = 24
    5! = 5*4*3*2*1 = 120
    n! = n * (n-1)!'''

print('Aqui calcularemos o fatorial do número informado')
def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)
while True:
    x = int(input('Informe um número por favor: '))
    print(f'O fatorial de {x}! é: {fatorial(x)} ')

