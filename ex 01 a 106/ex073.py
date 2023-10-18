tupla_times = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Bragantino', 'Athletico-PR', 'São Paulo',	'Cuiabá', 'Cruzeiro', 
               'Fortaleza', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco')

print(f'Lista de Times do Brasileirão: {tupla_times}')
print(f'Cinco primeiros: {tupla_times[0:5]}')
print(f'Quatro Últimos: {tupla_times[-1: -5: -1]}')
print(f'Times em ordem alfabética: {sorted(tupla_times)}')
time = 'Bragantino'
print(f'A {time} está na {tupla_times.index(time)}ª posição')