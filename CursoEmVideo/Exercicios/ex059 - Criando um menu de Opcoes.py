'''
Crie um programa que leia 2 valores e mostre um menu na tela
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    menu = int(input('''
Escolha uma opção
1 - Somar
2 - Multiplicar
3 - Maior número
4 - novos números
5 - Sair do Programa
Opção: '''))
    
    if menu == 1:
        soma = num1 + num2
        print('A soma do {} + {} = {}'.format(num1, num2, soma))
    elif menu == 2:
        multiplica = num1 * num2
        print('A multiplicação do {} X {} = {}'.format(num1, num2, multiplica))
    elif menu == 3:
        if num1 > num2:
            print('O primeiro valor é MAIOR que o segundo')
        elif num2 > num1:
            print('O segundo valor é MAIOR que o primeiro')
        else:
            print('Os dois valores são iguais')
    elif menu == 4:
        num1 = int(input('Digite o novo primeiro valor: '))
        num2 = int(input('Digite o novo segundo valor: '))
    elif menu == 5:
        print('Saindo do programa... ')
    else:
        print('Digite um valor válido!')

print('Obrigado por utilizar nosso sistema!!')