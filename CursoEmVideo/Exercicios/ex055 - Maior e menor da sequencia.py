# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

peso_lista = []

for i in range(1, 6):
    peso = float(input('Digite o peso em KG da {}ª pessoa: '.format(i)))
    peso_lista.append(peso)

print('O maior peso registrado foi {:.1f}KG e o menor peso registrado foi {:.1f}KG'.format(max(peso_lista), min(peso_lista)))