# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print('='*50)
print('Exercício 24 – Verificando as primeiras letras de um texto')
print('='*50)

cid = str(input('digite o nome de uma cidade: ')).strip().upper()

print(cid[:5] == 'SANTO')