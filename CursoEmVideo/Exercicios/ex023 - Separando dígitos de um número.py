# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('='*50)
print('Exercício 23 – Separando dígitos de um número')
print('='*50)

numero = int(input('Digite um valor entre 0 e 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10


print(f'Analisando o número {numero}')
print(f'a milhar é: {m}')
print(f'a centena é: {c}')
print(f'a dezena é: {d}')
print(f'a unidade é: {u}')