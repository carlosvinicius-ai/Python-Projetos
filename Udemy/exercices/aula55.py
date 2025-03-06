'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
'''
import os

compras = []

while True:
    option = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar [s]air\n').lower()
    os.system('clear')

    if option == 'i':
        valor = input('Digite o item: ')
        compras.append(valor)

    elif option == 'a':
        indice = int(input('Digite o indice: '))
        try:
            compras.pop(indice)
        except:
            print('Indice não existe')

    elif option == 'l':
        if len(compras) == 0:
            print('Lista vazia')
            continue

        for indice, valor in enumerate(compras):
            print(indice, valor)

    elif option == 's':
        break

    else:
        print('Digite uma opção válida')
