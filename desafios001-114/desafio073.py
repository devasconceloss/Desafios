tabela = ('Vasco', 'Coritiba', 'Flu', 'CAM', 'Fla', 'Corinthians', 'Botafogo', 'Sport', 'Grêmio', 'Sâo Paulo', 'Goiás', 'Inter', 'Palmeiras', 'Braga', 'Bahia', 'Ceará', 'CAP', 'ATL GO', 'Santos', 'Fortaleza')

Grêmio = tabela.index('Grêmio') +1

print(f'\nOs primeiros 5 colocados são: {tabela[:5]}'
      f'\nOs ultimos 4 colocados são: {tabela[-4:]}'
      f'\nTimes em ordem alfabética: {sorted(tabela)}'
      f'\nO Grêmio está na {Grêmio}ª posição')