# Peça a idade e se o usuario tem cnh: True ou False;
# Use if-elif-else com operadores logicos and e or para:
# Se for maior de 18 e tiver cnh: Pode dirigir
# Se for maior de 18 e não tiver cnh: Não pode dirigir, tem que tirar a cnh
# Se for menos de 18 anos: Não pode dirigir.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    tem_cnh = input("Você tem CNH? (True/False): ").strip().lower() == 'true'
    if tem_cnh:
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir, tem que tirar a CNH.")
else:
    print("Você não pode dirigir.")
