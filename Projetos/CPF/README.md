# CPF 🧑🏽

O algoritmo de validação do CPF calcula o primeiro dígito verificador a partir dos 9 primeiros dígitos do CPF, e em seguida, calcula o segundo dígito verificador a partir dos 9 (nove) primeiros dígitos do CPF, mais o primeiro dígito, obtido na primeira parte.

## Primeiro Digito 🥇

Para fazer o calculo para verificar o primeiro digito do cpf, coletamos a soma dos 9 primeiros digitos, após isso é multiplicado cada um dos valores por uma contagem regressiva que se inicia em 10 (dez)

**Exemplo:** 746.824.890-70

        10  9  8  7  6  5  4  3  2
    X
        7   4  6  8  2  4  8  9  0
    -------------------------------
        70  36 48 56 12 20 32 27 0

Após a realização da multiplicação será necessário somar todos os valores obtidos e multiplicar o resultado desta soma por 10, obtendo esse resultado, irá pegar ele e obter o resto da divisão da conta anterior por 11 (números de digitos do CPF)

Caso o resultado for maior que 9, o digito que irá ser representado será 0, caso contrário, o digito será o resultado da conta

veja o algoritmo aqui [algoritmo primeiro numero](CPF\primeiro_digito.py)

## Segundo Digito 🥈

A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9 primeiros dígitos, mais o primeiro dígito verificador, e vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2

**Exemplo:** 746.824.890-70

        11  10 9  8  7  6  5  4  3  2 
    X
        7   4  6  8  2  4  8  9  0  7
    ----------------------------------
        77 40 54 64 14 24 40 36  0 14

Após a realização da multiplicação será necessário somar todos os valores obtidos e multiplicar o resultado desta soma por 10, obtendo esse resultado, irá pegar ele e obter o resto da divisão da conta anterior por 11 (números de digitos do CPF)

Caso o resultado for maior que 9, o digito que irá ser representado será 0, caso contrário, o digito será o resultado da conta

veja o algoritmo aqui [algoritmo primeiro numero](CPF\segundo_digito.py)