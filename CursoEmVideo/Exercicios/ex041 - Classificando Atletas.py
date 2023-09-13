# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: Mirim, - Até 14 anos: Infantil, - Até 19 anos: Junior, - Até 20 anos: Senior, - Acima: Master

from datetime import date

atual = date.today().year

ano_nascimento = int(input('Ano de nascimento: '))

idade = atual - ano_nascimento

print('A idade do atleta é {}'.format(idade))

if idade <= 9:
    print('categoria MIRIM')
elif idade <= 14:
    print('categoria INFANTIL')
elif idade <= 19:
    print('categoria JUNIOR')
elif idade <= 20:
    print('categoria SENIOR')
else:
    print('categoria MASTER')