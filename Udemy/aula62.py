'''
Argumentos nomeados e não nomeados
Argumento nomeado tem nome com sinal de igual -> =
Argumento não nomeado recebe apenas o argumento (valor)
'''

# definição
def soma(x, y, z):
    print(f'{x=} y={y} | x + y = {x + y}')

soma(1,2)
soma(y=2 ,x=1, z=3) # argumentos nomeados