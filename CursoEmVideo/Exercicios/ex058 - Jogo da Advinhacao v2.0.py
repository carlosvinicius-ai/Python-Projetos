'''
Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer
'''

import random as rd

number = rd.randint(1, 10)
soma = 1
print('Estou pensando em um numero entre 1 e 10, em qual numero eu pensei?')
chute = int(input('Digite um numero de 1 a 10: '))

while chute != number:
    chute = int(input('Chute errado, Digite um numero de 1 a 10: '))
    soma += 1

print('VOCÊ ACERTOU, o número era {} e você acertou após {} tentativas'.format(number, soma))