doc = dict()

doc['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
doc['Idade'] = 2020 - ano
doc['CTPS'] = int(input('Carteira de trabalho (0 = Não tenho): '))


if doc['CTPS'] == 0:
    for k, v in doc.items():
        print(f'{k} tem o valor {v}')

else:
    act = int(input('Ano de contratação: '))
    doc['Aposentadoria'] = (act - ano) + 35
    doc['Salário'] = float(input('Salário: '))

    for k, v in doc.items():
        print(f'{k} tem o valor {v}')
