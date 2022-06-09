
def jogar():
    
    print('{:=<30}'.format('='))
    print('Bem-vindo(a) ao jogo da Forca')
    print('{:=<30}'.format('='))
    
    palavra_secreta = 'banana'
    enforcou = False #bool
    acertou = False
    
    #Enquanto não enforcou e não acertou contiua
    while(not enforcou and not acertou):     
        chute = input('Qual letra: ')
        chute = chute.strip()  # strip é utilizado para não contar os espaços
        
        index = 0
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index += 1
    
if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()