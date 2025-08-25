# Peça a idade de uma pessoa
# use if-else para classifica a idade em
# "Criança" (0 a 12)
# "Adolescente" (13 a 17)
# "Adulto" (18 a 99)

idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Ela é criança.")
elif idade <= 17:
    print("Ela é Adolescente.")
elif idade <= 59:
    print("Ela é Adulto")
else:
    print("Ele é um Idoso")