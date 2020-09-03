#Detector de palíndromo

pf = str(input('Digite uma palavra ou frase: ')).lower()
palavra = pf.split()
jts = ''.join(palavra)
if jts == jts[::-1]:
    print(f'A frase "{pf}" é um palíndromo')
else:
    print(f'A frase "{pf}" não é um palíndromo')
