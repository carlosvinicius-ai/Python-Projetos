# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('='*50)
print('Exercício 27 – Primeiro e último nome de uma pessoa')
print('='*50)

nome = str(input('Digite seu nome completo: ')).strip().title()
nomes =  nome.split()

print('Seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu ultimo nome é: {}'.format(nomes[len(nomes) - 1]))