tamanho = int(input('Digite o tamanho da sequencia de numeros: '))


produto = 1
i = 0

while i < tamanho:
    valor = int(input('digite o valor a ser multiplicado: '))
    produto= produto * valor
    i = i + 1
    
print('a soma dos valores digitados é:', produto)