# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print('-'*20)
print('CONTAGEM DE NÚMEROS PARES')
print('-'*20)

for i in range(1, 51):
    if (i % 2) == 0:
        print(i, end=' ')

print('ACABOU A CONTAGEM')