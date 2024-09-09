# Faça um programa que calcule o IMC

name = 'Carlos Vinicius'
height = 1.77
weight = 82.35
imc = weight / (height**2) # IMC -> peso / (altura * altura)

print(name, 'have', height, 'meters, ', end='')
print('weigths', weight, 'kilos and you IMC is ', end='')
print(imc)