# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Qual o Valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos_pagar = int(input('Em quantos anos você vai pagar? '))

prestacao_mensal = (valor_casa / anos_pagar) / 12

salario_desconto = salario * 0.3

if prestacao_mensal >= salario_desconto:
    print('O empréstimo foi negado')
else:
    print('O empréstimo foi aceito \nA parcela será de R${:.2f}'.format(prestacao_mensal))