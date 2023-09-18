''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do Grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos '''

soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
soma_mulher = 0

for i in range(1, 5):
    print('-'*20, '{}ª PESSOA'.format(i), '-'*20)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip()
    soma_idade += idade
    
    if i == 1 and sexo in 'M m':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'M m' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'F f' and idade < 20:
        soma_mulher += 1

media_idade = soma_idade / 4
print('\nA média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_mais_velho))
print('Existe {} mulheres na lista com menos de 20 anos'.format(soma_mulher))