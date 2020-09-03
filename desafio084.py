galera = list()
dados = list()
pesos = list()

maiorp = menorp = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    r = str(input('Deseja continuar [S/N]? ')).lower()
    galera.append(dados[:])
    pesos.append(dados[1])
    dados.clear()
    if r == 'n':
        break
    while True:
        if r not in 'sn':
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
            r = str(input('Deseja continuar [S/N]? ')).lower()
        if r == 'n' or r == 's':
            break

for p in galera:
    if p[1] == max(pesos):
        print(f'\n{p[0]} foi a pessoa cadastrada com maior peso, {p[1]}kg')
    if p[1] == min(pesos):
        print(f'\n{p[0]} foi a pessoa cadastrada com menor peso, {p[1]}kg')

print(f'Foram cadastrada(s) {len(galera)} pessoa(s)')
