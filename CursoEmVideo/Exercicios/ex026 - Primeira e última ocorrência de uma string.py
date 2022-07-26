# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('='*50)
print('Exercício 26 – Primeira e última ocorrência de uma string')
print('='*50)

letra = str(input('Digite a sua frase: ')).strip().upper()

print('A letra A aparece {} no seu texto' .format(letra.count('A')))
print('Aparece pela primeira vez na posição {}'.format(letra.find('A') + 1)) 
print('Aparece pela ultima vez na posição {}'.format(letra.rfind('A') + 1))