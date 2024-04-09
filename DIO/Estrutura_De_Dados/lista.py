lista = ['Programação em Python',
         'Programação em Java',
         'Power BI',
         'Google Cloud',
         'Fundamentos Python',
         'AWS',
         'Microsoft Azure']

# for item in range(1, len(lista)):
#     print(f'O item {item} é {lista[item]}')

for pos, valor in enumerate(lista):
  print(f'O item {pos} é {valor}')

# alterar item da lista

lista[5] = 'Amazon'
print('')

for pos, valor in enumerate(lista):
    print(f'O item {pos} é {valor}')


# adicionar ao final da lista

lista.append('Programação em JavaScript')
print('')

for pos, valor in enumerate(lista):
    print(f'O item {pos} é {valor}')


# adicionar a uma posição especifíca da lista

lista.insert(2, 'Programação em C#')
print('')

for pos, valor in enumerate(lista):
    print(f'O item {pos} é {valor}')


# Organizar a lista

# lista.sort()
print('')

for pos, valor in enumerate(sorted(lista)):
    print(f'O item {pos} é {valor}')

print('')
for pos, valor in enumerate(lista):
    print(f'O item {pos+1} é {valor}')

# colocar a lista ao contrário

lista.reverse()
print('')

for pos, valor in enumerate(lista):
    print(f'O item {pos} é {valor}')

# contar quantas vezes a informação aparece

print(f'\nProgramação aparece {lista.count("Programação em Python")}')

# saber o indice da informação

print(f'O indice da Amazon é {lista.index("Amazon")}')

# apagar informação

del lista[7]
print('')

for pos, valor in enumerate(lista):
    print(f'O item {pos} é {valor}')


# apagar e armazenar

excluir = lista.pop(1)
print('')
print(f'O item {excluir} foi apagado com sucesso')

# apagar por nome

apagar = lista.remove('Amazon')

# limpar a lista

lista.clear()
print('')
print(lista)