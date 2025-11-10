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

"""PS C:\Users\Admin\Desktop\Curso-Softex-Python-Django> python -m venv venv
PS C:\Users\Admin\Desktop\Curso-Softex-Python-Django> .\venv\Scripts\activate
(venv) PS C:\Users\Admin\Desktop\Curso-Softex-Python-Django> pip install -r .\requirements.txt
Collecting asgiref==3.10.0 (from -r .\requirements.txt (line 1))
  Using cached asgiref-3.10.0-py3-none-any.whl.metadata (9.3 kB)
Collecting colorama==0.4.6 (from -r .\requirements.txt (line 2))
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting Django==5.2.7 (from -r .\requirements.txt (line 3))
  Using cached django-5.2.7-py3-none-any.whl.metadata (4.1 kB)
Collecting iniconfig==2.3.0 (from -r .\requirements.txt (line 4))
  Using cached iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging==25.0 (from -r .\requirements.txt (line 5))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy==1.6.0 (from -r .\requirements.txt (line 6))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Pygments==2.19.2 (from -r .\requirements.txt (line 7))
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting pytest==8.4.2 (from -r .\requirements.txt (line 8))
  Using cached pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
Collecting sqlparse==0.5.3 (from -r .\requirements.txt (line 9))
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata==2025.2 (from -r .\requirements.txt (line 10))
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached asgiref-3.10.0-py3-none-any.whl (24 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached django-5.2.7-py3-none-any.whl (8.3 MB)
Using cached iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Using cached pytest-8.4.2-py3-none-any.whl (365 kB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: tzdata, sqlparse, Pygments, pluggy, packaging, iniconfig, colorama, asgiref, pytest, Django
Successfully installed Django-5.2.7 Pygments-2.19.2 asgiref-3.10.0 colorama-0.4.6 iniconfig-2.3.0 packaging-25.0 pluggy-1.6.0 pytest-8.4.2 sqlparse-0.5.3 tzdata-2025.2                                                    

[notice] A new release of pip is available: 25.1.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\Admin\Desktop\Curso-Softex-Python-Django> cd .\modulo4\              
(venv) PS C:\Users\Admin\Desktop\Curso-Softex-Python-Django\modulo4> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 10, 2025 - 09:46:50
Django version 5.2.7, using settings 'meuprojeto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[10/Nov/2025 09:46:52] "GET / HTTP/1.1" 200 916
[10/Nov/2025 09:46:52] "GET /static/css/style.css HTTP/1.1" 200 310
Not Found: /favicon.ico
[10/Nov/2025 09:46:53] "GET /favicon.ico HTTP/1.1" 404 2711"""