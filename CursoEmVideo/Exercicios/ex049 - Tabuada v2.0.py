# Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando o laço for

num1 = int(input('Escolha um número para ser multiplicado: '))
num2 = int(input('Escolha até qual número será multiplicado: '))

for i in range(1, num2+1):
    print('{} X {} = {}'.format(num1, i, num1*i))
    num2 -= 1