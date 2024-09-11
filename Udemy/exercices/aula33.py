"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input('Enter your first name: ')

if len(first_name) <= 4:
    print(f'The name {first_name} is short')

elif len(first_name) <= 6:
    print(f'The name {first_name} is normal')

else:
    print(f'The name {first_name} is too big')
