# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('='*50)
print('Exercício 30 – Par ou Ímpar?')
print('='*50)

numero =  int(input('Digite um número inteiro: '))

if numero%2:
    print(f'O número {numero} é Impar')
else:
    print(f'O número {numero} é Par')

# Todo numero par quando é dividido por 2 tem resto 0