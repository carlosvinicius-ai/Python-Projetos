'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
'''

print('Gerador de PA')
print('-'*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
count = 1
total = 0
mais = 10

while mais != 0:

    total += mais
    
    while count <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        count += 1
        
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
    

print(f'Programa finalizado foram mostrados {count} termos no total')