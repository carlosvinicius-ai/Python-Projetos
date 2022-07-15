#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

print('='*50)
print('Exercício 14 - Conversor de Temperatura')
print('='*50)

celsius = float(input('Insira o valor da temperatura em ºC: '))

fah = celsius * 9 / 5 + 32

print('A temperatura de {}ºC em Fahrenheit é {}ºF!!'.format(celsius, fah))