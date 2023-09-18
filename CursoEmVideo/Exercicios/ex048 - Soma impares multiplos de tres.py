# Faça um programa que calcule a soma entre todos os número impares que são multiplos de três e que se encontram no intervalo de 1 até 500

for i in range (3, 500, 3):
    if (i%2) != 0:
        print(i)
print('ACABOU!')