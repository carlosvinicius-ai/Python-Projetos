# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('É um PALINDROMO')
else:
    print('Não é um PALINDROMO')
