from time import sleep


def maior(*num):
    print(f'\nAnalisando os números fornecidos...')
    sleep(1)
    if len(num) == 0:
        print('Nenhum número foi cadastrado!')
    else:
        print(f'Foram cadastrandos {len(num)} números e o maior foi: {max(num)}')

maior(1, 2, 4, 7)
maior()
maior(1000, 12, 15, 13)
maior(1000000, 0, 1)

