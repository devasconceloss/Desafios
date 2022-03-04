n1 = int(input('Digite um número por favor: '))
n2 = int(input('Digite outro número por favor: '))
n3 = int(input('Digite outro número por favor: '))
if n3 < n2 and n1:
    print(f'{n3} é o menor digito')
if n2 < n1 and n3:
    print(f'{n2} é o menor digito')
if n1 < n2 and n3:
    print(f'{n1} é o menor digito')