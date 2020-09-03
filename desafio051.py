# Progressão aritmética
pn = int(input('Digite o primeiro termo da P.A: '))
rz = int(input('Digite a razão/constante desta P.A: '))
tm = int(input('Quantos termos vc deseja ver? '))
n=0
print(pn)
for i in range (pn,pn + (tm - 1)*rz,rz):
    print(f'{i} + {rz} = {i+rz}')

