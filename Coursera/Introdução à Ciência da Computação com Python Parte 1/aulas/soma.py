print('Digite uma sequencias de valores terminada por zero')

soma = 0
valor = 1

while valor != 0:
    valor = int(input('digite o valor a ser somado: '))
    soma = soma + valor
    
print('a soma dos valores digitados é:', soma)