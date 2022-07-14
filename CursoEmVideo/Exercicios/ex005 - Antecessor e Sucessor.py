# Faça um programa q calcule um número inteiro e mostre na tela seu sucessor e seu antecessor 

print('='*50)
print('Exercício 5')
print('='*50)

n1 = int(input('Insira um número inteiro: '))

s = n1+1 #para mostrar o sucessor
a = n1-1 #para mostrar o antecessor

print('O número escrito foi: {0}. Seu Sucessor é {1} e seu Antecessor é {2} '.format(n1, s, a))