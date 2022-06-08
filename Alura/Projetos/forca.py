
def jogar():
    
    print('{:=<30}'.format('='))
    print('Bem-vindo(a) ao jogo da Forca')
    print('{:=<30}'.format('='))
    
    palavra_secreta = 'lindo'
    enforcou = False #bool
    acertou = False
    
    #Enquanto não enforcou e não acertou contiua
    while(not enforcou and not acertou):     
        print('jogando')
    
if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()