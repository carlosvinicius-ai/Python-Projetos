# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('='*50)
print('Exercício 20 - Sorteando uma ordem na lista')
print('='*50)

n1 = input('Primeiro Aluno: ').title()
n2 = input('Segundo Aluno: ').title()
n3 = input('Terceiro Aluno: ').title()
n4 = input('Quarto Aluno: ').title()

alunos = [n1, n2, n3, n4]

shuffle(alunos)

print(f'a ordem de apresentação será:')
print(alunos)