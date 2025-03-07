'''
Listas de listas e seus indices
'''

salas = [
    ['Maria', 'João'],
    ['Elaine'],
    ['Pedro', 'Roberto', 'Jacinto']
]

print(salas[0][1])
print(salas[2][2])
print(salas[2][1])

for sala in salas:
    print('A sala é: ')
    for aluno in sala:
        print(aluno)