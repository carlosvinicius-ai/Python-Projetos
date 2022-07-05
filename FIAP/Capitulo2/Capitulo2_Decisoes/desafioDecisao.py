nivel = input('Digite seu nivel de permissão: ').upper()
sexo = input('Digite seu sexo (M masculino, F feminino): ').upper()

if (nivel == 'ADM'):
    if (sexo == 'M'):
        print('Olá administrador')
    elif (sexo == 'F'):
        print('Olá adinistradora')
    else:
        print('Olá administrador(a)')

elif (nivel == 'USR'):
    if(sexo == 'M'):
        print('Olá usuario')
    elif(sexo == 'F'):
        print('Olá Usuaria')
    else:
        print('Olá usuario(a)')

elif(nivel == 'GUEST'):
    print('Olá desconhecido(a)')

else:
    print('Ola desconhecido(a)')
    