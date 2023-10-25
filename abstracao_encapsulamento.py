""""
POO = Abstração e encapsulamento


"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f"Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}"
        )

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1 = Conta("Geek", 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 999999999
conta1.limite = 999999999

print(conta1.__dict__)
