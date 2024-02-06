'''
Crie um programa que leia varios números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999. No final mostre quantos números foram digitados e qual foi a soma entre eles
'''

print('-'*30)
print('Soma de vários valores')
print('-'*30)

soma = 0
cont = 0

while True:
    numero = int(input('Digite um número: (999 para sair) '))
    
    if numero == 999:
        break
    
    else:
        soma += numero
        cont += 1
        

print(f'A soma dos {cont} números é igual a {soma}')