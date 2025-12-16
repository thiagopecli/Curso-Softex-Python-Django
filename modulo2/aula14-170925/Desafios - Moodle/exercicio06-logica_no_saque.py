"""Exercício 6: Lógica no Saque
Na mesma classe ContaBancaria, adicione um método para sacar(valor). Este 
método deve verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado 
com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o 
saldo. Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar
 mais do que tem."""

class ContaBancaria():
    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor_a_depositar:float) -> None:
        if valor_a_depositar > 0:
            self.saldo += valor_a_depositar
            print(f"Você depositou R$ {valor_a_depositar:.2f}")
        else:
            print(f"Erro. O valor para depósito deve ser positivo!")
            
    def saque(self, valor_saque:float) -> None:
        if valor_saque <= 0:
            print(f"Erro. O valor para depósito deve ser positivo!")
        elif valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f"Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self) -> None:
        print(f"O saldo atual do {self.titular} é de R$ {self.saldo:.2f}.")

carlos = ContaBancaria("Carlos", 100.00)
print("--- Cenário 1: Saldo Insuficiente ---")
carlos.mostrar_saldo()
carlos.saque(150.00)
carlos.mostrar_saldo()

print("\n--- Cenário 2: Saque Bem-Sucedido ---")
carlos.saque(70.00)
carlos.mostrar_saldo()

print("\n--- Cenário 3: Tentativa de Saque Inválido ---")
carlos.saque(-20.00)
carlos.mostrar_saldo()