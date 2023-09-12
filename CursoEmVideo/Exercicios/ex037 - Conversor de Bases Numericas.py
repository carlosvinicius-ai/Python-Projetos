# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão -  1: binario 2: octal 3: hexadecimal

numero = int(input('Escreva um número inteiro: '))
conversao = int(input('Escolha a base de conversão: \n1 - BINÁRIO \n2 - OCTAL \n3- HEXADECIMAL \nSua opção: '))

if conversao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Por favor insira uma opção válida')