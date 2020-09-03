
lista = []

for i in range(0, 5):
    n = int(input('Digite um valor inteiro: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista com sucesso!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado à posição {pos}...')
                break
            pos += 1
print(f'Sua lista em ordem: {lista}')