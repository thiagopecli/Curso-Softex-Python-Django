"""2.  Imutabilidade da Tupla: 
Crie a tupla dias_da_semana = ('segunda', 'terça', 'quarta'). 
Tente adicionar um novo dia a essa tupla e observe o tipo de erro que ocorre."""

dias_da_semana = ("Segunda", "Terça-Feira", "Quarta-feira")
print(f"Tupla original: {dias_da_semana}")

dias_da_semana.append("Quinta-Feira")

print("Tentativa de adicionar 'Quinta-feira' a uma tupla resulta em um 'AttributeError'.")
print("-" * 25)