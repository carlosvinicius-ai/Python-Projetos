# AND = para ser verdadeiro tudo tem que ser TRUE
# OR = para ser verdadeiro apenas 1 tem que ser TRUE

print(True and True)
print(True and False)
print(True or True)
print(True or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo = (conta_especial and saque <= saldo)

exp = saldo_suficiente or conta_especial_com_saldo

print(exp)