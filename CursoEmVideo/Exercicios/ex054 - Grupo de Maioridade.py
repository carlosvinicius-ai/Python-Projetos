# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores

from datetime import date

menor = 0
maior = 0
atual = date.today().year

for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1

print('{} ainda não atingiram a maioridade e {} já são maiores'.format(menor, maior))