from desafio109 import Moeda
num = float(input('Digite um número: '))
aum = float(input('Quantos % deseja acrescer? '))
dim = float(input('Quantos % deseja descrecer? '))


print(f'\nO número digitado foi {Moeda.real(num)};'
      f'\nO dobro equivale á {Moeda.dobro(num, False)};'
      f'\nA metade equivale á: {Moeda.metade(num, False)};'
      f'\nAcrescendo {aum}% temos: {Moeda.infla(num, aum, False)};'
      f'\nDiminuindo {dim}% temos: {Moeda.dim(num, dim, False)}')