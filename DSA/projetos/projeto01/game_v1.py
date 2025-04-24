import random as rd
from os import system, name

# limpando a cada execução
def limpar_tela():
    # Windows
    # O '_' é utilizado para não retornar nada
    if name == 'nt':
        _=system('cls')
    # Mac e Linux
    else:
        _=system('clear')

def game():
    limpar_tela()
    print('Bem vindo ao jogo da forca!')
    print('Advinhe a palavra abaixo: \n')

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhendo aleatoriamente um item da lista
    palavra = rd.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    chances = 6
    letras_erradas = list()

    while chances > 0:
        limpar_tela()
        print(f'{letras_descobertas}')
        print(f'Chances restantes: {chances}')
        print(f'Letras erradas: {letras_erradas}')

        tentativa = input('\nDigite uma letra: ').lower()

        # verificando e adicionando através do indice
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)


        if '_' not in letras_descobertas:
            print(f'Você acertou, a palavra era {palavra}')
            break

# Padrão para iniciação de módulo
if __name__ == '__main__':
    game()