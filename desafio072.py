contagem = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS','DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

choice = int(input('Escolha um número entre 0 e 20: '))
if choice > 20 or choice < 0:
    print('Você digitou um valor não correspondente, tente novamente')
    choice = int(input('Escolha um número entre 0 e 20: '))
print(f'O digito escolhido foi: {contagem[choice]}')