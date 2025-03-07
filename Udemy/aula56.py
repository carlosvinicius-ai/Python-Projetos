"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

numero1 = decimal.Decimal('0.1') #Converter para string para ter maior precisão
numero2 = decimal.Decimal('0.7')
soma = numero1 + numero2

print(round(soma, 2))
print(soma)