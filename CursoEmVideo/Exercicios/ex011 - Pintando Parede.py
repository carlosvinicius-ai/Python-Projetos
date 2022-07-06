# Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta ncessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('Exercício 11')
print('='*50)

h = float(input('Insira a Altura da parede em Metros: '))
b = float(input('Insira a Largura da parede em Metros: '))
a = h * b
tinta = a / 2

print('A área da parede é igual a {}m² e será nescessário {}L de tinta'.format(a,tinta))
