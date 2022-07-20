# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('digite o nome de uma cidade: ')).strip().upper()

print(cid[:5] == 'SANTO')