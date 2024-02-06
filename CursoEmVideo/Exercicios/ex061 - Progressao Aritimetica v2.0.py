'''
Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
'''

print('Gerador de PA')
print('-'*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
count = 1

while count <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    count += 1
    
print('FIM')