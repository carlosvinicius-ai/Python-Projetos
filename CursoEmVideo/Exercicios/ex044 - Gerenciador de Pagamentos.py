# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento: - Avista dinheiro: 10% de desconto, - Avista no cartão: 5% de desconto, até 2x no cartão preço normal, - 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: R$'))
print('''
Escolha uma das opções:
1 - Avista dinheiro
2 - Avista Cartão
3 - Até 2x no Cartão
4 - 3x ou mais no Cartão
''')
opcao = int(input('Opção: '))

print('O produto sairá no valor de ', end='')

if opcao == 1:
    valor = valor_produto * 0.9
    print('R${:.2f}'.format(valor))
elif opcao == 2:
    valor = valor_produto * 0.95
    print('R${:.2f}'.format(valor))
elif opcao == 3:
    print(print('R${:.2f}'.format(valor_produto)))
elif opcao == 4:
    valor = valor_produto * 1.20
    print('R${:.2f}'.format(valor))
else:
    print('R$ invalido')