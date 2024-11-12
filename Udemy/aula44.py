texto = 'Python'

novo_texto = ''
# Para cada letra no texto ele vai repetir 
# Ele vai repetir por um tamanho padrão
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')