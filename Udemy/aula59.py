# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena','Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'João'],
    ['Elaine'],
    ['Pedro', 'Roberto', 'Jacinto']
]

print(*lista)
print(*string)
print(*tupla) #o * é utilizado para fazer desempacotamento
print(*salas, sep='\n') # para melhorar a visualização dos dados