# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('='*50)
print('Exercício 15')
print('='*50)

km = float(input('Quantos Km foram percorridos: '))
dia = int(input('Quantos dias o carro ficou alugado: '))

pago = (dia * 60) + (km * 0.15)

print('O valor que será pago pelo aluguel do carro será de R${:.2f}'.format(pago))