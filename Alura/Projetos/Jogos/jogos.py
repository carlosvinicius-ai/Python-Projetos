import forca
import adivinhacao

def escolha_jogo():
    print("{:=<30}".format('='))
    print("Escolha o seu jogo")
    print("{:=<30}".format('='))

    print('(1) Forca \n(2) Advinhação')

    jogo = int(input('Qual jogo: '))

    if(jogo == 1):
        print('jogando forca \n')
        forca.jogar()
    elif(jogo == 2):
        print('jogando adivinhação \n')
        adivinhacao.jogar()
        
if(__name__ ==  '__main__'):
    escolha_jogo()