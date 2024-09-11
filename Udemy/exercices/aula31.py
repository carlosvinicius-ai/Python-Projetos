"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input('Enter an integer: ')

try:
    number = int(number)
    if number % 2 == 0:
        print(f'The number {number} is even')

    else:
        print(f'The number {number} is odd')

except:
    print('The value not an integer')