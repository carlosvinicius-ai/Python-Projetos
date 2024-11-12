"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

secret_word = 'pelumbra'
letter_accept = ''
count = 0

while True:
    letter_input = input('type a letter: ')

    if len(letter_input) > 1:
        print('write just one letter')
        continue

    count += 1

    if letter_input in secret_word:
        letter_accept += letter_input

    format_word = ''
    for letter in secret_word:
        if letter in letter_accept:
            format_word += letter
        
        else:
            format_word += '*'

    print(f'format word is {format_word}')

    if format_word == secret_word:
        break


print('Congratulations!!!!!!! YOU WIN!!!!!')
print(f'The secret word is {secret_word} you need just {count} chances')

