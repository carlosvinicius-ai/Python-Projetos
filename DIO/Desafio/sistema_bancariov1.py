menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3

while True:

    opcao = input(menu)
    
    if opcao == 'd':
        
        valor = float(input('\nDigite o valor que deseja depositar: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito R$ {valor:.2f}\n'
            
        else:
            print('Digite um valor acima de R$0.00')
            continue
        
    
    elif opcao == 's':
        
        valor = float(input('\nDigite o quanto deseja sacar: '))
        
        if numero_saque >= limite_saque:
            print('Limite de saque diáario atingido!')
        
        elif valor > saldo:
            print('Não é possível sacar o dinheiro por saldo insuficiente')
            
            
        elif valor > limite:
            print('valor de saque maior que o limite')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f} \n'
            numero_saque += 1
        
        else:
            print('Digite um valor válido')
        
    elif opcao == 'e':
        print('EXTRATO'.center(20, '#'))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('#' * 20)
    
    elif opcao == 'q':
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')