
times = (
    "Palmeiras",
    "Gremio",
    "Atletico-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "Sao Paulo",
    "Cuiaba",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goias",
    "Coritiba",
    "America-MG"
)

print('-'*30)
print(f'Lista de times {times}')
print('-'*30)


print(f'Os 5 primeiros times do Brasileirão: {times[0:5]}')
print('-'*30)

print(f'Os 4 ultimos times são: {times[-4:]}')
print('-'*30)

print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-'*30)

print(f'O Vasco está na {times.index("Vasco") + 1} posição')

