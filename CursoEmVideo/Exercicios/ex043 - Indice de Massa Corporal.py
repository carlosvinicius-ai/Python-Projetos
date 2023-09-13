# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5: Abaixo do peso, - Entre 18.5 e 2: Peso Ideal, 25 até 30: Sobrepeso, - 30 até 40: Obesidade, - Acima de 40: Obesidade mórbida

peso = float(input('Qual seu peso (em KG): '))
altura = float(input('Qual sua altura (em METROS e utilizando ponto): '))

imc = peso / (altura * altura)

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc < 25:
    print('Você está no PESO NORMAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
