# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

print('='*50)
print('Exercício 13 - Reajuste Salarial')
print('='*50)

nome = input('Insira o nome do funcionário: ')
v1 = float(input('Insira o Salário atual dele: R$'))
p = float(input('Insira quantos % de aumento terá: '))
vd = v1 + (v1*p/100)

print('O Funcionário {} tinha o salário de R${} e com o aumento de {}% agora recebe R${:.2f}'.format(nome, v1, p, vd))