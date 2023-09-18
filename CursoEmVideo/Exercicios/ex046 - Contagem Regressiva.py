# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0 com uma pausa de 1 segundo entre eles

import time

print('Vai iniciar a contagem regressiva, para os FOGOS!')

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    if i == 1:
        print('='*20)
        print('FELIZ ANO NOVO!!!')
        print('='*20)