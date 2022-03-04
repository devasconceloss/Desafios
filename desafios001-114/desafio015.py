dias=int(input('Por quantos dias você alugou o carro? '))
km=float(input('Quantos kilometros foram percorridos? '))
custo=dias*60+(km*0.15)
print(f'Tendo utilizado o carro por {dias} dias e percorrido {km}Km, o custo total é de R${custo}')