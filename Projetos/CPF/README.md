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
