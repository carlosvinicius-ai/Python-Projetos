'''
split e join com list e str
split -> divide uma string (list)
join -> une uma string
'''

frase = 'Olha só que, coisa interessante'
lista_de_palavras_cruas = frase.split(',') #separa por padrão no espaço

lista_de_palavras_corrigidas = []
for i, frase in enumerate(lista_de_palavras_cruas):
    lista_de_palavras_corrigidas.append(lista_de_palavras_cruas[i].strip()) #retira o espaço do texto

print(lista_de_palavras_corrigidas)
frases_unidas = '/'.join(lista_de_palavras_corrigidas) #passa as informações que quer unir e o separador que será utilizado
print(frases_unidas)