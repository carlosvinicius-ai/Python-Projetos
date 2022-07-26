# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from re import A


print('='*50)
print('Exercício 33 – Maior e menor valores')
print('='*50)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

menor = n1
maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

print(f'O menor número é {menor} e o maior número é {maior}')