from math import sqrt, pow
cop =int(input('Digite quanto mede o cateto oposto: '))
cad =int(input('Digite quanto mede o cateto adjacente: '))
sum = pow(cop,2) + pow(cad,2)
hip = sqrt(sum)
print(f'O cateto oposto mede {cop}, o cateto adjacente mede {cad}, sendo a hipotenusa mede {hip}')

