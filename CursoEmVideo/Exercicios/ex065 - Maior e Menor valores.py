'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

contar = 0
soma = 0
maior = 0
menor = 0

while True:
    numero = float(input('Digite o número: '))
    soma += numero
    contar += 1

    if numero > maior:
        maior = numero
    
    elif numero > menor:
        menor = numero

    opcao = str(input('Digite S para continuar e qualquer outra tecla para sair: ')).upper()
    if opcao == 'S':
        continue

    else:
        break


media = soma / contar

print(f'Sua média foi: {media:.2f} \nO maior número foi {maior} e o menor número foi {menor}')