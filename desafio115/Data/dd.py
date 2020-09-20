def leia_int(msg):
    """
    Função de tratamento de variáveis, se o input não for o valor inteiro o programa não
    prosseguirá com seu fluxo.
    :param msg: varivael a ser lida
    :return: n1
    """
    while True:
        n1 = input(msg)
        try:
            n1 = int(n1)
        except (ValueError, TypeError):
            print(f'\033[0;30;41mHouve problemas com o valor ou tipo do dado informado.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mO usuário interrompeu o programa ou não digitou nada,'
                  ' por padrão atribuiremos 0 a variável.\033[m')
            return 0
        else:
            return n1


def leia_float(msg):
    """
    Função de tratamento de variáveis, se o input não for o valor inteiro o programa não
    prosseguirá com seu fluxo.
    :param msg: variavel a ser analisada
    :return: n2
    """
    while True:
        n2 = input(msg)
        try:
            n2 = float(n2)
        except (ValueError, TypeError):
            print(f'\033[0;30;41mHouve problemas com o valor ou tipo do dado informado.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mO usuário interrompeu o programa ou não digitou nada, '
                  'por padrão atribuiremos 0 a variável.\033[m')
            return 0
        else:
            return n2



def armazenandodados():
    store = open('dados.txt', 'a')
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = dd.leia_float('Idade: ')
    geral.append(cadastro.copy())
    store.write(f"{cadastro['Nome']},{cadastro['Idade']}")
    store.close()
    geral.clear()


def lendodados():
    store = open('dados.txt', 'r')
    for i in store.readlines():
        print(f'\n{i}')
        print('anos', end='')


