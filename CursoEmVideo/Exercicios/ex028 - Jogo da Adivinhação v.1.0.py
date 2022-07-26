# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random, time

print('='*50)
print('Exercício 28 – Jogo da Adivinhação v.1.0')
print('='*50)

numero = random.randrange(0,5)
print('\nEstou pensando em um numero entre 0 e 5, em qual numero eu pensei?')
usuario = int(input('Digite um numero de 0 a 5: '))

print('PROCESSANDO...')
time.sleep(2)

if(usuario == numero):
    print(f'Você acertou, o numero secreto era {numero}')
else:
    print(f'Você perdeu, o numero secreto era {numero}')