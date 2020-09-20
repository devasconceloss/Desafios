# FUNCTIONS TO DO: OPEN, LOAD, SAVE, CABEÇALHO, INCREMENTO.
from desafio115.Data.dd import leia_int
arquivo = 'dados.txt'

def arquivo_existe(arquivo):
    try:
        s = open(arquivo, 'rt')
        s.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(arquivo):
    try:
        s = open(arquivo, 'wt+')
        s.close()
    except:
        print('Houve um erro na criação')
    else:
        print(f'O arquivo {arquivo} foi criado.')



def armazenando_dados(arquivo, nome='Inexistente', idade=0):
    try:
        s = open(arquivo, 'at')
        s.write(f'{nome},{idade}\n')
        s.close()
    except FileNotFoundError:
        print('Houve um problema na hora de abrir o arquivo;')
    else:
        print('Dados cadastrados com sucesso.')




def lendo_dados(arquivo):
    try:
        s = open(arquivo, 'rt')
    except:
        print('Erro ao ler o banco de dados.')
    else:
        print('Pessoas cadastradas')
        print(s.readlines())



def cabecalho():
    titulo = 'MENU PRINCIPAL'
    linha = '---'*11

    print(linha)
    print(titulo.center(33))
    print(linha)
    print('\n1. Cadastrar mais uma pessoa.'
          '\n2. Ver pessoas cadastradas.'
          '\n3. Encerrar programa.')
    print(linha)
    while True:
        choice = str(input('Escolha operação a ser feita: '))
        if choice in '123':
            if choice == '1':
                nome = str(input('Nome: '))
                idade = leia_int('Idade: ')
                armazenando_dados(arquivo, nome, idade)
                return cabecalho()
            if choice == '2':
                lendo_dados(arquivo)
            if choice == '3':
                print('Fim de programa')
                break
        else:
            print('\nEscolha uma opção válida.')
            return cabecalho()



