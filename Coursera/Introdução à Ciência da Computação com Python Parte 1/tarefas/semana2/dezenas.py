numero = int(input('Digite um número inteiro: '))
unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10

print('O dígito das dezenas é', dezena)