import random as rd

print("{:=<30}".format('='))
print("Bem-vindo(a) ao jogo de Advinhação")
print("{:=<30}".format('='))

numero_secreto = rd.randrange(1, 101) 
# random gera entre 0.0 e 1.0
# randrange gera numero aleatorio no intervalo que eu quiser
# round para arredondar o numero
tentativas = 0
pontos = 500

print('Qual nível você de dificuldade você deseja para jogar?')
print('(1) Fácil \n(2) Médio \n(3) Difícil')
nivel = int((input('Defina o nível: ')))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
elif(nivel == 3):
    tentativas = 5
    
for rodada in range(1, tentativas + 1):
    print('tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou:", chute)
    
    if(chute < 1 or chute > 100): # or para escolher entre um ou outro
        print('você deve digitar um numero entre 1 e 100!')
        continue #Para continuar o programa 
    

    if(chute == numero_secreto):
        print('Você acertou em {} tentivas e fez {} pontos de 500 pontos possiveis!'.format(tentativas, pontos)) 
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


