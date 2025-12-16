######## Aleatoriedade: O modulo random ########

# Em muitos programas, precisamos de algo aleatório, como um jogo de dados ou um sorteio. 
# Para isso, Python nos oferece o módulo random. Um módulo é como uma "maleta de 
# ferramentas" extra que podemos usar. Para usá-la, você precisa "abrí-la" com o comando 
# import no início do seu código.

# import ramdom: importa as ferramentas:
# random.randin(a,b): retorna o numero aleatório entre "a" e "b"
# random.coice(lista): escolhe um item da lista aleatoriamente.

import random

numero_secreto = random.randint(1, 100)
print(f"O número secreto é {numero_secreto}.")

jogadores = ["Jorge", "Lucas", "Otávio", "Ronald"]
sorteado = random.choice(jogadores)
print(f"O jogador escolhido foi: {sorteado}.")