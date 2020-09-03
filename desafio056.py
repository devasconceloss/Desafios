''' nome, idade e sexo de 4 pessoas
media da idade, nome do homem mais velho,
quantas mulheres possuem MENOS de 20 anos'''

Sidade = 0
midade = 0
nomev = ''
cont = 0

for i in range(1,5):
    print(f'------------{i}ª Pessoa------------')
    nome = str(input('Diga-me seu nome: ')).upper()
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo? [M/F] ')).upper()
    Sidade += idade
    mdi = (Sidade)/4
    if i == 1 and sexo == 'M':
        midade = idade
        nomev = nome
    if sexo == 'M' and idade > midade:
        midade = idade
        nomev = nome
    if sexo == 'F' and idade < 20:
        cont += 1

print(f'A média de idade do grupo é {mdi}, possuindo {cont} mulheres com menos de 20 anos, o homem mais velho é o {nomev} que possui {midade} anos')
