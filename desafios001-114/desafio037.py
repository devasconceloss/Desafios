# escreva um programa que leia um nmr qualquer e o converta para bin, hex, octal

n = int(input('Escreva um número por favor: '))
bs = str(input('Escolha uma base de conversão bin, hex ou oct: '))
if bin:
    print(bin(n))
elif hex:
    print(hex(n))
else:
    print(oct(n))
