# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# utilizando biblioteca math

import math

print('='*50)
print('Exercício 17 - Catetos e Hipotenusa')
print('='*50)


cateto_op = float(input('Comprimento Cateto Oposto: '))
cateto_ad = float(input('Comprimento Cateto Adjacente: '))

print(f'com soma do {cateto_op} com {cateto_ad} a hipotenusa vai medir: {math.hypot(cateto_op,cateto_ad):.2f}')

# math.hypot(x,y) é utilizado para calcular a hipotenusa


#sem utilizar nenhuma biblioteca
cateto_op = float(input('\nComprimento Cateto Oposto: '))
cateto_ad = float(input('Comprimento Cateto Adjacente: '))
hipotenusa = (cateto_op ** 2 + cateto_ad ** 2) ** (1/2)

print(f'com soma do {cateto_op} com {cateto_ad} a hipotenusa vai medir: {hipotenusa:.2f}')