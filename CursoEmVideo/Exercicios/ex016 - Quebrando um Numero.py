# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

print('='*50)
print('Exercício 16')
print('='*50)

num = float(input('Digite um numero qualquer: '))
inteiro = math.ceil(num)    #utilizado para arredondar
print(inteiro)