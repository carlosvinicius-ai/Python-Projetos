# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

# para o valor aparecer temos que utilizar nossa indentação que é a tabulação
# if e elif precisam de uma condição para funcionar

# posso ter um if sozinho, mas o elif e o else depende do if para funcionar

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:   # else vai funcionar quando nenhuma condição for verdade
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')