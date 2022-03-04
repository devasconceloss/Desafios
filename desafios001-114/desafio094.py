pessoas = dict()
geral = list()
cont = 0
soma: int = 0

while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('[M/F]: ')).upper()
    pessoas['Idade'] = int(input('Idade: '))
    geral.append(pessoas.copy())
    cont += 1
    soma += pessoas['Idade']
    r = str(input('Deseja continuar [S/N]? ')).lower()
    if r == 'n':
        break
    if r not in 'sn':
        print('Opção inválida')
        r = str(input('Deseja continuar [S/N]? ')).lower()
        if r == 'n':
            break

media = soma/cont

print('-=-'*10)
print('PESSOAS CADASTRADAS')
print('-=-'*10)
print(geral)
print(f'Foram cadastradas {cont} pessoas, a média de idade do grupo é {media} anos')

print('\nPessoas do sexo feminino: ')
for p in geral:
    if p['Sexo'] == 'F':
        print(p['Nome'])

print('\nPESSOAS COM IDADE ACIMA DA MÉDIA DO GRUPO: ')
for p in geral:
    if p['Idade'] > media:
        print(f'{p["Nome"]}')



