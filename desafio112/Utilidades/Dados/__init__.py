def leia_dinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;33;41mErro, digite um número real\033[m')
        else:
            valido = True
            return float(entrada)
