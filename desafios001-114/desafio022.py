nome = str(input("Digite seu nome completo por favor: ")).strip()
print(f"O seu nome com letras maiúsculas é {nome.upper()}, já em letras minúsculas é {nome.lower()}")
print(f"O seu nome possui {len(nome) - nome.count(' ')} letras")
# comando strip elimina espaços antes e depois da string, mas não entre
# comando count neste exemplo, conta os espaços na string e os elimina na subtração do len