cpf = input('Digite seu cpf: ')

cpf_separado = cpf.split('-') # separando os primeiros 9 digitos
nove_digitos = []

for numero in cpf_separado[0]:
    try:
        numero = int(numero)
        nove_digitos.append(numero) # armazenando os números para calculo
    except ValueError:
        ...

contador = 10
soma_nove_digitos = 0
for numero in nove_digitos:
    soma_nove_digitos += numero * contador 
    contador -= 1

# multiplicando a soma do resultado por 10 e trazendo o resto de 11
primeiro_numero_cpf_calculo = (soma_nove_digitos * 10) % 11 

resultado_primeiro_digito = primeiro_numero_cpf_calculo if primeiro_numero_cpf_calculo <= 9 else 0



# Segundo digito
dez_digitos = nove_digitos.copy()
dez_digitos.append(resultado_primeiro_digito)

contador = 11
resultado = 0

for digito in dez_digitos:
    resultado += int(digito) * contador
    contador -= 1

digito = (resultado * 10) % 11
segundo_digito = digito if digito <= 9 else 0


# verificação
dez_digitos.append(segundo_digito)
novo_cpf = ''
# transformando a lista em texto para poder fazer a verificação da forma correta
for i, digito in enumerate(dez_digitos):
    if i == 2 or i == 5:
        novo_cpf += str(digito)
        novo_cpf += '.'
        continue
    elif i == 8:
        novo_cpf += str(digito)
        novo_cpf += '-'
        continue
    novo_cpf += str(digito)

if cpf == novo_cpf:
    print(f'{cpf} enviado é VÁLIDO')
else:
    print('CPF INVÁLIDO')