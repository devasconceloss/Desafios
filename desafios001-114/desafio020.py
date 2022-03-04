from random import shuffle
al1 = input('Digite o nome do 1º aluno: ')
al2 = input('Digite o nome do 2º aluno: ')
al3 = input('Digite o nome do 3º aluno: ')
al4 = input('Digite o nome do 4º aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)