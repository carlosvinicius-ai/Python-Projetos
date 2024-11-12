for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue # não le o resto do texto e passa para o proximo item

    if i == 8:
        print('i é 8, seu else não executará')
        break # Quebra o laço de repetição

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')