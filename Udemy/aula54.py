'''
enumerate -> enumera interáveis (indices)
'''

lista = ['Carlos', 'Roberto', 'Jacinto']
lista.append('Ronildo')

for item, valor in enumerate(lista):
    print(item, valor)