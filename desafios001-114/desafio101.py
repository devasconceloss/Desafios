
def voto(nascimento, ano_atual):
    """
    --> Função para checar seu status em relação a voto e eleições
    :param nascimento: Seu ano de nascimento, exemplo: 1996
    :param ano_atual: Ano vigente, exemplo: 2020
    :return:
    """
    s = ano_atual - nascimento
    if 18 <= s <= 70:
        print(f'Com {s} anos o voto é obrigatório')
    if 16 <= s < 18:
        print(f'Com {s} anos o voto é opcional')
    if s < 16 or s > 70:
        print(f'Com {s} anos você não vota')

voto(nascimento= int(input('Em que ano você nasceu? ')), ano_atual= int(input('Em que ano nós estamos? ')))