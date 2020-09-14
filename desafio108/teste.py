from desafio108 import Moeda
num = float(input('Digite um número: '))
aum = float(input('Quantos % deseja acrescer? '))
dim = float(input('Quantos % deseja descrecer? '))

print(f'\nO número digitado foi {Moeda.real(num)};'
      f'\nO dobro equivale á {Moeda.real(Moeda.dobro(num))};'
      f'\nA metade equivale á: {Moeda.real(Moeda.metade(num))};'
      f'\nAcrescendo {aum}% temos: {Moeda.real(Moeda.infla(num, aum))};'
      f'\nDiminuindo {dim}% temos: {Moeda.real(Moeda.dim(num, dim))}.')
