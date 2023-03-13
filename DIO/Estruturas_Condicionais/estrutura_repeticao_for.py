texto = input('Informe o texto: ')
vogais = 'AEUIOU'

#Exemplo utilizando a funcao built-in range
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=' ')
else:
    print()
    

#Exemplo com range
for numero in range(0, 51, 5):
    print(numero, end= ' ')