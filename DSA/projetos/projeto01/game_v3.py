import random as rd
import pandas as pd
from InquirerPy import prompt
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

def personagem(chances):
    forca = [
        '''
        \033[31m_______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      / \\
        |
       _|___\033[0m
        ''',
        '''
        _______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      / 
        |
       _|___
        ''',
        '''
        _______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      
        |
       _|___
        ''',
        '''
        _______
        |/      |
        |      (_)
        |      \\|
        |       |
        |      
        |
       _|___
        ''',
        '''
        _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |
       _|___
        ''',
        '''
        _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |
       _|___
        ''',
        '''
        _______
        |/      |
        |      
        |      
        |       
        |      
        |
       _|___
        '''
    ]

    return forca[chances]

# gerando a palvra aleatória de acordo com uma base de dados
def palavras(topico):
    dados = pd.read_csv('DSA\projetos\projeto01\jogo_da_forca\dataset\palavra_secreta.csv')
    for k, v in topico.items():
        valor = v
    dados_filtro = dados.query(f'topico == "{valor}"')
    return rd.choice(dados_filtro['nome'].to_list())


def game():
    limpar_tela()
    print('Bem vindo ao jogo da forca!')
    # criando as opções para o usuário
    perguntas = [
        {
         'type': 'list',
         'message': 'Qual tópico você deseja jogar?',
         'choices': ['Jogos', 'Paises', 'Tecnologia'],
        }
    ]
    topico = prompt(perguntas)
    # Escolhendo aleatoriamente um item da lista
    palavra = palavras(topico)

    print('Advinhe a palavra abaixo: \n')

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    chances = 6
    letras_erradas = list()

    while chances > 0:
        print(personagem(chances))
        print(f'{letras_descobertas}')
        print(f'Letras erradas: {letras_erradas}')

        tentativa = input('\nDigite uma letra: ').lower()

        # verificando o tamanho da palavra
        if len(tentativa) > 1:
            print('Digite apenas 1 caracter')
            continue

        # verificando e adicionando através do indice
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            if tentativa in letras_erradas:
                print(f'letra: \033[1m{tentativa}\033[0m já foi tentada anteriormente e não está na palavra, tente outra')
            else: 
                chances -= 1
                letras_erradas.append(tentativa)

        if chances == 0:
            print(personagem(chances))
            print(f'Você errou, a palavra era \033[1;33m{palavra}\033[0m')


        if '_' not in letras_descobertas:
            print(f'Você acertou, a palavra era \033[1;33m{palavra}\033[0m')
            break

    input('Aperte qualquer tecla para sair...')

# Padrão para iniciação de módulo
if __name__ == '__main__':
    game()