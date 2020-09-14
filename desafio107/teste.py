from desafio107 import Moeda
num = float(input('Digite um número: '))
aum = float(input('Quantos % deseja acrescer? '))
dim = float(input('Quantos % deseja descrecer? '))

print(f'\nO número digitado foi {num}, o dobro equivale á {Moeda.dobro(num)}, a metade equivale á: {Moeda.metade(num)},'
      f' acrescendo {aum}% temos: {Moeda.infla(num, aum)}, diminuindo {dim}% temos: {Moeda.dim(num, dim)}')
