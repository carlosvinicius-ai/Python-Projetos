"""Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag) """


soma = contar = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))
    
    if num == 999:
        break
    
    contar += 1
    soma += num
    
    
print(f'foram digitados {contar} e soma deles é igual a {soma}')