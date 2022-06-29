class Conta:

    def __init__(self, numero, titular, saldo, limite):     # __init__ é uma função contrutora
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = (self.__limite + self.__saldo)
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {} ultrapassou o limite! Operação cancelada!".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # sempre retorna
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # nunca retorna
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'CAIXA': '104', 'BRADESCO': '237'}