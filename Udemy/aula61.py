'''
Introdução a funções (def) em Python
Funçoes são trechos de código usados para
replicar determinada ação ao longo do seu código
Elas podem receber vários valores para parâmetros (argumentos)
e retornar um valor específico
Por padrão, funções Python retornam None (nada)
'''

# palavra reservada para a criação de uma função
# def Print():
#     print('Várias')

def imprimir (a, b, c):
    print(a, b, c)

def saudacao(nome):
    print(f'Olá, {nome}')

imprimir(1, 2, 3) # retornando o valor com base em parametros
imprimir(4, 5, 6)

saudacao('Carlos')
saudacao('Thaisa')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)