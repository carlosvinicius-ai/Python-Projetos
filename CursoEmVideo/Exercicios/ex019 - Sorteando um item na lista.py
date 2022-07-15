# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#meu metodo

import random

print('='*50)
print('Exercício 19 - Sorteando um item na lista')
print('='*50)

alunos = ['Carlos', 'Junior', 'Thata', 'Roberto']

aluno = random.randrange(0, len(alunos))     # para aleatorizar seguindo o tamanho do arquivo
aluno_secreto = alunos[aluno]   # para passar a variavel para o valor do aluno
print(f'O Aluno escolido foi {aluno_secreto}')

'''

random.randrange(start, stop[, step])
Retorna um elemento selecionado aleatoriamente em range(start, stop, step). Isso é equivalente a choice(range(start, stop, step)), mas na verdade não cria um objeto range.

O padrão de argumento posicional corresponde ao de range(). Os argumentos nomeados não devem ser usados porque a função pode usá-los de maneiras inesperadas.

Alterado na versão 3.2: randrange() é mais sofisticado em produzir valores igualmente distribuídos. Anteriormente, usava um estilo como int(random()*n), que poderia produzir distribuições ligeiramente desiguais.

'''

#outro metodo

n1 = input('Primeiro Aluno: ').title()
n2 = input('Segundo Aluno: ').title()
n3 = input('Terceiro Aluno: ').title()
n4 = input('Quarto Aluno: ').title()

lista = [n1, n2, n3, n4]
aluno_escolhido = random.choice(lista)
print(f'O Aluno escolido foi {aluno_escolhido}')

'''
random.choice(seq)
Retorna um elemento aleatório da sequência não vazia seq. Se seq estiver vazio, levanta IndexError.
'''