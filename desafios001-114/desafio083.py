
cont = cont2 = 0

exp = str(input('Digite uma expressão matemática: '))

if '(' in exp:
    cont += 1
if ')' in exp:
    cont2 += 1
print('Analisando.....')

if cont == cont2:
    print('expressão correta!')
else:
    print('Expressão errada!')
