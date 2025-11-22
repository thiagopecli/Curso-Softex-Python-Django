# Meus Estudos de Python - Curso Softex Pernambuco

Bem-vindo(a)! Este repositório serve como um diário do meu aprendizado em programação com Python, documentando os exercícios e desafios resolvidos durante o curso de formação da Softex Pernambuco. O objetivo é aplicar os conceitos teóricos em problemas práticos, construindo uma base sólida na linguagem.

## 🚀 Tecnologias e Conceitos Abordados

Ao longo dos módulos e desafios, os seguintes conceitos fundamentais de Python e lógica de programação foram praticados e implementados:

* **Fundamentos de Python:**
    * Variáveis e Tipos de Dados (`int`, `float`, `str`, `bool`) [cite: 7, 9, 13, 18, 23]
    * Operadores (Matemáticos, Relacionais e Lógicos) [cite: 30, 46]
    * Entrada e Saída de Dados (`input()` e `print()`) [cite: 33, 35, 36]
    * Conversão de Tipos (Type Casting) [cite: 37]
    * Estruturas Condicionais (`if`, `elif`, `else`) [cite: 44, 56, 64]
    * Laços de Repetição (`while`, `for`)
    * Controle de Loops (`break`, `continue`) [cite: 86, 87]
    * Manipulação de Strings (f-strings, `.lower()`, `.split()`, `.replace()`, `.capitalize()`, `[::-1]`)

* **Estruturas de Dados:**
    * **Listas:** Criação, manipulação, fatiamento (`slicing`), `append()`, `remove()`, `pop()`, `len()`, `sum()`.
    * **Tuplas:** Criação, acesso por índice, imutabilidade e aninhamento.
    * **Conjuntos (Sets):** Criação, unicidade de elementos, `add()`, `remove()`, e operações (`union`, `intersection`, `difference`, `issubset`).
    * **Dicionários:** Criação, acesso por chave `[]`, método `.get()`, `.items()`, adição e atualização de dados.

* **Lógica de Programação e Algoritmos:**
    * Validação robusta de entrada de usuário (`try-except` e métodos manuais).
    * Resolução de problemas com algoritmos (ex: encontrar o segundo maior, verificar palíndromos, combinar listas ordenadas).
    * Estruturação de código com funções (`def`) para reutilização e clareza.

## 📝 Exercícios e Desafios Resolvidos

O repositório está organizado com os seguintes exercícios e desafios:

### Módulo 1: Fundamentos da Linguagem (Baseado na Apostila)
* **1. Conversor de Moedas Simples** [cite: 98]
* **2. Par ou Ímpar** [cite: 103]
* **3. Maior de Idade** [cite: 108]
* **4. Sistema de Login Básico** [cite: 114]
* **5. Calculadora de Média (Simples)** [cite: 119]
* **6. Classificador de Triângulos** [cite: 124]
* **7. Contador de Vogais** [cite: 130]
* **8. Jogo de Adivinhação Melhorado** [cite: 134]
* **9. Validação de Dados** [cite: 142]
* **10. Calculadora de Média com Repetições** [cite: 146]

### Módulo 2: Desafios de Lógica e Estruturas de Dados
* **Análise Completa de Frase:** Contagem de palavras, vogais, consoantes e verificação de palíndromo.
* **Validação do Triângulo:** Verificação se três lados podem formar um triângulo.
* **Manipulação de Listas:**
    * Encontrando o Segundo Maior Valor (sem usar `.sort()`).
    * Removendo Todas as Ocorrências de um item.
    * Combinando Listas Ordenadas (sem usar `.sort()`).
    * Encontrando uma Sublista e sua posição.
    * Média das Sublistas.
    * Rotacionando uma Lista.
* **Tuplas e Conjuntos:** Exercícios práticos de nível básico, médio e avançado para manipulação de tuplas e conjuntos.
* **Dicionários:** Exercícios práticos para criação, manipulação e consulta de dicionários.
* **Coleta e Processamento de Dados:** Scripts para coletar e processar registros de usuários.

## 📂 Como Utilizar
Cada exercício ou desafio está contido em seu próprio arquivo Python. Sinta-se à vontade para navegar pelos scripts, testar e ver as diferentes abordagens utilizadas para resolver cada problema.

---
*Este repositório está em constante atualização com novos aprendizados e desafios do curso.*

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
pip install -r .\requirements.txt
cd .\modulo4\
python manage.py makemigrations
python manage.py migrate
python .\manage.py runserver