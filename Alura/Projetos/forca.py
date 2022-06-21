import random as rd


def jogar():
    
    print('{:=<30}'.format('='))
    print('Bem-vindo(a) ao jogo da Forca')
    print('{:=<30}'.format('='))
    
    arquivo = open("palavras.txt", "r") #para pegar um arquivo escolhido
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    print(palavras)

    numero = rd.randrange(0, len(palavras)) #para aleatorizar seguindo o tamanho do arquivo
    
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta] #Criação da lista
    enforcou = False #bool
    acertou = False
    erros = 0
   
    print(letras_acertadas)
    
    #Enquanto não enforcou e não acertou contiua
    while(not enforcou and not acertou):     
        chute = input('Qual letra: ')
        chute = chute.strip().upper()  # strip é utilizado para não contar os espaços
        
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra #alterando o valor da lista para as letras colocadas se forem de acordo com a palavra secreta    
                index += 1
        else:
            erros += 1
            print('você errou! ainda faltam {} tentativas'.format(6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        if(acertou):
            print('você ganhou!')
        elif(enforcou):
            print('você errou!')

    
if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()