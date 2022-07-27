# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('='*50)
print('Exercício 34 – Aumentos múltiplos')
print('='*50)

salario = float(input('Digite seu salario: R$'))

if salario <= 1250.00:
    print('Seu salario era R${:.2f} e com o aumento de 15% passará a ser R${:.2f}'.format(salario, ((salario * 0.15) + salario)))
else:
    print('Seu salario era R${:.2f} e com o aumento de 10% passará a ser R${:.2f}'.format(salario, ((salario * 0.10) + salario)))