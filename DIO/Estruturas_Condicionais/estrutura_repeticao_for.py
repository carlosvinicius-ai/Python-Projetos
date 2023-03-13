texto = input('Informe o texto: ')
vogais = 'AEUIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=' ')
else:
    print()