# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final de acordo com a média atingida: - Média abaixo de 5.0: Reprovado, - Média entre 5.0 e 6.9: Recuperação, - Media 7.0 ou superior: Aprovado

nota1 = float(input('Entre com a Primeira nota: '))
nota2 = float(input('Entre com a Segunda nota: '))

media = (nota1 + nota2) / 2

print('A média do aluno foi {} o aluno está:'.format(media))
if media < 5.0:
    print('\033[1;49;31mREPROVADO')
elif media < 6.9:
    print('\033[1;49;34mRECUPERAÇÃO')
else:
    print('\033[1;49;92mAPROVADO')