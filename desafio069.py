
'''
A) quantas pessoas tem mais de 18
B) quantos homens cadastrados
C) quantas mulheres tem menos de 20
'''

cont1 = cont2 = cont3 = 0

print('----' * 10)
print('Cadastre uma pessoa:')
print('----' * 10)

while True:

    while True:

        s = str(input('SEXO M/F: ')).lower()
        if s in 'mf':
            break

    i = int(input('Digite a idade: '))
    c = str(input('Deseja cadastrar mais uma pessoa? ')).lower()

    if i > 18:
        cont2 += 1
    if s == 'm':
        cont1 += 1
    if s == 'f' and i > 20:
        cont3 += 1

    if c == 'n':
        print('FIM DE PROGRAMA! ')
        break



print(f'{cont2} pessoas com mais de 18 foram cadastradas, {cont1} homens foram cadastrados, {cont3} mulher(es) com mais de 20 anos foram cadastrada(s)')



