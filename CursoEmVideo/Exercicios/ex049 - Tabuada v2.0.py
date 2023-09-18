# Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando o laço for

num1 = int(input('Escolha um número para ser multiplicado: '))
num2 = int(input('Escolha até qual número será multiplicado: '))

for i in range(num2):
    print('{} X {} = {}'.format(num1, num2, num1*num2))
    num2 -= 1