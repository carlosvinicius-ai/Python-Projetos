nome = input('Digite o nome do funcionário: ')
empresa = input('Digite o nome da empresa: ')
qtdeFuncionarios = int(input('Digite a quantidade de funcionarios: '))
mediaMensalidade = float(input('Digite a media da mensalidade: '))

print('\n{} trabalha na empresa {}'.format(nome, empresa))
print('Possui: {}'.format(qtdeFuncionarios))
print('A média da mensalidade é de {}'.format(mediaMensalidade))