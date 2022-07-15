# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


# utilizando a biblioteca math

from math import trunc

print('='*50)
print('Exercício 16 - Quebrando Numero')
print('='*50)

num = float(input('Digite um valor: '))

print(f'O valor real é {num} e sua porção inteira é {trunc(num)}') #utilizado para arredondar

#match.ceil() é utilizado para arredondar para cima

#sem utilizar nenhuma biblioteca

num = float(input('\nDigite um valor: '))

print(f'O valor real é {num} e sua porção inteira é {int(num)}')