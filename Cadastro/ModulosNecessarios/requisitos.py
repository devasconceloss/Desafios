# Aqui estarão todas as funções necessárias pra o cadastro funcionar

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


def linhas():
    print('---' * 11)


def format_cabecalho(msg):
    """
    -> Assim como a função linha esta também possui apenas um valor visual, deixando a msg entre linhas, destacando a
    mesma.
    :param msg:
    :return:
    """

    linhas()
    print(msg.center(33))
    linhas()


def criando_arquivo():
    """
    -> Função para criação de um arquivo txt, neste caso o dados.txt, formulei o algoritmo desta forma para que ele não
    ficasse recriando o mesmo arquivo e perdendo os dados do mesmo. Anteriormente eu tinha feito uma função que criava
    um arquivo txt de acordo com a escolha de nome pelo usuario.
    :return:
    """
    format_cabecalho('Criando arquivo')
    arquivo = 'dados.txt'
    try:
        data = open(arquivo, 'wt+')
        data.close()
    except FileExistsError:
        print(f'Não foi possivel criar o arquivo: {arquivo}')
    else:
        print(f'{arquivo} criado com sucesso!')


def menu():
    """
    -> Função que te mostra as opções possiveis neste sistema
    :return: Te encaminha para função escolha
    """
    format_cabecalho('MENU PRINCIPAL v3.0')
    escolhas = ['Cadastrar uma pessoa', 'Ver pessoas cadastradas', 'Sair do programa']
    for i in range(3):
        print(f'{i+1}. {escolhas[i]}')
        i += 1
    linhas()
    choices()


def choices():
    """
    -> Aqui você decidirá o que fazer
    :return: Se a opção escolhida não for válida vc retornará para as opções.
    """
    opc = str(input('Escolha uma ação a ser feita: '))
    while True:
        if opc in '123':
            if opc == '1':
                format_cabecalho('Cadastrando mais uma pessoa')
                nome = str(input('Nome: '))
                idade = leia_int('Idade: ')
                data = open('dados.txt', 'at')
                data.writelines(f'{nome}; {idade}\n')
                data.close()
                return menu()
            if opc == '2':
                try:
                    data = open('dados.txt', 'r')
                    format_cabecalho('Pessoas cadastradas')
                    for linha in data:
                        dados = linha.split('; ')
                        dados[1] = dados[1].replace('\n', '')
                        print(f'{dados[0]:<25}{dados[1]} Anos')
                    data.close()
                except (FileExistsError, FileNotFoundError):
                    print('Não foi possivel fazer a leitura do arquivo')
                else:
                    return menu()
            if opc == '3':
                format_cabecalho('Fim de programa')
                break
        else:
            print('Opção inválida.')
            return choices()
