# Crie um programa que faça o computador jogar jokenpo com você

import random as rd
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = rd.randint(0, 2)
print(''' 
SUAS OPÇÕES
0 - PEDRA
1 - PAPEL
2 - TESOURA
''')
jogador = int(input('Qual sua jogada: '))
print('\nJO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO\n')
time.sleep(0.5)

print('=' * 20)
print('O COMPUTADOR jogou {}.\nO JOGADOR jogou {}.'.format(itens[computador], itens[jogador]))
print('=' * 20)

if computador == 0: # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        ('Opção inválida')

elif computador == 1: # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        ('Opção inválida')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        ('Opção inválida')