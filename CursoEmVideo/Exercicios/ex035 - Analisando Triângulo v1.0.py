# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('='*50)
print('Exercício 35 – Analisando Triângulo v1.0')
print('='*50)

a = float(input('\nDigite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if (a < b + c) and (b < c + a) and (c < b + a):
    print('É um triangulo')
else:
    print('Não é um triângulo')