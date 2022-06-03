n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 % n2
e = n1 ** n2

print('O valor da soma é: {0}, O valor da multiplicação é: {1}, o valor da divisão é: {2:.3f}.'.format(s, m, d))
print('O valor do Resto é: {0}, O valor da pontecialização é: {1}'.format(di, e))