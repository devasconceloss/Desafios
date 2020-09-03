from time import sleep

alunos = list()
notas = list()
dados = list()


while True:
    dados.append((str(input('Nome: '))))
    dados.append((float(input('Nota 1: '))))
    dados.append((float(input('Nota 2: '))))
    r = str(input('Desaja continuar [S/N]? ')).lower()

    alunos.append(dados[:])
    notas.append(dados[1])
    notas.append(dados[2])
    dados.clear()

    if r not in 'sn':
        print('Opção inválida, tente novamente')
        r = str(input('Deseja continuar [S/N]? '))
        if r == 'n':
            break
    if r =='n':
        break

print('-=-'*10)
print('      BOLETIM FINAL ')
print('-=-'*10)


for i, v in enumerate(alunos):
    print(f'\n{i:<4} {alunos[i][0]:<10}   {(alunos[i][1] + alunos[i][2])/2:<4}')
print('-=-'*10)
while True:
    n = int(input('\nQuer ver as notas de qual aluno? (999 interrompe) '))
    if n == 999:
        print('Finalizando processo...')
        sleep(2)
        print('OBRIGADO, VOLTE SEMPRE!!')
        break
    print(f'As notas do(a): {alunos[n][0]} são estas: {alunos[n][1],alunos[n][2]} ')



