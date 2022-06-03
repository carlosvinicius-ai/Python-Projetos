print("=" * 30)
print("Bem-vindo(a) ao jogo de Advinhação")
print("=" * 30)

numero_secreto = 25
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    print('tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input("Digite o seu numero: "))
    print("Você digitou: ", chute)

    if(chute == numero_secreto):
        print('Você acertou!')  
    elif(chute > numero_secreto):
        print("Você errou seu numero é maior que o numero secreto")
    elif(chute < numero_secreto):
        print("Você errou seu numero é menor que o numero secreto")
    
    rodada += 1

print('O numero secreto era: ', numero_secreto)        
print('FIM DO JOGO')
