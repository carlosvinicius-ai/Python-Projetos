'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter o valor correto
'''

sexo = input('Informe o seu sexo: ').strip().upper()[0]

while sexo not in 'M F':
    sexo = input('Dados inválidos, Informe o seu sexo: ').strip().upper()[0]

print('O sexo {} foi registrado com sucesso'.format(sexo))