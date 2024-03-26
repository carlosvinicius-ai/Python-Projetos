# importando a biblioteca para chamar a api
import requests
#importando a biblioteca para usar as informações da biblioteca
import json

# importando a biblioteca datetime para armazenar o dia e a hora da cotação
from datetime import datetime

# importando a bilbioteca random para pegar aleatoriamento o valor do dicionário
import random as rd

# criando o arquivo cotação na pasta moedas
try:
    with open('D:/Python-Projetos/Pessoal/moedas_python/moedas/cotacao.csv', 'x') as base:
        base = base.write('moeda,valor,data,hora\n')

except FileExistsError:
    pass

# criando o dicionário para poder utilizar qual moeda eu quiser
moedas = {
    'Dolar': ['USD-BRL', 'USDBRL'],
    'Euro': ['EUR-BRL', 'EURBRL'],
    'Libra': ['GBP-BRL', 'GBPBRL'],
    'Bitcoin': ['BTC-BRL', 'BTCBRL'],
    'Franco': ['CAD-BRL', 'CADBRL'],
    'Doge coin': ['DOGE-BRL', 'DOGEBRL'],
    'Ethereum': ['ETH-BRL', 'ETHBRL'],
    'Peso argentino': ['ARS-BRL', 'ARSBRL'],
    'Boliviano': ['BOB-BRL', 'BOBBRL'],
    'Yuan': ['CNY-BRL', 'CNYBRL']
}

print(f'{' CONVERSOR DE MOEDA ':-^30}')
print('')

# mostrando as opções de moedas no nosso dicionário para o nosso usuário
for moeda in moedas.keys():
    print(f'Digite {moeda} para trazer o valor dela em Real')

# repetindo para aceitar apenas quando o usuário digitar uma moeda que está em nosso dicionário
while True:
    converter = str(input('\nEscolha uma das opções acima (Digite aleatório para caso deseje que seja aleatório): ')).strip().capitalize()
    
    if converter ==  'Aleatório':
        # escolhendo aleatóriamente entre a lista de itens
        converter = rd.choice(list(moedas.keys()))

    elif converter not in moedas:
        continue

    break

# chamando a api de acordo com a moeda escolhida
atual = requests.get(f'https://economia.awesomeapi.com.br/last/{moedas[converter][0]}')

# convertendo em json para poder buscar a informação que desejamos
atual = atual.json()

# buscando o BID da moeda escolhida
# BID é a conversão atual da moeda
valor_atual = atual[moedas[converter][1]]['bid']

# pegando a data atual e formatando ela
data_agora = datetime.now()
data_atual = data_agora.strftime('%d/%m/%Y')
hora_atual = data_agora.strftime('%H:%M:%S')

# armazenando a data atual no nosso arquivo txt
with open('D:/Python-Projetos/Pessoal/moedas_python/moedas/cotacao.csv', 'a') as adicionar:
    adicionar = adicionar.write(f'{converter},R${float(valor_atual):.2f},{data_atual},{hora_atual}\n')


# mostrando para o usuário o valor armazenado

print(f'O valor armazenado na nossa tabela foi: \nA moeda {converter} está valendo R${float(valor_atual):.2f} no dia e hora {data_atual}')