"""23. Conversor de Unidades: Crie um dicionário onde as chaves são unidades de medida 
(ex: "metros", "quilômetros") e os valores são seus fatores de conversão para uma base 
única (ex: para metros). Peça ao usuário uma quantidade e uma unidade para converter. """

unidades = {
    "metros": 1,
    "quilometros": 1000,
    "centimetros": 0.01,
    "milimetros": 0.001
}
quantidade = float(input("Digite a quantidade: "))
unidade_origem = input("Digite a unidade de origem (metros, quilometros, centimetros, milimetros): ").lower()
unidade_destino = input("Digite a unidade de destino (metros, quilometros, centimetros, milimetros): ").lower()

if unidade_origem in unidades and unidade_destino in unidades:
    # Converter para metros
    quantidade_em_metros = quantidade * unidades[unidade_origem]
    # Converter de metros para a unidade de destino
    resultado = quantidade_em_metros / unidades[unidade_destino]
    print(f"{quantidade} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}.")
else:
    print("Unidade de medida inválida.")