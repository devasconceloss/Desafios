#categorização por ano de nascimento
from datetime import d
dt = datetime.datetime.today()
ano_atual = (dt.year)
nasc = (input('Em que ano você nasceu? '))
if ano_atual - nasc <= 9:
    print('Você esta na categoria Mirim')