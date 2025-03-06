'''
Tipo list - mutavel
Suporta vários valores de qualquer tipo
Métodos úteis -> append, insert, pop, del, clear, extend
Create, Read, Update, Delete -> CRUD
'''

lista = [1, 2, 3, 4]
lista_a = [7, 12, 100]
lista_c = lista_a + lista #Concatenação de lista
lista[2] = 300 #Update
print(lista)
del lista[2] # Delete
print(lista)
lista.append(35) # adiciona um item ao final da lista
print(lista)
lista.pop() #remove o ultimo item da lista e guarda o valor
print(lista)
lista.insert(0, 19) # adiciona o item na posição passada
print(lista)
print(lista_c)
lista_a.extend(lista) # Altera a lista que está recebendo o valor
lista.clear() #limpa a lista e a deixa vazia = None