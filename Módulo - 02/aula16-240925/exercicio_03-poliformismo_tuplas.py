class Conta():
    def __init__(self, saldo:float) -> None:
        self.saldo = saldo

    def obter_saldo(self) -> float:
        return self.saldo

class ContaPoupanca(Conta):
    def __init__(self, saldo:float, juros:float) -> None:
        super().__init__(saldo)
        self.juros = juros

    def obter_saldo(self) -> float:
        return self.saldo * (1 + self.juros)
    
    def obter_detalhes(self) -> tuple:
        return (self.saldo, self.juros)

conta_corrente = Conta(saldo=1000.00)
conta_poupanca = ContaPoupanca(saldo=5000.00, juros=0.05)

saldo_conta_corrente = conta_corrente.obter_saldo()
saldo_poupanca = conta_poupanca.obter_saldo()

print(f"Saldo Conta Corrente: R$ {saldo_conta_corrente:.2f}")
print(f"Saldo Conta Poupança (com juros): R$ {saldo_poupanca:.2f}")