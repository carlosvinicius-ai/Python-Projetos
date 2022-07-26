# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('='*50)
print('Exercício 31 – Custo da Viagem')
print('='*50)

distancia = float(input('\nDigite a quilomentragem da viagem: '))

if distancia <= 200:
    print('Você viajou {}KM e a passagem cobrada será no valor de R${:.2f}'.format(distancia, (distancia * 0.50)))
else:
    print('Você viajou {}KM e a passagem cobrada será no valor de R${:.2f}'.format(distancia, (distancia * 0.45)))