import random
al1 = input('Digite o nome do aluno nº1: ')
al2 = input('Digite o nome do aluno nº2: ')
al3 = input('Digite o nome do aluno nº3: ')
al4 = input('Digite o nome do aluno nº4: ')
alunos = [al1, al2, al3, al4]
print(f'O aluno escolhido para apagar o quando foi {random.choice(alunos)}')

