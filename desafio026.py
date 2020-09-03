frase = str(input('Digite uma frase por favor: ')).lower().strip()
letra = str(input('Digite a letra que você deseja procurar: '))
print(f'A letra {letra} aparece {frase.count(letra)} vezes, ela aparece pela primeira vez na posição {frase.find(letra)} e aparece pela última vez na posição {frase.rfind(letra)} ')