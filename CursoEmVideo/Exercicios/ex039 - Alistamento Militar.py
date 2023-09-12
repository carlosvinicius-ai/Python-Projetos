# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: - Se ele ainda vai se alistar, - Se é a hora de se alistar, - Se ja passou da hora de se alistar. Seu programa também deve mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

ano_nascimento = int(input('Informe seu ano de nascimento: '))

idade = 2023 - ano_nascimento

if idade < 18:
    print('Você ainda vai se alistar, falta {} anos'.format(18 - idade))
elif idade > 18:
    print('Ja passou o da hora de se alistar, passou {} anos'.format(idade - 18))
else:
    print('Está na hora de se alistar')
