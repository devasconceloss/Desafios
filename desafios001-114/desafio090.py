aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))

for k,v in aluno.items():
    print(f'{k} é {v}')

if aluno['Média'] <= 5.9:
    print(f'O aluno {aluno["Nome"]} está reprovado')
else:
    print(f'O aluno {aluno["Nome"]} está aprovado')
    if aluno['Média'] == 10:
        print('MEUS PARABÉNS')