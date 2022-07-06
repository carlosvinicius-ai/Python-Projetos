# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
print('Exercício 8')
print('='*50)

m = float(input('Insira um valor em Metros: '))
cm = m*100
mm = m*1000

print('o valor em Metros é {}M em centimetros é {}cm e em milimetros é {}mm'.format(m, cm, mm))