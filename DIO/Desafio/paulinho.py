''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
- "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns casos, é necessário converter/tratar os dados de entrada; 
- "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a impressão dos dados de saída. 
'''

N = int(input())

for i in range(N):
    A, B = input().split()
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")