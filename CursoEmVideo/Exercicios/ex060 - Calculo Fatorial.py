'''
Faça um programa que leia um número qualquer e mostre seu fatorial
Ex: 5! = 5x4x3x2x1 = 120
'''

n = int(input('Digite o número que deseja fatoriar: '))
resultado = 1
count = 1

while count <= n:
    resultado *= count
    count += 1

print(resultado)
