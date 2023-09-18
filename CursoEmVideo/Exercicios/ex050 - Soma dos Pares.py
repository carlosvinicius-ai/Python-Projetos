# Desenvolva um programa que leia 6 números inteiros e mostre apenas a soma daqueles que forem pares. Se o valor for impar, desconsidere-o

soma = 0
pares = []

for i in range (1, 7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        soma += num
        pares.append(num)

print('A soma de todos valores pares que são {} é igual a {}'.format(pares, soma))