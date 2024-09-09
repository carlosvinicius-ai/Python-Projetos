a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

# format é uma função que é utilizada para formatação do texto
formato = string.format(
    nome1=a, nome2=b, nome3=c
) # isto é um parametro nomeado, para organização do código

print(formato)