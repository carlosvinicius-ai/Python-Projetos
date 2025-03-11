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

print(resultado_primeiro_digito)


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


print(segundo_digito)