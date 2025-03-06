'''
Cuidados com dados mutáveis
copiando valor (imutáveis)
aponta para o mesmo valor na memória (mutável)
'''

nome = 'Carlos'
nome = 'Thata' # modifica o valor da variável

lista_a = ['Carlos', 'Thata']
lista_b = lista_a

lista_a[0] = 'Qualquer Coisa'
print(lista_b) # modifica pois está apontando para o mesmo lugar na memória