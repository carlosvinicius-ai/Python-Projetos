cpf = input('Digite seu cpf: ')

cpf_separado = cpf.split('-') # separando os primeiros 9 digitos
numeros_cpf = []

for numero in cpf_separado[0]:
    try:
        numero = int(numero)
        numeros_cpf.append(numero) # armazenando os números para calculo
    except ValueError:
        ...

contador = 10
soma_numeros_cpf = []
for numero in numeros_cpf:
    soma_numeros_cpf.append(numero * contador) 
    contador -= 1

# multiplicando a soma do resultado por 10 e trazendo o resto de 11
primeiro_numero_cpf = (sum(soma_numeros_cpf) * 10) % 11 

status = primeiro_numero_cpf if primeiro_numero_cpf < 9 else 0

print(status)