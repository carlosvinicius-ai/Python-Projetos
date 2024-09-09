# Exercício
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se o nome e a idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A ultima letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     exiba "Desculpe, você deixou campos vazios"

name = input('Insert your name: ')
age = input('Insert your age: ')

if name and age:
    print(f'Your name is {name}')
    print(f'Your name inverted is {name[::-1]}')
    if ' ' in name:
        print('Your name have spaces')
    
    else:
        print("Your name haven't spaces")

    print(f'Your name have {len(name)} letters')
    print(f'The first letter is {name[0]}')
    print(f'The last letter is {name[-1]}')

else:
    print('Sorry, you left fields empty')