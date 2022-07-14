# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('='*50)
print('Exercício 6')
print('='*50)

n1 = int(input('Digite um número qualquer: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2) #para realizar a raiz quadrada 

print('O numero selecionado foi: {0}, seu dobro é: {1}, seu triplo é: {2} e sua raiz quadrada é {3:.2f}'.format(n1, d, t, r))