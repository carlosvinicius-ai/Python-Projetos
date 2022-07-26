# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('='*50)
print('Exercício 25 – Procurando uma string dentro de outra')
print('='*50)

nome = str(input('Digite seu nome completo: ')).strip().upper()

print('Seu nome tem Silva?' .format({'SILVA' in nome}))