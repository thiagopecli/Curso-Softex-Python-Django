"""7.  Verificação de Pertinência: 
Crie um conjunto frutas = {'maçã', 'banana', 'morango'}. Use 
a palavra-chave in para verificar se a 'banana' está no conjunto."""

frutas = {'maçã', 'banana', 'morango'}
print(f"Conjunto de frutas: {frutas}")

if 'banana' in frutas:
    print("Sim, este conjunto possui a fruta banana.")
else:
    print("Não, a fruta 'banana' não está neste conjunto.")

# Exemplo 02:

if 'abacaxi' in frutas:
    print("Sim, este conjunto possui a fruta abacaxi.")
else:
    print("Não, a fruta 'abacaxi' não está neste conjunto.")
