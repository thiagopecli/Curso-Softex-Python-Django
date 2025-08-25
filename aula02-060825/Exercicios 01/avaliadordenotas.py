# Avaliador de Notas
# Peça a nota de um aluno(Float):
# Use if-elif-else para atribuir um conceito:
# 9.0 a 10.0: A
# 7.0 a 8.9: B
# 5.0 a 6.9: C
# 3.0 a 4.9: D
# 0.0 a 2.9: E

print("=== Avaliador de Notas ===")
nota = float(input("Digite a nota do aluno: "))
if nota < 0.0 or nota > 10.0:
    print("Nota invalida. Digite uma nota entre 0.0 e 10.0.")
elif nota >= 9.0:
        print("Conceito: A")
elif nota >= 7.0:
        print("Conceito: B")
elif nota >= 5.0:
       print("Conceito: C")
elif nota >= 3.0:
       print("Conceito: D")
else:
       print("Conceito: E")