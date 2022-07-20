'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

print('='*50)
print('Exercício 22 – Analisador de Textos')
print('='*50)

nome = input('\nDigite seu nome completo: ').strip()
separa = nome.split()

print(f'''Seu nome com todas letras maiuscula é: {nome.upper()}
Seu nome com todas as letras minuscula é: {nome.lower()}
Seu nome tem: {len(nome)- nome.count(' ')} letras
Seu primeiro nome é {separa[0]} tem {len(separa[0])} letras''')

# - nome.count() para diminuir