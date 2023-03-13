conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque Realizado')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com cheuqe especial')  
    else:
        ('Saldo insuficiente')  
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado')
    else:
        ('Saldo insuficiente')
else:
    print('Tipo de conta não encontrado')