import random as rd

def jogar():
    
    print("{:=<30}".format('='))
    print("Bem-vindo(a) ao jogo de Advinhação")
    print("{:=<30}".format('='))

    numero_secreto = 0 
    # random gera entre 0.0 e 1.0
    # randrange gera numero aleatorio no intervalo que eu quiser
    # round para arredondar o numero
    tentativas = 0
    pontos = 0
    pontos_maximo = 0
    numero_gerado = 0


    print('Qual nível você de dificuldade você deseja para jogar?')
    print('(1) Fácil \n(2) Médio \n(3) Difícil')
    nivel = int((input('Defina o nível: ')))

    if(nivel == 1):
        tentativas = 20
        numero_secreto = rd.randrange(1, 31)
        pontos = 150
        pontos_maximo = 150
        numero_gerado = 30
    elif(nivel == 2):
        tentativas = 10
        numero_secreto = rd.randrange(1, 61)
        pontos = 300
        pontos_maximo = 300
        numero_gerado = 60
    elif(nivel == 3):
        tentativas = 5
        numero_secreto = rd.randrange(1, 101)
        pontos = 500
        pontos_maximo = 150
        numero_gerado = 100
        
    for rodada in range(1, tentativas + 1):
        print('tentativa {} de {}'.format(rodada, tentativas), numero_secreto)
        chute = int(input("Digite o seu número entre 1 e {}: ".format(numero_gerado)))
        print("Você digitou:", chute)
        
        if(chute < 1 or chute > numero_gerado): # or para escolher entre um ou outro
            print('você deve digitar um numero entre 1 e {}!'.format(numero_gerado))
            continue #Para continuar o programa 
        

        if(chute == numero_secreto):
            print('Você acertou em {} tentivas e fez {} pontos de {} pontos possiveis!'.format(rodada, pontos, pontos_maximo)) 
            break # Para finalizar o programa
        else:
            if(chute > numero_secreto):
                print("Você errou seu numero é maior que o numero secreto")
            elif(chute < numero_secreto):
                print("Você errou seu numero é menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute) #abs é utilizado para transformar numero negativo em numero absoluto
            pontos = pontos - pontos_perdidos
        

    print('O numero secreto era:', numero_secreto)        
    print('FIM DO JOGO')


if(__name__ == '__main__'):     #ele seta automaticamente uma variavel e isso é para fazer a verificação
    jogar()