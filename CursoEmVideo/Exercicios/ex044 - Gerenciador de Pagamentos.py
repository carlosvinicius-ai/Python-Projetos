# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento: - Avista dinheiro: 10% de desconto, - Avista no cartão: 5% de desconto, até 2x no cartão preço normal, - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS CARLIN '))
valor_produto = float(input('Digite o valor do produto: R$'))
print('''
Escolha uma das opções:
1 - Avista dinheiro
2 - Avista Cartão
3 - Até 2x no Cartão
4 - 3x ou mais no Cartão
''')
opcao = int(input('Opção: '))

if opcao == 1:
    valor = valor_produto * 0.9
elif opcao == 2:
    valor = valor_produto * 0.95
elif opcao == 3:
    valor = valor_produto
    parcela = valor / 2
    print('Sua compra será em 2x com cada parcela no valor R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    valor = valor_produto * 1.20
    numero_parcela = int(input('Digite o número de parcelas: '))
    parcela = valor / numero_parcela
    print('Sua compra será em {}x com cada parcela no valor R${:.2f} COM JUROS.'.format(numero_parcela, parcela))
else:
    valor = 0
    print('Digite um valor válido')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_produto, valor))