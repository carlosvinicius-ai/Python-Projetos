numero_1 = input('Digite um número: ') # input é utilizado para receber dados do usuário
numero_2 = input('Digite outro número: ') # por padrão ele é str

int_numero_1 = int(numero_1) # conversão do tipo de str -> int
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')