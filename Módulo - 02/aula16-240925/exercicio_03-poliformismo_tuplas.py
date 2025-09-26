class Conta():
    def __init__(self, saldo:float) -> None:
        self.saldo = saldo

    def obter_saldo(self) -> float:
        return self.saldo

class ContaPoupanca(Conta):
    def __init__(self, saldo:float, juros:float) -> None:
        self.juros = juros
        super().__init__(saldo)
        self.juros = juros

    def obter_saldo(self) -> tuple:
        return (self.saldo, self.juros)

conta_corrente = Conta(saldo=1000.00)
conta_poupanca = ContaPoupanca(saldo=5000.00, juros=0.05)

saldo_conta_corrente = conta_corrente.obter_saldo()
saldo_poupanca = conta_poupanca.obter_saldo()

