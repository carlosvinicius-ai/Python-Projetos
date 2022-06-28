class Conta:

    def __init__(self, numero, titular, saldo, limite):     # __init__ é uma função contrutora
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor