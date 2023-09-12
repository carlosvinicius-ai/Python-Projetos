nome = input('Qual seu nome? ')

if nome == 'Carlos':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))