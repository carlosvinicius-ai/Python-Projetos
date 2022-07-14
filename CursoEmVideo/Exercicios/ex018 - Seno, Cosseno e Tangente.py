# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

print('='*50)
print('Exercício 18')
print('='*50)

angulo = float(input('Digite o valor do Ângulo: '))

print(f'o valor do ângulo de {angulo}º seu SENO é {math.sin(math.radians(angulo)):.2f} \nseu COSSENO é {math.cos(math.radians(angulo)):.2f} \nsua TANGENTE é {math.tan(math.radians(angulo)):.2f}')

'''
math.radians(x)
Converte o ângulo x de graus para radianos.
math.cos(x)
Retorna o cosseno de x radianos.
math.sin(x)
Retorna o seno de x radianos.
math.tan(x)
Retorna o tangente de x radianos.
'''