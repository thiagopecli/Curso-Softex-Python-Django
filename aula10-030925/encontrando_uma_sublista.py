lista_principal = [10, 20, 30, 40]
sublista = [10, 50, 60, 70]

len_principal = len(lista_principal)
len_sublista = len(sublista)

for numero in range(len_principal - len_sublista + 1):
    fatia = lista_principal[numero : numero + len_sublista]
    if fatia == sublista:
        print(f"Sub-lista encontrada. Começa no indice: {numero}")
        break
else:
    print("A sub-lista não foi localizada na lista principal.")