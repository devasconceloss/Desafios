#ler data de nascimento e informar se ele vai se alistar ou se ja passou do tempo e o quanto passou

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Essa é a hora de se alistar')
elif idade > 18:
    print(f'Já passou {idade - 18} anos do tempo ')
else:
    print(f'Ainda faltam {18 - idade} para você se alistar')



