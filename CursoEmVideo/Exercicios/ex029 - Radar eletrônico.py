# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('='*50)
print('Exercício 29 – Radar eletrônico')
print('='*50)

carro = float(input('\nDigite a velocidade que o carro estava: '))

if carro > 80:
    print('O carro passou a {:.1f}KM/h em uma via de 80KM/h e pagará {:.2f}R$ de multa'.format(carro,(carro - 80) * 7))
else:
    print('O carro passou a velocidade {}KM/h. Tenha um bom dia e dirija com segurança!'.format(carro))