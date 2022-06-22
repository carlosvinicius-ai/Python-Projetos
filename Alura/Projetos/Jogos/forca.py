import random as rd

def jogar():

    abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = incializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False #bool
    acertou = False
    erros = 0
    
    #Enquanto não enforcou e não acertou contiua
    while(not enforcou and not acertou):     
        chute = pede_chute()
        
        
        if(chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        if(acertou):
            mensagem_acerto()
        elif(enforcou):
            mensagem_erro(palavra_secreta)


def abertura():
    print('{:=<30}'.format('='))
    print('Bem-vindo(a) ao jogo da Forca')
    print('{:=<30}'.format('='))


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # para pegar um arquivo escolhido
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = rd.randrange(0, len(palavras))  # para aleatorizar seguindo o tamanho do arquivo

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def incializa_letras_acertadas(palavra):
    return ['_' for letra in palavra] #Criação da lista

def pede_chute():
    chute = input('Qual letra: ')
    chute = chute.strip().upper()  # strip é utilizado para não contar os espaços
    return chute


def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[
                index] = letra  # alterando o valor da lista para as letras colocadas se forem de acordo com a palavra secreta
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_acerto():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_erro(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()