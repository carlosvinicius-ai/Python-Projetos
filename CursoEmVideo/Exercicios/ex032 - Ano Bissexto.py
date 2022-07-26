# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('='*50)
print('Exercício 32 – Ano Bissexto')
print('='*50)

ano = int(input('Digite o Ano que quer analisar (Coloque 0 para analisar o ano Atual): '))

if ano == 0:
    ano = date.today().year #mudará a variavel ano para a data atual

if (ano%4 == 0 and ano%100 != 0) or (ano%400==0):
    print(f'{ano} É um ano Bissexto!')
else:
    print(f'{ano} Não é um ano Bissexto!')