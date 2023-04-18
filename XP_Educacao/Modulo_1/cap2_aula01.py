# define o valor da limiar
limiar = 5

maiores = [] # Cria a Lista dos Maiores
menores = [] # Cria a lista dos Menores

# Divide os números de 1 a 10 em maiores e menores

for i in range(10):
    if i < limiar:
        menores.append(i)
    elif i > limiar:
        maiores.append(i)

# imprime na tela os valores da lista
print('Resultado Final: ')
print('menores', menores)
print('maiores', maiores)