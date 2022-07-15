# Faça um programa que leia o preço de um produto e mostre este produto com 5% de desconto

print('='*50)
print('Exercício 12 - Calculando Descontos')
print('='*50)

v1 = float(input('Insira o valor do produto: R$'))
p = float(input('Insira a porcentagem do desconto: '))

vd = v1 - (v1*p/100)

print('O valor do produto era R${} e com o desconto de {}% é igual a R${:.2f}'.format(v1, p, vd))