import urllib
import urllib.request

def teste_conexão():
    try:
        site = urllib.request.urlopen('https://www.python.org/')
    except urllib.error.URLError:
        print('Não foi possivel acessar site')
    else:
        print('Tudo ok')

teste_conexão()