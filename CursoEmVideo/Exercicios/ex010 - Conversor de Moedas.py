# Crie um programa que leia quanto dinheiro a pessoa tem em sua carteira e mostre quantos dolares ela pode comprar

print('='*50)
print('Exercício 10')
print('='*50)

nome = input('Qual seu nome: ')
din = float(input('Senhor(a) {} poderia informar quanto você tem em sua carteira: '.format(nome)))

dol = din / 5.60

print('Senhor(a) {} com o dinheiro que você tem em sua carteira, que é igual a R${}, você consiguirá comprar US${:.2f}'.format(nome, din, dol))