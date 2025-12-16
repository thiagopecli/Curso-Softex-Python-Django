"""Exercício 5: Conta Bancária
Crie uma classe ContaBancaria. Toda conta deve começar com um titular e um 
saldo inicial. Crie um método depositar(valor) que some um valor ao saldo da 
conta. Crie um objeto, deposite um valor e imprima o novo saldo."""

class ContaBancaria():
    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_a_depositar: float) -> None:
        if valor_a_depositar > 0:
            self.saldo += valor_a_depositar
            print((
                f"Deposito de R$ {valor_a_depositar:.2f}, "
                f"realizado com sucesso!"
            ))
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def mostrar_saldo(self) -> None:
        print(f"O saldo atual de {self.titular} é de R$ {self.saldo:.2f}")

carlos = ContaBancaria("Carlos", 0)
carlos.mostrar_saldo()

carlos.depositar(150)
carlos.mostrar_saldo()
