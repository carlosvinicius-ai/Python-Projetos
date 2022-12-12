import math

x0 = int(input('Digite a coordenada x do primeiro plano: '))
y0 = int(input('Digite a coordenada y do primeiro plano: '))
x1 = int(input('Digite a coordenada x do segundo plano: '))
y1 = int(input('Digite a coordenada y do segundo plano: '))

a = (x1 - x0)**2 + (y1 - y0)**2
b = math.sqrt(a)

if b >= 10:
    print('longe')
else:
    print('perto')

