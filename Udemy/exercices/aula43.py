"""
Qual letra apareceu mais vezes em uma frase
"""

frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'

i = 0
maior = 0
apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra = frase.count(letra_atual)

    if letra_atual.isspace(): #atualizando o valor para não ter loop infinito
        i+= 1
        continue

    if maior < qtd_letra:
        maior = qtd_letra
        apareceu_mais = letra_atual


    i+= 1

print(f'A letra que apareceu mais vezes foi {apareceu_mais} aparecendo {maior} vezes')