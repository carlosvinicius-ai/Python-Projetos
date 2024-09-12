# Calculadora com while

while True:

    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')

    numeros_validos = None

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        numeros_validos = True
    except: 
        numeros_validos = None


    if numeros_validos is None:
        print('Digite um valor válido')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos or len(operador) > 1:
        print('Operador inválido')
        continue

    
    print('Realizando a operação solicitada.\nVerifque abaixo o resultado:')
    if operador == '+':
        print(numero1 + numero2)
    
    elif operador == '-':
        print(numero1 - numero2)

    elif operador == '*':
        print(numero1 * numero2)

    elif operador == '/':
        print(numero1 / numero2)

    sair = input('Quer sair? [s]im: ').lower().startswith('s') # lower -> deixa a letra minuscula / startswish -> verifica a letra que se inicia

    if sair:
        break
