# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
total = 0

for i in range (1, num + 1):
    if num % i == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(i, end= ' ')
print('\nO número {} foi divisivel {} vezes' .format(num, total))

if total == 2:
    print('Por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')