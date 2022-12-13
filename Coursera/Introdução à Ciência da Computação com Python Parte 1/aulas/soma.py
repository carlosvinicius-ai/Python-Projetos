tamanho = int(input('Digite o tamanho da sequencia de numeros: '))

soma = 1
i = 0

while i < tamanho:
    valor = int(input('digite o valor a ser somado: '))
    soma = soma + valor
    i += 1
    
print('a soma dos valores digitados é:', soma)