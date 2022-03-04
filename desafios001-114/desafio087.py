matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = list()

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))

print('-=-'*10)
print(f'Analisando a matriz....')
print('-=-'*10)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
    print()

scolu = list()

for p in matriz:
    scolu.append(p[2])
print(f'A soma dos números pares da matriz equivale à: {sum(par)}'
      f'\nA soma dos números da 3ª coluna equivale à: {sum(scolu)}'
      f'\nO maior da 2ª linha é {max(matriz[1])}')
