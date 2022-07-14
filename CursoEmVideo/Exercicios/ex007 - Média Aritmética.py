# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média

print('='*50)
print('Exercício 7')
print('='*50)

prof = input('Por favor insira o nome do professor: ')
aluno = input('Inira o nome do Aluno avaliado: ')

n1 = float(input('Insira a Primeira nota: '))
n2 = float(input('Insira a Segunda nota: '))
nf = (n1 + n2) / 2  #Para calcular a média

print('Prof {0} o(a) aluno(a) {1} ficou com uma média de {2:.2f} '.format(prof, aluno, nf))

if nf >= 7:
    print('O(A) Aluno(a) {} foi Aprovado(a)!'.format(aluno))
else:
    print('O(A) Aluno(a) {} foi Reprovado(a)!'.format(aluno))