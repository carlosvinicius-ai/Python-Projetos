nome = input('Digite o nome do cliente: ')
dia = int(input('Digite o dia de vencimento: '))
mes = input('Digite o mês de vencimento: ')
valor = input('Digite o valor da fatura: ')

print('Olá, {} \nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.' .format(nome, dia, mes, valor))