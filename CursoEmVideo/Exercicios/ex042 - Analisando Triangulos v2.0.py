# Refaça o desafio 32 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilatero: Todos os lados iguais, - Isósceles: dois lados iguais, - Escaleno: todos os lados diferentes

a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if (a < b + c) and (b < c + a) and (c < b + a):
    print('É um triangulo = ', end='')
    if a == b == c:
        print('EQUILÁTERO!!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Não é um triângulo')