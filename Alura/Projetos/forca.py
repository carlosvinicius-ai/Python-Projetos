
def jogar():
    
    print('{:=<30}'.format('='))
    print('Bem-vindo(a) ao jogo da Forca')
    print('{:=<30}'.format('='))
    
    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_'] #Criação da lista
    enforcou = False #bool
    acertou = False
    
    print(letras_acertadas)
    
    #Enquanto não enforcou e não acertou contiua
    while(not enforcou and not acertou):     
        chute = input('Qual letra: ')
        chute = chute.strip()  # strip é utilizado para não contar os espaços
        
        index = 0
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra #alterando o valor da lista para as letras colocadas se forem de acordo com a palavra secreta
                
            index += 1
    
    print(letras_acertadas)
    
if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()