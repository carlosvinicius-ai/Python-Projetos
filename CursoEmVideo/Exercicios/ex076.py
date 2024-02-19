materiais_escolares = (
    "Lápis", 1.50,
    "Caneta", 2.00,
    "Caderno", 15.00,
    "Borracha", 0.50,
    "Apontador", 1.00,
    "Régua", 3.00,
    "Compasso", 9.50,
    "Mochila", 85.00,
    "Estojo", 10.00,
    "Cola", 2.50
)

print('-'*30)
print(f'{"LISTAGEM DE PREÇO":^30}')
print('-'*30)

for i in range(0, len(materiais_escolares)):
    if i % 2 == 0:
        print(f'{materiais_escolares[i]:.<25}', end = '')
    
    else:
        print(f'R${materiais_escolares[i]:>5.2f}')