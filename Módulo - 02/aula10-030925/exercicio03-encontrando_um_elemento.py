"""3.  Contando Elementos: 
Crie uma tupla numeros = (1, 2, 3, 2, 4, 2). Use o método .count() 
para descobrir quantas vezes o número 2 aparece."""

numeros = (1,2,3,4,5,6,7,8,9)
print(f"Tupla de números: {numeros}")

contagem_do_2 = numeros.count(2)
print(f"O número 2 aparece {contagem_do_2} vezes na Tupla. ")
print("-" * 25)