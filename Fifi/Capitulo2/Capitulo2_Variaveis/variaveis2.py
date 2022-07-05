responsavel = input('Digite o nome do responsavel: ')
funcionario = input('Digite o nome do funcionario: ')
empresa = input('Digite o nome da empresa: ')
valor = float(input('Digite o valor da entrada: '))

print('Declaro para o senhor {} que o senhor {} esteve presente no evento {} e gastou o valor de R${} com a entrada'.format(responsavel, funcionario, empresa, valor))