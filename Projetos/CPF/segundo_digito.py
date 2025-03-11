cpf = '75016434077'

dez_digitos = cpf[:10]
contador = 11

resultado = 0

for digito in dez_digitos:
    resultado += int(digito) * contador
    contador -= 1

digito = (resultado * 10) % 11
segundo_digito = digito if digito <= 9 else 0

print(cpf)
print(segundo_digito)